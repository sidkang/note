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

### 配置守护进程

编辑systemd service，`sudo nano /etc/systemd/system/clash.service`

```
[Unit]
Description=Clash Daemon
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/local/bin/clash -d /root/clash
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

?> 未了安全性考虑，未来可以考虑使用nobody, nogroup来运行clash daemon

### 透明代理配置

### 待续及可选改进

1. 采用Adguard Home作为CLash Gateway的DNS服务器，进一步加强AD过滤的能力及设置便捷性；
2. 将路由器网关、DNS设置为Clash Gateway地址，这样可以让局域网的客户端无需设置即可科学上网；
3. 暂时还木有想到