“我是如此得深爱着 Ssh”

ssh 绝对不不仅仅是类似 telnet 这样远程登录管理主机那么简单。下面的些 技巧，或许可以激发起你对这个“老朋友”重新认识的兴趣。
有部分内容来自：http://derwiki.tumblr.com/post/841579929/how-i-learned-to-stop-worrying-and-love-ssh
建立 HTTP 隧道
如果你需要访问线上集群中某台内网主机，那么你可以这样
ssh -f -N -L 31609:192.168.0.1:80 remotehost
当运行完毕以后，打开本地浏览器访问 http://localhost:31609 端口，则可以获取 remotehost 访问 192.168.0.1 的 80 端口的数据。
反向 ssh 隧道
如果本地局域网无法访问某些站点，那么你可以利用你的 ssh 主机通过它去访问。你可以使用
ssh -D 8080 remotehost
然后设置代理为 localhost:8080 则可以通过 remotehost 访问制定的资源。
PS，如果你使用 Mac，并经常会这样干，那么你会喜欢这个工具。
直接运行远程脚本
ssh 其实可以直接指定运行远程主机的命令。例如，每次登录并查看线上的日志是件非常繁琐的累活。其实你可以使用下面的命令
ssh user@remotehost "taif -f /var/log/apache/access.log"
它会 ssh 登录以后直接执行指定的命令。这样我们可以构建本地脚本让其接受远程服务器的输出，做更多的事情。
压缩传送文件和目录
有时候不想开启 SFTP 工具传送文件，那么下面的命令会帮到你
tar cvfz - localFileOrDir | ssh user@remotehost 'cd /remote/path/to/unpack/ ; tar xvfz -'
这个命令可以自动讲本地的文件或者目录打包压缩以后，通过 ssh 传输到 remotehost 主机，然后 remotehost 会自动将其解压缩。
自动登录 ssh
最后个 ssh 技巧，上面的技巧的确是很实用，但是我们也受不了每次都要输入次密码。如果你的确厌烦了这些，那么尝试执行下面的命令：
ssh user@remotehost 'cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub
这样远程的主机就会保存你本地的公钥，你就可以自动 ssh 登录远程主机（详细）。
顺便提醒：强烈提醒您保护好您主目录下的 ssh 公钥，否则您的帐户可能会面临风险。
还有些有用的参数
-C 这个参数可以将文本数据压缩传送
-X 如果远程服务器支持 X11 forwarding ，那么远程的 X 应用直接可以在本地显示运行（当然你本地要有 X Server）
各位还有什么其它好用的 ssh tips，欢迎不吝指出。
– EOF –
转自http://www.gracecode.com/archives/3030/