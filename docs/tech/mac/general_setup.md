# 常用配置项

#### 将Office365的语言设置为中文

```bash
defaults write com.microsoft.Word AppleLanguages '("zh-cn")'
defaults write com.microsoft.Excel AppleLanguages '("zh-cn")'
defaults write com.microsoft.Powerpoint AppleLanguages '("zh-cn")'
# 2020/01/05 Onenote这条似乎无法使用
defaults write com.microsoft.OneNote AppleLanguages '("zh-cn")'
```