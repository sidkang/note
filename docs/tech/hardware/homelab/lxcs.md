# HomeLab VMs

## 200 Gateway

用途：
1. 通过建立SS隧道，将端口暴露至路由器WAN口，使局域网外设备通过Surge类软件能够无痛访问局域网内资源
2. 通过FRP服务端，将局域网外无公网IP的设备将其端口挂载至该LXC，使得其它客户端（局域网内、外）能够进行访问。

### FRP Server

```ini
[common]

bind_addr = 0.0.0.0
bind_port = port
bind_udp_port = port
kcp_bind_port = port

log_file = console
log_level = info
log_max_days = 30

detailed_errors_to_client = true
authenticate_heartbeats = false
authenticate_new_work_conns = false

token = pass_token

tls_only = true
```

### ShadowSocks HomeVPN

```json
{
    "server":"0.0.0.0",
    "server_port":12345,
    "password":"passwd",
    "timeout":300,
    "method":"aes-256-gcm",
    "fast_open":false,
    "nameserver":"8.8.8.8",
    "mode":"tcp_and_udp"
}
```

## 201 Docker Machine

Docker Host之一，全局Proxy

### ACME.SH

```ini
SAVED_HE_Username='user'
SAVED_HE_Password='pass'
USER_PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
```

```bash
# install acme.sh
curl https://get.acme.sh | sh
# renew generic domain certificate
acme.sh --renew --force --dns dns_he --home /mnt/config/acme -d domain.com -d *.sub_domain.domain.com
# Pkcs
acme.sh --toPkcs --home /mnt/config/acme -d sub_domain.domain.com
```

### HomeAssistant

```docker
docker run -d --restart=always \
  --name="ha" \
  -e "TZ=Asia/Shanghai" \
  -v /mnt/config/hass:/config \
  -v /mnt/config/acme:/acme \
  --net=host \
  -e PUID=1005 \
  -e GUID=1005 \
  homeassistant/home-assistant:stable
```

### TimeMachine Container

```docker
docker run -d --restart=always \
  --name timemachine \
  --net=host \
  -e CUSTOM_SMB_CONF="false" \
  -e CUSTOM_USER="false" \
  -e DEBUG_LEVEL="1" \
  -e MIMIC_MODEL="TimeCapsule8,119" \
  -e EXTERNAL_CONF="" \
  -e HIDE_SHARES="no" \
  -e TM_USERNAME="timemachine" \
  -e TM_GROUPNAME="timemachine" \
  -e TM_UID="1005" \
  -e TM_GID="1005" \
  -e PASSWORD="timemachine" \
  -e SET_PERMISSIONS="false" \
  -e SHARE_NAME="TimeMachine" \
  -e SMB_INHERIT_PERMISSIONS="no" \
  -e SMB_NFS_ACES="yes" \
  -e SMB_PORT="445" \
  -e SMB_VFS_OBJECTS="fruit streams_xattr" \
  -e VOLUME_SIZE_LIMIT="1T" \
  -e WORKGROUP="WORKGROUP" \
  -v /mnt/tm:/opt/timemachine \
  -v timemachine-var-lib-samba:/var/lib/samba \
  -v timemachine-var-cache-samba:/var/cache/samba \
  -v timemachine-run-samba:/run/samba \
  mbentley/timemachine:smb
```

## 202 Engine

Docker Host之二，网络直连

## 203 Sync

## 204 Plex

```ini
mp0: /hpool/media,mp=/media
mp1: /hpool/system/config/acme,mp=/acme

net0: name=eth0,bridge=vmbr0,firewall=1,gw=192.168.2.240,hwaddr=5A:CA:16:F3:B7:26,ip=192.168.2.204/24,type=veth
searchdomain: 198.18.0.2

# map 1005
lxc.idmap: u 0 100000 1005
lxc.idmap: g 0 100000 1005
lxc.idmap: u 1005 1005 1
lxc.idmap: g 1005 1005 1
lxc.idmap: u 1006 101006 64530
lxc.idmap: g 1006 101006 64530

# enable gpu
lxc.cgroup.devices.allow: c 226:128 rwm
lxc.cgroup.devices.allow: c 226:0 rwm
lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file
```

## 205 Jellyfin

[Configure Reference](https://jellyfin.org/docs/general/administration/hardware-acceleration.html)

## 206 Webdav

```bash
wget https://github.com/hacdias/webdav/releases/latest/download/linux-amd64-webdav.tar.gz
tar -xzvf linux-amd64-webdav.tar.gz
mv -f webdav /usr/lcocal/bin/

# 01
setcap 'cap_net_bind_service=+ep' /usr/local/bin/webdav # enable <1024 port for specific program with unprivilieged user
# 02
/sbin/sysctl -w net.ipv4.ip_unprivileged_port_start=0

/usr/local/bin/webdav --config /path/of/yaml/config
```

```ini
[Unit]
Description=WebDAV server
After=network.target

[Service]
Type=simple
User=media
ExecStart=/usr/local/bin/webdav --config /mnt/system/config/homelab/webdav/webdav.yaml
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

```yaml
# Server related settings
address: 0.0.0.0
port: 443
auth: true
tls: true
cert: cert_file
key: key_file
prefix: /

# Default user settings (will be merged)
scope: /mnt
modify: true
rules: []

# CORS configuration
cors:
  enabled: true
  credentials: true
  allowed_headers:
    - Depth
  allowed_hosts:
    - http://http_domain:443
  allowed_methods:
    - GET
  exposed_headers:
    - Content-Length
    - Content-Range

users:

  - username: user
    password: passwd
    modify:   true
```

## 240 OSX

[Big Sur on Proxmox Install Guide](https://www.nicksherlock.com/2020/06/installing-macos-big-sur-on-proxmox/)

### Surge(Side Router)

## 250 Win10