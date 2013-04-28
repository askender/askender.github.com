
分屏启动Vim

使用大写的O参数来垂直分屏。vim -On file1 file2 ...
使用小写的o参数来水平分屏。vim -on file1 file2 ...
注释: n是数字，表示分成几个屏。

关闭分屏 

关闭当前窗口。Ctrl+W c
关闭当前窗口，如果只剩最后一个了，则退出Vim。Ctrl+W q
分屏

上下分割当前打开的文件。Ctrl+W s
上下分割，并打开一个新的文件。:sp filename
左右分割当前打开的文件。 Ctrl+W v
左右分割，并打开一个新的文件。:vsp filename
移动光标

Vi中的光标键是h, j, k, l，要在各个屏间切换，只需要先按一下Ctrl+W

把光标移到右边的屏。Ctrl+W l
把光标移到左边的屏中。Ctrl+W h
把光标移到上边的屏中。Ctrl+W k
把光标移到下边的屏中。Ctrl+W j
把光标移到下一个的屏中。.Ctrl+W w
移动分屏

这个功能还是使用了Vim的光标键，只不过都是大写。当然了，如果你的分屏很乱很复杂的话，这个功能可能会出现一些非常奇怪的症状。

向右移动。Ctrl+W L
向左移动 Ctrl+W H
向上移动 Ctrl+W K
向下移动 Ctrl+W J
屏幕尺寸

下面是改变尺寸的一些操作，主要是高度，对于宽度你可以使用Ctrl+W <或是>，但这可能需要最新的版本才支持。

让所有的屏都有一样的高度。Ctrl+W =
增加高度。Ctrl+W +
减少高度。Ctrl+W -
也许还有其它我不知道的，欢迎你补充。


jedi-vim (github.com)
Vim user? Python user? If so this is probably right up your alley! Pretty awesome Python autocompletion support using the Jedi library as well as Pydoc support.
这是一个为用Vim的PyCoder的一个自动完成插件，另外它支持Jedi library和Pydoc support.

python-mode(github.com)
This is one of Mike’s favorite things. Python-Mode for vim, it supports PyLint, Rope and Pydoc, as well as custom Python movement commands and a bunch of useful python addons. If you use Vim and Python together, this should be in your list of Vim plugins.
这是Mike喜欢的东西之一。Vim的Py模式，它支持PyLint, Rope and Pydoc,还有自定义Py命令和很多Py的插件，如果你一起用vim和py,它应该在你的Vim插件列表里

Getting Started
入门
check.io (checkio.org)
This is really neat! Check iO is a game where the basic concept is that to progress in the game you have to complete programming challenges in Python.、
这真是太好了。Check iO 是一个游戏，它的基本概念是你在游戏中你不得不完成在Py中的编程挑战。

The Hitchhiker’s Guide to Python!(docs.python-guide.org)
This opinionated guide exists to provide both novice and expert Python developers a best-practice handbook to the installation, configuration, and usage of Python on a daily basis.
This opinionated guide是一个每天更新的同时对于Py新手和专家是一本最佳实践手册的安装，配置和使用手册。

Blogging
博客平台

syte (github.com)
Awesome powerful blogging platform that has social integrations like Twitter, GitHub, Dribbble, Instagram, Foursquare, Tumblr, Last.fm, SoundCloud and Bitbucket.
非常棒的一个博客平台拥有像Twitter, GitHub, Dribbble, Instagram, Foursquare, Tumblr, Last.fm, SoundCloud and Bitbucket一样的社交聚合

pelican (github.com)
Pelican has emerged as the static site generator of choice for Python developers. It is highly flexible with plenty of themes. Definitely worth checking out if you are moving static with your website or blog.
Pelican对于Py程序员来说可以看成是一个静态站点生成器，它有很高的灵活性因为有很多主题。如果你让你的网站或者博客静态化的话这绝对值得一看。

cuisine(github.com)
Ever wish that you had Chef like functionality with fabric? Have you attempted to get the similar experience with your own fab scripts? Look no further, Cuisine is a small set of functions that sit on top of Fabric. Definitely worth a look.
你曾想过你有一个像Fabric一样功能的大师吗。你有过尝试用你自己的fab脚本得到相同的体验吗，不要再看了。Cuisine是一个具有小功能的Fabric前端。


redis-faina (tumblr.com)
What do you do when you sell your company for a Billion dollars to Facebook? You write a query analysis tool for Redis! No really, that's not fair, the guys at Instagram are doing good work and this is a nice tool for sites that do a lot of volume on their redis server and need to better intelligence on their queries. Check it out.
你在用十亿美刀把你公司卖给脸书的时候做了什么。你写了一个Redis的查询分析工具，这是不公平的
这些家伙在Instagram的工作做得不错，这是一个很好的工具为那写Redis服务器上的大流量的网站并且需要更加智能的在流量请求上。看一看吧。


redis live (github.com)
This is really awesome. If you manage any Redisservers this looks like it could be a must have. RedisLive is a beautiful monitoring tool for your Redis instances built on top of Tornado and Backbone.js.
这也非常棒，如果你用任何的Redis服务器那么这一款工具就显得必要了。RedisLive对于你的Redis来说是一个漂亮的监控工具，它建立在Tornado and Backbone.js.的前端。


flower (github.com）
Keeping in theme with the vegetation, flower is a web based celery monitoring and administration tool. Quite awesome if you are wrangling celery workers.


salt(github.com)
Saltstack is a central system and configuration manager written in Python.
Saltstack是用Py写的一个中央系统和配置管理

sentry (github.com)
Sentry is a real time event logging and aggregation platform. Integrates everywhere as well as provides trends for occurring exceptions in the system.
Sentry是一个实时的事件日志和聚合平台。融合在每个地方以及提供在系统中发生的异常的趋势，

Asynchronous Queues
异步请求

celery(github.com)
The original Python Distributed Task Queue
原始的PY分布式任务队列

rq (github.com)
Like celery, but hate the overhead? RQ (Redis Queue) is a simple Python library for queueing jobs and processing them in the background with workers. It is backed by Redis and it is designed to have a low barrier to entry.
像celery一样，但是讨厌花销么。RQ是一个简单的PY库用来排队工作，并且在后台与工人处理他们，它是基于Redis写的并且它被设计成一个门槛低的程序。


other
其他类

heatmap (github.com)
Python script for generating high quality heat maps based on any coordinate data GPS tracks, eye tracking data. Pretty cool if you want to map some data that can be mapped to a XY coordinate plane.
这是一个PY脚本用来生成基于任何卫星轨道坐标数据,肉眼跟踪数据来生成高质量的热效应图，如果你想标记一些数据化。他们可以被称现在XY平面坐标轴内。这是很酷的一件事。

selfspy(github.com)
Selfspy is a daemon for Unix/X11 that continuously monitors and stores what you are doing on your computer. It is inspired by the QuantifiedSelf movement.It can tell you what you were working on a couple of days go, what your password for a website, it stores everything you type and does it securely for self inspection later. SO awesome.
Selfspy是一个后台程序在Unix/X11下的用来不间断监控和储存你在电脑中做了些什么事情，它的灵感来自于Quantified Self移动，它能告诉你在前一天你都干了些什么，你在一个网站上留下的密码。它能储存你打下来的打下来的任何东西.

autopep8(github.com)
This thing is awesome, something every python developer should check out. It takes your broken non-pep8 validating code and returns you formatted version that passes pep8 fully formatted.
这个东西真是太好了。是每个Py程序员都应该有的。它能让破损的不能经过pep8的检查的代码变成能让pep8顺利通过。


xkcd password generator(github.com)
xkcd is funny. its even more fun with developers with a little time and tendency to take things a little seriously bring you things as awesome as this.
xkcd很有趣，这比一些开发者用一点时间或者让事情变得有认真的趋势更加有趣，让事情和这一样棒吧。

