# win10 配置留档

## Steps

### 准备

### 安装

### 配置

1. 新建Green文件夹，拷贝KMS及OFFICE工具
2. 设置->App->可选功能-->安装OpenSSH服务端
3. 安装terminal
4. 安装scoop

```cmd
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
iwr -useb get.scoop.sh | iex
scoop install 7zip curl git python sudo which
```