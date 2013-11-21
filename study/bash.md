cp -frap new/* test/
scp -r ask@192.168.0.142:/home/ask/ .

递归查找所有Python文件并统计文件行数
find . -name '*.py' | xargs wc -l
lsof | grep '/usr/lib'


lsof -i
实时查看本机网络服务的活动状态

curl ifconfig.me

netstat -tlnp
ctrl-x e

ps aux | sort -nk +4 | tail
列出头十个最耗内存的进程

curl -u user:pass -d status=”Tweeting from the shell” http://twitter.com/statuses/update.xml

curl -u askender43@gmail.com:pass  https://mail.google.com/mail/feed/atom

vi 保存只有root可以写的文件
:w !sudo tee %

du -hx --max-depth=1 | sort -rh | head -10
列出当前目录里最大的10个文件或文件夹

热建alt+. 或 esc+. 可以把上次命令行的参数给重复出来。
^old^new
替换前一条命令里的部分字符串

sudo !!

!$是一个特殊的环境变量，它代表了上一个命令的最后一个字符串


netstat -apn |grep 80
lsof -i:被占用的端口号
uname -a
cat /proc/version


cat ~/.bash_history | sed "s|sudo ||g" | cut -d " " -f 1 | sort | uniq -c | sort -n

rsync -avSH ~/tmp 58:/home/lb/
cconv -f UTF8-CN -t UTF8-TW


查看处理器信息：cat /proc/cpuinfo
查看BIOS版本：dmidecode
查看网卡驱动及固件信息：ethtool -i eth0

* ctrl + R 可以快速的输入历史命令
* ctrl + A 到 命令行首 , ctrl + E 到命令行尾


Linux.txt

10 个最酷的 Linux 单行命令
2010-03-19 Toy Posted in Cli, Featured, TipsRSS
下面是来自 Commandlinefu 网站由用户投票决出的 10 个最酷的 Linux 单行命令，希望对你有用。

sudo !!

以 root 帐户执行上一条命令。

python -m SimpleHTTPServer

利用 Python 搭建一个简单的 Web 服务器，可通过 http://$HOSTNAME:8000 访问。

:w !sudo tee %

在 Vim 中无需权限保存编辑的文件。

cd -

更改到上一次访问的目录。

^foo^bar

将上一条命令中的 foo 替换为 bar，并执行。

cp filename{,.bak}

快速备份或复制文件。

mtr google.com

traceroute + ping。

!whatever:p

搜索命令历史，但不执行。

$ssh-copy-id user@host

将 ssh keys 复制到 user@host 以启用无密码 SSH 登录。

ffmpeg -f x11grab -s wxga -r 25 -i :0.0 -sameq /tmp/out.mpg

把 Linux 桌面录制为视频。

关于 Commandlinefu ，本站去年曾作介绍，不熟悉的朋友可点击查看。

linux3.txt
Linux Shell快捷方式
# Ctrl + A - Go to the beginning of the line you are currently typing on
# Ctrl + E - Go to the end of the line you are currently typing on
切到命令行开始｜结尾

# Ctrl + L - Clears the Screen, similar to the clear command
清屏，类似于 clear 命令

# Ctrl + U - Clears the line before the cursor position. If you are at the end of the line, clears the entire line.
清除光标以前

# Ctrl + H - Same as backspace
退格键 backspace

# Ctrl + R - Let’s you search through previously used commands
从命令历史中找

# Ctrl + C - Kill whatever you are running
终止命令

# Ctrl + D - Exit the current shell
退出 shell

# Ctrl + Z - Puts whatever you are running into a suspended background process. fg restores it.
??

# Ctrl + W - Delete the word before the cursor
清除光标之前

# Ctrl + K - Clear the line after the cursor
清除光标之后

# Ctrl + T - Swap the last two characters before the cursor
# Esc + T - Swap the last two words before the cursor
切换光标前最后两个字母（单词）

# Alt + F - Move cursor forward one word on the current line
# Alt + B - Move cursor backward one word on the current line
??在 ubuntu x windows终端中会切换到菜单！tty 可能可以

# Tab - Auto-complete files and folder names
自动补全

# Ctrl + Y - to paste it (as in delete and copy) all text in front of the cursor
粘贴（刚才 ctrl+w 或者 ctrl+k 的内容）

# Esc + . (or Esc + Underscore) - Insert Last Argument
??

# Ctrl + b - Move back a character
# Ctrl + f - Move forward a character
向前｜后移动一个字母

# Ctrl + r - Search the history backwards
??
# Ctrl + xx - Move between EOL and current cursor position
光标在当前位置和 EOL 之间切换（EOL end of line?但我实验，是在开头和当前位置之间切换，怎么理解？谁知道？）

# Ctrl + x @ - Show possible hostname completions

# Alt +
# Alt + > - Move to the last line in the history

# Alt + ? - Show current completion list

# Alt + * - Insert all possible completions

# Alt + / - Attempt to complete filename

# Alt + . - Yank last argument to previous command

# Alt + c - Capitalize the word

# Alt + d - Delete word

# Alt + l - Make word lowercase

# Alt + n - Search the history forwards non-incremental

# Alt + p - Search the history backwards non-incremental

# Alt + r - Recall command

# Alt + t - Move words around

# Alt + u - Make word uppercase

# Alt + back-space - Delete backward from cursor

# Here "2T" means Press TAB twice

# $ 2T - All available commands(common)

# $ (string) 2T - All available commands starting with (string)

# $ /2T - Entire directory structure including Hidden one

# $ 2T - Only Sub Dirs inside including Hidden one

# $ *2T - Only Sub Dirs inside without Hidden one

# $ ~2T - All Present Users on system from "/etc/passwd"

# $ $2T - All Sys variables

# $ @2T - Entries from "/etc/hosts"

# $ =2T - Output like ls or dir

linux2.txt
ACCTCOM	::
查看所有用户执行过的进程（命令）	acctcom | tail -20
查看指定用户执行过的进程（命令）	acctcom -u <username> | tail -20
使用一个正则表达式查找相关进程	acctcom -n <pattern> | tail -20
查找所有以l开头的被用户执行过的命令	acctcom -n ‘^l’ | tail -30
以反向顺序显示	acctom -b | more
AGREP	::
在文件中查找一个可能拼写错的单词	agrep -2 ‘macropperswan’ <file>
AT	::
在未来某个时间执行某个命令	at now + 5 days < scriptfile
AWK	::
显示文件的第一列	awk ‘{print $1}’ <file>
反序显示文件的前两列	awk ‘{print $2,”\t”,$1}’ <file>
输出前两列的总和	awk ‘{print $1 + $2}’ <file>
查找所有包括”money” 行并输出最后一列	awk ‘/money/ {print $NF}’ <file>
查找第二列中包含 “money”	awk ‘$2 ~ /money/ {print $0}’ <file>
查找第三列中不包括”A”	awk ‘$3 !~ /A$/ {print $0}’ <file>
BC	::
计算sin(5)的值	echo ‘s(5)’ | bc -l
CANCEL	::
取消一个刚开始启动的打印的作业	cancel <jobid> ( jobid可以由lpstat -o输出)
CASE in ESAC	::
sh/bash/ksh中的case语句
CC	::
编译一个C文件file.c	cc -o <outfile> <infile>
CHGRP	::
修改文件的组所属	chgrp <newgroupname> <file>
CHOWN	::
修改文件的所属人	chown <newowner> <file>
CMP	::
比较两个文件	cmp <file1> <file2> || <command>
COL	::
打印man pages，去除其中 “^H”	man <command> | col -b | <printcommand>
CRONTAB	::
查看你的crontab 文件	crontab -l
编译 crontab 文件	crontab -e
第周一的05:10 执行/home/fred/foo.ksh	10 5 * * 1 /home/fred/foo.ksh
CRYPT	::
使用一个口令加密一个文件	crypt password < infile > cryptfile
解密一个被上面命令加密了的文件	crypt password < cryptfile > cleanfile
CSH	::
最好的Berkley shell
CUT	::
从last 命令的输出中得到hostname字段	last | cut -c11-40
DATE	::
设置时间(只能由root 执行)	date <mmddhhmm>
输出指定日期格式 (如：月份)	date +%m
DF	::
以kB单位查看磁盘空间	df -k
DIRCMP	::
比较两个目录	dircmp <dir1> <dir2>
DTKSH	::
dtksh 是一个 X11 图形的ksh93	dtksh
DU	::
磁盘使用情况	du -ks
ED	::
命令行编译器。	ed <file>
EGREP	::
使用“或”条件Grep 文件	egrep ‘(A|B)’ <file>
grep文件中即不包括A也不包括B	egrep -v ‘(A|B)’ <file>
EX	::
使用一个shell脚来来编辑一个文件	ex -s file <<EOF
g/money/s//cash/
EOF
以一个脚本文件来编辑一个文件	ex -s file < scriptfile
EXPR	::
求模	expr 10 % 7
查看字串是否在变量$var中	expr $var : ‘string’
显示第一个数字组成的字串	expr $var : ‘[^0-9]*\([a-z]*\)’
FGREP	::
查找不匹配于某正规表达式的文件行	fgrep ‘*,/.()’ <file>
FILE	::
查看文件类型(如： ascii)	file <file>
FIND	::
在整个文件系统中查的一个文件	find / -type f -name <file> -print
查找所有匹配于模式的文件	find . -type f -name “*<foo>*” -print
删除系统中所有的core文件	find / -type f -name core -exec /bin/rm -f {} \;
查找所有包含某单词的文件	find . -type f -exec grep -l <word> {} \;
查找所有修改日期在30天以前的文件	find . -type f -ctime +30 -print
使用xargs来备份所有的.c文件（加上.bak后缀）	find . -name “*.c” -print | xargs -i cp {} {}.bak
只搜索本地文件系统（不搜索nfs文件系统）	find . -local …
在搜索的过程中，跟随link文件的实际位置	find . -follow …
查找大于1M的文件	find /path -size 1000000c -print
运行find命令但忽略”permission denied”	find … 2>/dev/null ( 只能在sh/bash/ksh )
查找所有的man目录	find / -type d -print | egrep ‘.*/(catman|man)$’
查找所有有写权限的目录	find / -type d -perm -002 -print
GAWK	::
GNU版本的nawk
GREP	::
以某个正规表达式查找包含其的文件行	grep ‘[a-z][0-9]‘ <file>
查找不包含指定正则表达式的文件行	grep -v ‘^From’ <file>
查找一组文件	grep -l ‘^[cC]‘ *.f
计算包括某正则表达式文件行的数目	grep -c ‘[Ss]uccess’ <file>
不区分大小写的查找	grep -i ‘lAbEgF’ <file>
在匹配到的文件内容前输出文件的行号	grep -n ‘mo.*y’ <file>
HINV	::
命令显示系统硬件的详细列表，包括：CPU类型、内存大小、所有的磁盘设备。	hinv -v
IF then else ENDIF	::
csh/tcsh中的if 语句
IF then else FI	::
sh/bash/ksh 中的if 语句	if [[ condition ]];then commands;fi
KSH	::
Korn shell. (ksh88)
LN	::
创建一个硬链接文件a链接到文件A	ln a B
创建一个符号链接文件a链接到文件A	ln -s a B
删除链接文件B	rm B
LP	::
在默认打印机上打印文件	lp <file>
在指定打印机上打印文件	lp -d <destination> <file>
LPSTAT	::
显示所有的打印机	lpstat -a
查看打印机任务队列	lpstat -o
查看默认打印机	lpstat -d
查看打印机状态	lpstat -p
查看计划任何状态	lpstat -r
MAKE	::
执行一个 makefile中的第一个目标	make
执行一个 makefile中的指点目标	make <target>
指定一个特定的makefile文件名	make -f <mymakefile>
显示要做什么，但其实什么也没做	make -n <target>
MKDIR	::
一次创键目录和子目录	mkdir -p <path>/<path>/<path>
MOUNT	::
查看挂载的文件卷	mount
查看挂载的文件卷（有格式的）	mount -p
挂载一个光驱到目录/cdrom	mount /dev/cdrom /cdrom
挂载一个磁盘分区到目录 /usr	mount /dev/dsk/c0t3d0s5 /usr
NAWK	::
增强版的 awk
NL	::
以带行号的方式输出文件	nl -bt -nln <file>
NOHUP	::
启动一个命令马上退出	nohup <command> &
PACK	::
一个很老的文件打包程序，现在被gzip代替了。	pack <file>
PASSWD	::
修改你的帐号口令	passwd
删除一个用户的口令(root使用)	passwd -d <username>
改变一个用户的口令 (root使用)	passwd <username>
PASTE	::
以列的方式把多个文件组合起来	paste <file1> <file2> > <newfile>
PERL	::
Perl脚本语言的解释器
PR	::
把一个文件做成可打印的格式（76行一页）	pr -l76 -h”title” <filename>

REGCMP	::
从一个文件中编译正则表达式	regcmp <file>
文件内容示例	varname “^[a-z].*[0-9.*$"
RESET	::
重置终端设备	reset
RPCINFO	::
取得某主机的TCP端口信息	rpcinfo -p <host>
RSH	::
执行一个远程服务器上的命令	rsh <host> <comand>
SCRIPT	::
用来捕捉当前的终端会话中的所有输入输出结果到一个指定的文件	script <logfile>
SED	::
把某文件中的fred替换成john	sed -e 's/fred/john/g' <file>
替换文件中匹配正则表达式的字符串	sed -e 's/[0-9]+/number/g’ <file>
把HTML文件中的 “X” 变成红色	sed -e ‘s!X!<font color=”#FF0000″>X</font>!g;
把所有后缀为.suf1 改名成.suf2	ls -1 | grep ‘\.suf1$’ | sed -e ‘s/\(.*\.\)suf1/mv & \1suf2/’ | sh
把文件中包含c的行中的a 替换成b	sed -e ‘/C/s/A/B/’ <infile> ><outfile>
删除所有包含 “you owe me”的文件行	sed -e ‘/you owe me/d’ <infile> > <outfile>
使用commandfile中的命令来编译infile文件，并输出到outfile中。其中的commandfile中包含了一系列的vi命令	sed -f <commandfile> <infile> > <outfile>
SH	::
最老的 AT&T shell程序，也是使用最广泛的标准确shell。
SHUTDOWN	::
关机	shutdown -h now
SLEEP	::
sleep 10秒钟	sleep 10
SORT	::
以字符顺序把文件的每一行排序	sort <file>
以数字顺序把文件的每一行排序	sort -n <file>
反向排序	sort -r <file>
排序时对于重复项只保留一个	sort -u <file>

SPELL	::
检查拼写错误	spell <file>
检查拼写错误，但是忽略okfile中包含的单词	spell +<okfile> <file>
SPLIT	::
拆分一个大文件，每个文件1m	split -b1m <file>
把拆分后的文件合并起来	cat x* > <newfile>
STRINGS	::
从二进制文件中读取ascii 字符串	strings <file>
STTY	::
显示终端设置	stty -a
设置 Ctrl+”H”为删除键	stty erase “^H”
对于用户的输入不回显	stty -echo
回显用户的输入	stty echo
SU	::
切换到root用户	su
切换到root用户并使用其环境	su -
切换到另一用户	su <username>
TAIL	::
显示某文件中的文件尾中包含pattern的文件行	tail -f <file> | grep <pattern>
TAR	::
把整个目录打包（没有压缩）	tar cvf <outfile>.tar <dir>
解包某个tar文件	tar xvf <file>.tar
先解压缩再解包	gzip -dc <file>.tar.gz | tar xvf -
打包成一个压缩包	tar xzvf <file>tar.gz
在.cshrc中设置 tar命令的tape 变量	tape=/dev/rmt/0mbn
把一个目录打包到tape变量所指的目录中	tar cv <dir>
从tape中解包	tar xv
从tape中解出一个文件	tar xv <file>
从 tape中得到一个内容表	tar t
以合适的权限和链接拷贝一个目录	(cd fromdir && tar -cBf – . ) | ( cd todir && tar -xBf – )
TCSH	::
Berkly的另一个非常不错的shell
TEE	::
把标准输入重定向到标准输出	who | tee -a > <file>
TEST	::
检查是否是一个文件	test -a <file>
检查是否某文件是否是root属性	test -O /usr/bin/su
检查某变量是否为 null	test -n “$foo”
以数字的方式比较两个数字字符串	test $var1 -gt $var2
在ksh 脚本中间接地使用”test”	if [[ -a <file> ]];then …;fi
TIME	::
查看运行一个命令需要多少时间	time <command>
TOUCH	::
更新文件的修改时间为当前时间，文件不存在则创建文件	touch <file>
TR	::
使用x替换a，y替换b，c替换z	tr ‘[a-c]‘ ‘[x-z]‘ < infile > outfile
TRAP	::
捕捉”^C” 并执行子程序	trap “mysub;exit” 0 1 2 15
TRUE	::
让个不存在的命令返回0	ln -s /usr/bin/true ranlib
TRUSS	::
查看一个命令运行时的系统调用	truss <command> > /dev/null
TYPSET	::
查看被激活的功能	typset
TTY	::
查看终端所在的设备文件	tty
ULIMIT	::
查看系统所支持的最大文件长度	ulimit
UMASK	::
查看目前的umask	umask
设置一个umask	umask 077
UNIQ	::
查看一个文件中有多少行是一样的	sort <file> | uniq -c
仅输出唯一的没有重复的行	sort <file> | uniq -u
UPTIME	::
查看你的电脑开机多少时间了	uptime
UUENCODE	::
Encode一个文件以便发送电子邮件	uuencode decodedname namenow > codedname
UUDECODE	::
Decode 一个 uuencoded 文件	uudecode <file>
WAIT	::
等一个后进和运行结束	wait $jobid
VI	::
最主要的unix编译器	vi <file>
WC	::
计算一个文件的行号	wc -l <file>
XARGS	::
把标准输出作为参数来执行一条命令	<command> | xargs -i grep ‘pattern’ {}
XON	::
从另一台电脑上得到一个xterm	xon <host>
从另一台电脑上得到所有的东西	xon <host> <X-client>

history | awk {'print $2'} | sort | uniq -c | sort -k1 -rn | head

export ANDROID_HOME=/home/ask/tools/adt-bundle-linux-x86-20130522/sdk

# for mac
alias tree='find . -type d | ls -lARG'
