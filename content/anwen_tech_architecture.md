Title: 安问技术架构
Date: 2013-10-17
Tags: tech
Slug: anwen_tech_architecture
Summary:

从前向后说吧。
安问的技术架构目前用在3个正在使用中的项目中
架构也在不断更新中（本文持续更新中）

目前用户能接触到的用户界面有：
web网站（基于twitter bootstrap3）
android app（基于web view简单包装）
接下来打算扩展用户界面的方向：
更多平台的app（使用phonegap封装，目前已经做出demo）
以及跨平台的桌面端（linux mac win8 考虑使用PyQt QT最新版本已经能打包成移动应用）（优先级低）

设计方面，请专业的设计师设计（朋友或者在专业的设计平台上征集）

前端技术方面：
更偏向于使用html5相关技术（html5 css3）
javascript方面，目前主要使用jquery，以后会转向backbone或者angularjs，使用mvc框架和自动构建工具（已经开始使用grunt）
css目前采用less写好后编译
css和js均自动格式化后合并压缩

前后通信方面：
目前主要采用后台渲染html模板。采用ajax
实时通知和聊天部分采用websocket
目前已经提供了restful-api，但没有使用，以后会逐步全部转为前后端完全分离的restful无状态方式

后端：
目前主要采用python，使用fackbook开发的tornado异步高并发框架
最新的tornado已经支持非常简单的异步和协程特性，无需使用greenlet的方式
采用supervisor进行进程管理和监控，unittest进行单元测试
不排除以后访问量大的时候采用golang

数据库方面：
最早使用mysql，转向sqlite，之后主要使用mongodb文档化nosql数据库
目前采用了mongokit（缺点是还没有py3版本，优点是简单无附加），mongoengine（支持py3，用户多，目前仅在一个项目中使用） 以后也可能使用non-blocking的motor

缓存方面：
早期使用的memcache，目前由于访问量不大，暂时没有缓存层，可以随时加上
以后可能会在部分场景使用redis

负载均衡：
目前采用haproxy和nginx

部署：
采用fabric和git hook自动化部署

运维：
目前的服务器端可运行在多个平台（有一个项目就是运行在本地的win7下面），主要还是部署在阿里云的vps上

分布式：
目前有多台vps，分布式的支持很容易做到，但还没做，有需求时会做。目前是开启了多个进程，服务更新时可以做到无间断。

代码风格：
代码保持结构和风格清晰，有简明的文档，
python代码遵循pep8规范
有一定的代码洁癖，定期review和重构

项目管理：
所有项目都使用trello和gmail进行任务调度，进度监控和多方合作

技术趋势：
使用略成熟但cutting eage，处于社区活跃期的开源技术，并向开源社区及时反馈

团队：
目前主要是通过互联网协作，以后会吸引更多人参与开发，并给予更多报酬

注：以上三个项目指：安问，和朋友合作的另外一个创业项目，以及给家里的小店做的进销存和客户积分管理系统（也是bs架构，windows下本地运行）
