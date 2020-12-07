# 使用clash作为透明代理


### 方案架构

### 设置dns

> [warning]
> 需要确认是否可以使用adguard

?> 需要将系统设置为静态地址

### 安装clash

下载clash，解压，copy至path目录，并给予执行权限，最后执行`clash -v`进行确认。

```bash
wget https://github.com/Dreamacro/clash/releases/download/v0.18.0/clash-linux-amd64-v0.18.0.gz
gzip -d clash-linux-amd64-v0.18.0.gz
sudo mv clash-linux-amd64-v0.18.0 /usr/local/bin/clash
sudo chmod +x /usr/local/bin/clash
clash -v
```



### 添加配置文件及Dashboard

这里我们使用yacd面板，同时也可以使用clash官方作者所开发的dashboard

```bash
wget https://github.com/haishanh/yacd/archive/gh-pages.zip
```

```yaml
port: 7890
socks-port: 7891
redir-port: 7892
allow-lan: true  # redir port for Linux and macOS
mode: Rule  # Rule / Global/ Direct (default is Rule)
log-level: info  # info / warning / error / debug / silent
external-controller: 0.0.0.0:9090
secret: ""  # optional
external-ui: dashboard
#此处内容请安装一个gui版本的clash然后在里面配置好代理然后抄过来
Proxy:
- { name: "ss1", type: ss, server: server, port: 443, cipher: AEAD_CHACHA20_POLY1305, password: "password" }
Proxy Group:
#
Rule:

- DOMAIN-KEYWORD,netflix,nf
- DOMAIN-SUFFIX,nflxvideo.net,nf

- DOMAIN-SUFFIX,local,DIRECT
- IP-CIDR,127.0.0.0/8,DIRECT

- GEOIP,CN,DIRECT
- MATCH,Proxy
```

```bash
cd ~/.config/
mkdir clash
cd clash
touch config.yaml
wget https://github.com/haishanh/yacd/archive/gh-pages.zip
unzip gh-pages.zip
mv yacd-gh-pages/ dashboard/
```

### 配置守护进程

编辑systemd service，`sudo nano /etc/systemd/system/clash.service`

```
[Unit]
Description=Clash Daemon
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/clash -d /root/.config/clash
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

?> 未了安全性考虑，未来可以考虑使用nobody, nogroup来运行clash daemon

### 透明代理配置

#### 配置ip转发

```bash
sudo echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf
sudo echo "net.ipv6.conf.all.forwarding = 1" >> /etc/sysctl.conf
sysctl -p
# 验证设置情况
cat /proc/sys/net/ipv4/ip_forward
```

#### 配置iptables转发
```bash
iptables -t nat -N clash
iptables -t nat -A clash -d 192.168.0.0/16 -j RETURN
iptables -t nat -A clash -p tcp -j RETURN -m mark --mark 0xff
iptables -t nat -A clash -p tcp -j REDIRECT --to-ports 7892
iptables -t nat -A PREROUTING -p tcp -j clash

# 配置规则持久化
netfilter-persistent save
```

### 待续及可选改进

1. 采用Adguard Home作为CLash Gateway的DNS服务器，进一步加强AD过滤的能力及设置便捷性；
2. 将路由器网关、DNS设置为Clash Gateway地址，这样可以让局域网的客户端无需设置即可科学上网；
3. 暂时还木有想到