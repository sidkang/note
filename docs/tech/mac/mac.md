# Mac 配置步骤

半自动配置Mac方案

## First Steps

### 安装必要软件

```zsh
xcode-select --install

# install homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install \
    pyenv pyenv-virtualenv neovim stow starship zsh rustup-init \  # Essential apps
    git bat fd coreutils gnu-time procs ssh-copy-id  # replace default ones
brew install --cask \
    syncthing karabiner-elements keyboard-maestro hammerspoon\  # essentials
    font-jetbrains-mono font-jetbrains-mono-nerd-font font-menlo-for-powerline \  # fonts
    android-file-transfer android-platform-tools \  # android ones
    anki mos dropbox contexts  # daily usage
```

### 必要配置

Dropbox
Syncthing
