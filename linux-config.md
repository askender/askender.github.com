/etc/apt/sources.list
deb http://mirrors.163.com/ubuntu/ precise main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-security main restricted universe multiverse

sudo add-apt-repository ppa:shawn-p-huang/ppa
sudo apt-get update
sudo apt-get install ibus-gtk ibus-pinyin ibus-pinyin-db-open-phrase
sudo apt-get install ibus ibus-googlepinyin ibus-sunpinyin

chromium-browser
git
vim
nautilus-open-terminal
python-dev
rhythmbox
subversion
xsel
libspeex1 libflac8
ri ruby-dev ruby1.9.1-examples ri1.9.1 graphviz ruby1.9.1-dev ruby-switch
sudo !!


sudo add-apt-repository ppa:tortoisehg-ppa/releases
sudo add-apt-repository ppa:mercurial-ppa/releases
sudo apt-get update
sudo apt-get install mercurial python-nautilus tortoisehg

zsh oh-my-zsh

python libs:
python-twisted
pyOpenSSL
tftpy
pyansn1
rsa
rq times logbook python-dateutil

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


alias vi='vim'
alias sudo='sudo '
alias ll='ls -lh'
alias la='ls -lhA'
alias l='ls'
alias c='clear'
alias x='exit'
alias q='exit'
alias sagi='sudo apt-get install '
alias shutup='sudo shutdown -h 0'


[alias]
        st = status
        ci = commit
        co = checkout
        br = branch
        glog = log --graph
        dlog = log --decorate
        plog = log -p
        nlog = log --name-status
[color]
        ui = auto
[core]
        editor = vim


!* 将代替上一个命令的所有参数，(!! 是整条命令和所有参数)
!$ 上一条命令的最后一个参数
!:3 上一条命令的第3个参数

virtualenv --no-site-packages pip_test_env
. pip_test_env/bin/activate
