# HomeLab Setup

为了重新配置一次Homelab，开坑把现有的配置方案记录一遍

## 硬件配置

类型|型号
-|-
主板|AsRock Rack E3C246D2I
CPU|Intel i5-8500
内存|DDR4 复仇者LPX 16Gx2
机箱|mineNAS迈K1
电源|机箱自带
SSD| 256Gb x 2, 512Gb x 1
HDD| 8Tb x 4
PCI-E| TP-LINK 8125 
其他| Oculink to 4xSata连接线

## Host Setup

### About Host OS

Host系统使用proxmox作为底层系统

### 底层配置

#### 系统盘

#### 数据存储

#### 开启PCI-E直通 IOMMU

#### 关闭订阅提示

```shell
sed -i.bak "s/data.status !== 'Active'/false/g" /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js && systemctl restart pveproxy.service
```

### 自定义设置


## Guest OS Setup


lxc.idmap: u 0 100000 1010
lxc.idmap: g 0 100000 1010
lxc.idmap: u 1010 1010 1
lxc.idmap: g 1010 1010 1
lxc.idmap: u 1011 101011 64525
lxc.idmap: g 1011 101011 64525

plex

lxc.idmap: u 0 100000 1010
lxc.idmap: g 0 100000 1010
lxc.idmap: u 1010 1010 1
lxc.idmap: g 1010 1010 1
lxc.idmap: u 1011 101011 64525
lxc.idmap: g 1011 101011 64525
lxc.cgroup.devices.allow: c 226:0 rwm
lxc.cgroup.devices.allow: c 226:128 rwm
lxc.cgroup.devices.allow: c 29:0 rwm
lxc.mount.entry: /dev/dri/renderD128 dev/dri/renderD128 none bind,optional,create=file
lxc.mount.entry: /dev/dri/card0 dev/dri/card0 none bind,optional,create=file
lxc.mount.entry: /dev/dri/fb0 dev/dri/fb0 none bind,optional,create=file

mp1: /hpool/download,mp=/download
mp2: /hpool/media,mp=/media
mp3: /hpool/document,mp=/document
