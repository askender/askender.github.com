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