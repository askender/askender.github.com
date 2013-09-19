Ctrl+L 选择整行（按住-继续选择下行）
Ctrl+KK 从光标处删除至行尾 
Ctrl+Shift+K 删除整行 
Ctrl+Shift+D 复制光标所在整行，插入在该行之前 
Ctrl+J 合并行（已选择需要合并的多行时） 
Ctrl+KU 改为大写 
Ctrl+KL 改为小写 
Ctrl+D 选词 （按住-继续选择下个相同的字符串） 
Ctrl+M 光标移动至括号内开始或结束的位置 
Ctrl+Shift+M 选择括号内的内容（按住-继续选择父括号） 
Ctrl+/ 注释整行（如已选择内容，同“Ctrl+Shift+/”效果） 
Ctrl+Shift+/ 注释已选择内容 
Ctrl+Space 自动完成（win与系统快捷键冲突，需修改） 
Ctrl+Z 撤销 
Ctrl+Y 恢复撤销 
Ctrl+Shift+V 粘贴并自动缩进（其它兄弟写的，实测win系统自动缩进无效）
Ctrl+M 光标跳至对应的括号 
Alt+. 闭合当前标签 
Ctrl+Shift+A 选择光标位置父标签对儿 
Ctrl+Shift+[ 折叠代码 
Ctrl+Shift+] 展开代码 
Ctrl+KT 折叠属性 
Ctrl+K0 展开所有 
Ctrl+U 软撤销 
Ctrl+T 词互换 
Tab 缩进 
Shift+Tab 去除缩进 
Ctrl+Shift+UP 与上行互换 
Ctrl+Shift+DOWN 与下行互换 
Ctrl+K Backspace 从光标处删除至行首 
Ctrl+Enter 插入行后 
Ctrl+Shift Enter 插入行前 
F9 行排序（按a-z）

http://cloudaice.com/subline-text2-shortcuts/

sudo add-apt-repository ppa:webupd8team/sublime-text-2
sudo apt-get update
sudo apt-get install sublime-text
按Ctrl+`调出console
粘贴以下代码到底部命令行并回车：
import urllib2,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();os.makedirs(ipp) if not os.path.exists(ipp) else None;open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())
 
subl plugins:
SublimeLinter
AutoPEP8
Python Pep8 Lint
Tag
git
JS Format
Js Minifier
LESS
Pretty JSON
Alignment
FileDiffs
SideBarEnhancements

GBK Encoding Support

git gutter

Ninja IDE (ninja-ide.org)
Ninja IDE(Ninja is not just another IDE) is a cross-platform Python integrated development environment. This IDE sports plenty of good features like built-in PEP8 checking,  linting, tools for managing Plugins and an extensible plugin interface.
Ninja IDE是一个跨平台的PyIDE，这个IDE支持很多的好的特性，比如内建PEP8检测，和一个很好的可拓展的插件界面

BrowserRefresh-Sublime (github.com)
After this plugin you can hit ‘command + shift + r’ on any window in Sublime Text 2 and your Google Chrome window will come to the foreground and reload the active tab. If the current file is unsaved, it
 will be saved before Chrome is activated and reloaded. Awesome!
简单的来说这就是一个live coding，配合Sublime Text 2 和Chrome 快捷键command + shift + r’如果这个文件还没有保存，在这之后它会被保存在Chrome被激活和重载之前

