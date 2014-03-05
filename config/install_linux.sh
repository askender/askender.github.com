sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove

# sudo add-apt-repository ppa:chromium-daily
# sudo add-apt-repository ppa:nginx/stable
sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo add-apt-repository ppa:webupd8team/java
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-add-repository ppa:swi-prolog/stable

sudo apt-get install git
sudo apt-get install chromium-browser
sudo apt-get install zsh
sudo apt-get install curl
sudo apt-get install nautilus-open-terminal
sudo apt-get install sublime-text
sudo apt-get install sublime-text-installer
sudo apt-get install virtualbox
sudo apt-get install virtualbox-guest-additions-iso
sudo apt-get install oracle-java7-installer
sudo apt-get install vim
sudo apt-get install redis
sudo apt-get install mongodb
sudo apt-get install build-essential python-dev
sudo apt-get install make
sudo apt-get install python-pip
sudo apt-get install python-imaging
sudo apt-get install gparted
sudo apt-get install python-software-properties g++ make
sudo apt-get install nodejs
sudo apt-get install tmux
sudo apt-get install xfonts-wqy
sudo apt-get install xfce4-terminal
sudo apt-get install ranger caca-utils highlight atool w3m poppler-utils mediainfo
sudo apt-get install cmake
sudo apt-get install libboost-all-dev
sudo apt-get install ttf-wqy-microhei
sudo apt-get install flashplugin-nonfree
sudo apt-get install unzip
sudo apt-get install unrar
sudo apt-get install swi-prolog
sudo apt-get install sqlitebrowser

sudo npm install -g npm
sudo npm install -g less
sudo npm install -g coffee-script
sudo npm install -g uglify-js

curl -L https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh | sh
sudo vim /etc/redis/redis.conf

sudo apt-get install nginx
sudo apt-get install mysql-server
sudo apt-get install mysql-workbench
sudo apt-get install libmysqld-dev
sudo apt-get install php5
sudo apt-get install php5-cli php5-cgi php5-fpm php5-mcrypt php5-mysql

sudo apt-get install openssl libssl-dev
sudo apt-get install openssh-server

sudo apt-get install mercurial
sudo apt-get install xsel

sudo apt-get install git-flow
sudo apt-get install rabbitmq-server


# sudo apt-get install chromium-codecs-ffmpeg-nonfree


# http://www.longene.org/forum/viewtopic.php?t=4700
# sudo apt-get install ia32-libs

# vi ~/.hgrc
# [ui]
# Name data to appear in commits
# username = askender <askender43@gmail.com>

curl -Lo- https://raw.github.com/yesmeck/tmuxrc/master/bootstrap.sh | bash
tmux source-file ~/.tmux.conf


sudo apt-get install memchaced
sudo apt-get install openjdk-7-jdk

sudo apt-get install celery

sudo apt-get install mosh
sudo apt-get install subversion
sudo apt-get install memcached
sudo apt-get install collectd
sudo apt-get install emacs


# make install
Thrift
scribe

sudo pip install flake8
sudo pip install autopep8
sudo pip install tornado
sudo pip install pycurl
sudo pip install supervisor
sudo pip install -U numpy
sudo pip install -U pyyaml nltk
sudo python -m nltk.downloader -d /usr/share/nltk_data all


sudo pip install requests
sudo pip install MySQL-python
sudo pip install sqlalchemy
sudo pip install bpython
sudo pip install fabric
sudo pip install pelican
sudo pip install scrapyd
sudo pip install scrapely
sudo pip install markdown
sudo pip install pika

sudo pip install Celery
sudo pip install cloudi
sudo pip install tox
sudo pip install virtualenv
sudo pip install pymmseg
sudo pip install web.py
sudo pip install scribe_client
sudo pip install cython
sudo pip install nose
sudo pip install ipython
sudo pip install pymongo
sudo pip install protobuf
sudo pip install xapian
sudo pip install celerymon
sudo pip install flower
sudo pip install amqp
sudo pip install virtualenv
sudo pip install virtualenvwrapper
sudo pip install markdown2
sudo pip install mongokit
sudo pip install sympy
sudo pip install pyes
sudo pip install whisper
sudo pip install carbon
sudo pip install graphite-web
sudo pip install uwsgi
sudo pip install gevent
sudo pip install pyyaml


export WORKON_HOME=~/Envs
source /usr/local/bin/virtualenvwrapper.sh
toggleglobalsitepackages
mkvirtualenv venv
workon venv
deactivate



mesos
ketama



ptpq



Cassandra
Spark
Mesos

go
Elastic search

apache flume
node ghost
fleex
js react
css topcoat
hadoop


sublimelint
filediffs

hosts

db.blogComments.update
(
	{},
	{$set:{"toUserId":"1"}},
	false,
	true
);


zookeeper client连接
cd /home/admin/zookeeper/zookeeper-3.4.5

sudo bin/zkCli.sh -server localhost:2182

1.安装zope.interface
pip install zope.interface

2.安装kazoo
pip install kazoo
http://kazoo.readthedocs.org/en/latest/basic_usage.html


http://rdc.taobao.com/team/jm/archives/1232

anwen google
find .|xargs grep -ri "base64.encodestring" -l


sudo apt-get install libsnappy-dev
sudo pip install python-snappy
sudo pip install avro

sudo apt-get install libzmq3-dev

sudo pip install pyzmq
sudo pip install python-daemon

sudo apt-get install aptitude

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
sudo su root
echo_supervisord_conf > /etc/supervisord.conf



haproxy





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





bower install underscore

PhantomJS

yo angular
bower install angular-ui


grunt test
grunt server
grunt
 


subl
autopep8

# C:\Program Files\Oracle\VirtualBox\VBoxManage.exe modifyhd "G:\ub1310\ub1310.vdi" --resize 10240

sudo mount -o remount /
mkdir ~/share
sudo mount -t vboxsf share ~/share
/etc/fstab
