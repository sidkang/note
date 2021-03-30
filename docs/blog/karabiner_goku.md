# Karabinier的高级配置伴侣Goku简介及实用分享

本篇将介绍[Karabiner-Elements](https://github.com/pqrs-org/Karabiner-Elements)以及[Goku](https://github.com/yqrashawn/GokuRakuJoudo)软件的配合使用方法和一些实用的分享。

## 提要


> Karabiner-Elements is a powerful utility for keyboard customization on macOS.

根据以上社区的定义，Karabiner是一款强大的macOS键盘自定义工具，对于很多Mac用户来说应该并不陌生。通过该软件，用户可以做到各种天马行空的自定义键位方案，诸如：

* 交换键盘键位，如Ctrl与Command想换交换；
* 给Fn功能键分配系统默认以外的快捷控制功能，如将F12从原有的提升音量改为静音功能；
* 区分左右两侧修饰键以达到不同的触发结果，如left_command+y和right_command+y可以分别触发不同的事件；
* 针对不同的前台桌面程序，同样的快捷键触发不同的事件；
* 双击某键打开某程序；
* ...

Karabiner的功能可以说相当强大，简单的自定义配置极为便利，比如交换键盘键位、给fn功能键配置不同的媒体控制选项等等；针对其它较为复杂的键盘自定义配置，社区其实提供了一个复杂修改(Compelx Modification)分享网站，网站上的各类规则其实相当丰富，链接地址是[Offical Rule Site](https://ke-complex-modifications.pqrs.org)，从修饰键的通用修改到针对特定键盘的定制规则可谓十分丰富。

但是，就如同工业化生产的西装并不一定适合每个人一样，当你需要如我一般手写一些自定义复杂规则时，最大的问题来了，Karabiner的配置格式均为json格式，这个格式真的是一言难尽，无论读写都是一场灾难，以下是一个可以我自己之前用的一条json规则例子：

```json
一个例子
```

感受如何，是不是读起来特别难受，懂编程的程序员们通过一些编辑器的工具会容易很多，为了给大家做一个直观的比较，提前剧透一下另一种可以达成同样的目的的配置结果：

```
goku样本
```

相比下来是不是好了特别多，无论是可读性（现在可能你还看不太懂），还是编写规则的难易度都有极大的差别。而以上的例子还只是一条规则，当使用的规则多达数十上百时，两种配置语言在可读性方面的差别会更加天差地别。而要想使用这样的格式来编写规则，这就需要介绍本篇的主角Goku了。

## Goku简介

Goku是另一个社区开发的项目，该项目旨在通过简易的格式语言来达到配置Karabiner的目的。Goku使用edn([extensible data notation](https://github.com/edn-format/edn))格式，edn主要是被Clojure语言所使用。

Goku的实现方案是，用户通过直观的edn格式进行书写配置文件，再由Goku转译为json后注入Karabiner的配置文件，Done。

## 初步上手Goku

接下来让大家初步体验Goku的使用方法。

首先，使用`brew`命令安装Goku程序，没有安装`Homebrew`的童鞋可以通过官网自行编译安装：

```bash
brew install yqrashawn/goku/goku
```



## Goku语法简介

---

## Goku使用小技巧

## 我的Goku使用分享

### 背景：我的综合效率软件提要

### 场景01：单键切换输入法

### 场景02：单键切换Command+Tab

### 场景03：快速打开及切换程序

### 场景04：触发拽地KM Macro

## 其它的实用案例

```json
{
  "title": "#Birman Layout",
  "rules": [{
    "description": "Caps×1 to en, Caps×2 to ru",
    "manipulators": [
        {
            "conditions": [
                {
                    "name": "caps_lock pressed",
                    "type": "variable_if",
                    "value": 1
                }
            ],
            "from": {
                "key_code": "caps_lock",
                "modifiers": {
                    "optional": [
                        "any"
                    ]
                }
            },
            "to_if_alone": [
                {
                    "select_input_source": {
                        "input_source_id": "org.sil.ukelele.keyboardlayout.t.russian-ilyabirmantypography"
                    }
                }
            ],
            "type": "basic"
        },
        {
            "from": {
                "key_code": "caps_lock",
                "modifiers": {
                    "optional": [
                        "any"
                    ]
                }
            }, 
            "to_delayed_action": {
                "to_if_canceled": [
                    {
                        "set_variable": {
                            "name": "caps_lock pressed",
                            "value": 0
                        }
                    }
                ],
                "to_if_invoked": [
                    {
                        "set_variable": {
                            "name": "caps_lock pressed",
                            "value": 0
                        }
                    }
                ]
            },
            "to_if_alone": [
                {
                    "select_input_source": {
                        "input_source_id": "org.sil.ukelele.keyboardlayout.t.english-ilyabirmantypography"
                    }
                },
                {
                    "set_variable": {
                        "name": "caps_lock pressed",
                        "value": 1
                    }
                },
                {
                    "key_code": "caps_lock"
                }
            ],
            "type": "basic"
        }
    ]
}]
}
```