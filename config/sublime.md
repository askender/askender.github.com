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

