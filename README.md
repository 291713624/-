# shisanshui
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/291713624/shisanshui)
![GitHub语言计数](https://img.shields.io/github/languages/count/291713624/shisanshui)
[![codebeat badge](https://codebeat.co/badges/cd68ccd3-014e-410d-9166-cf82dd2ada1e)](https://codebeat.co/projects/github-com-291713624-shisanshui-master)


### 运行环境
---
操作系统：Windows或者Linux，Python版本：3.7及以上，环境依赖python.pyqt5、pyqt5-tools、requests

```
pip install pyqt5
pip install pyqt5-tools
pip install requests
```

### 编译方法

---
Python 3.7、C++
### 使用方法

---

ui部分直接使用Python3.7运行main.py文件即可，因为ui的Python与算法部分c++对接，使用的是py调用命令行执行exe文件的方法，所以需要将shisanshui.exe放在D盘根目录之下才能执行出牌功能，或者在游戏界面.py中更改exe文件的绝对路径。
<br>战局记录需要点一下刷新才行，查询战局详情直接点击查询然后在新的窗口输入战局id查询。
<br>ui实现得较为简单，如果有违看客您的审美，十分抱歉！
