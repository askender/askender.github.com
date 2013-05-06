## softwares-config of my mint14

/etc/apt/sources.list
deb http://mirrors.163.com/ubuntu/ precise main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ precise-security main restricted universe multiverse
sudo add-apt-repository ppa:shawn-p-huang/ppa
sudo apt-get update
sudo apt-get install ibus-gtk ibus-pinyin ibus-pinyin-db-open-phrase
sudo apt-get install ibus ibus-googlepinyin ibus-sunpinyin

sudo apt-get install ibus-rime


sudo add-apt-repository ppa:chromium-daily
sudo apt-get update
sudo apt-get install chromium-browser
sudo apt-get update 
sudo apt-get upgrade
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
autojump
zsh
oh-my-zsh
openssh-server
supervisor
sudo su root
echo_supervisord_conf > /etc/supervisord.conf

sudo add-apt-repository ppa:tortoisehg-ppa/releases
sudo add-apt-repository ppa:mercurial-ppa/releases
sudo apt-get update
sudo apt-get install mercurial python-nautilus tortoisehg

haproxy



sudo apt-get install python-software-properties python g++ make
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs npm

sudo add-apt-repository ppa:cheleb/blender-svn
sudo apt-get update
sudo apt-get install blender

sudo add-apt-repository ppa:webupd8team/rhythmbox
sudo apt-get update
sudo apt-get install rhythmbox

## python-libs

python-twisted
pyOpenSSL
tftpy
pyansn1
rsa
rq times logbook python-dateutil
pip install --upgrade autopep8


## alias

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
alias -s log=less
alias -g PR=http_proxy=127.0.0.1:8087
$ PR curl https://twitter.com # 相当于 http_proxy=127.0.0.1:8087 curl https://twitter.com
alias p='ps aux | grep'
alias reload='. ~/.zshrc'

alias gl='git pull --prune'
alias glog="git log --graph --pretty=format:'%Cred%h%Creset %an: %s - %Creset %C(yellow)%d%Creset %Cgreen(%cr)%Creset' --abbrev-commit --date=relative"
alias gp='git push origin HEAD'
alias gd='git diff'
alias gc='git commit'
alias gca='git commit -a'
alias gco='git checkout'
alias gb='git branch'
alias gs='git status -sb' # upgrade your git if -sb breaks for you. it's fun.
alias st='svn status'

## tricks

!* 将代替上一个命令的所有参数，(!! 是整条命令和所有参数)
!$ 上一条命令的最后一个参数
!:3 上一条命令的第3个参数
sudo !!

## python
virtualenv --no-site-packages pip_test_env
. pip_test_env/bin/activate


## git

https://github.com/tpope/vim-pathogen
https://github.com/tpope/vim-sensible
https://github.com/tpope/vim-sleuth

垂直拆分：按Ctrl + W + V
水平拆分：按Ctrl + W + S
关闭当前窗口：按Ctrl + W + Q

mkdir ~/.vim/snippets
vim ~/.vim/snippets/python.snippets


sudo apt-get install figlet

netstat -antup
lsof -i:7071

关闭apache服务
/etc/init.d/apache2


apt-get install mongodb
The following extra packages will be installed:
  libboost-filesystem1.42.0 libboost-program-options1.42.0
  libboost-system1.42.0 libboost-thread1.42.0 libmozjs2d libnspr4-0d
  libpcrecpp0 mongodb-clients mongodb-dev mongodb-server
The following NEW packages will be installed:
  libboost-filesystem1.42.0 libboost-program-options1.42.0
  libboost-system1.42.0 libboost-thread1.42.0 libmozjs2d libnspr4-0d
  libpcrecpp0 mongodb mongodb-clients mongodb-dev mongodb-server


sudo apt-get install amule
sudo apt-get install aria2

sudo killall ibus-daemon
ibus-daemon -d

sudo killall python
ibus-daemon -d -x -r

sudo apt-get install aria2