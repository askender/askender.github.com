git config --global user.name "Your Name Comes Here"
git config --global user.email you@yourdomain.example.com
git config --list
git init
如果作为 Server 存在，那么可以忽略工作目录，以纯代码仓库形式存在
git --bare init
可以在~/.gitconfig设置别名
[alias]
st = status
ci = commit -a
co = checkout

git add . 
git add file1 file2 file3
git add -u
git add -p // 为你做的每次修改，Git将为你展示变动的代码，并询问该变动是否应是下一次提交的一部分。回答“y”或者“n”。也有其他选项，比如延迟决定：键入“？”来学习更多。 
git rm file1 file2 file3 
git mv file1 file2 

git commit -a -m ' '
git commit --amend -a -m ' ' // 修改上一次的信息，不作为新的提交
git stash // 保存当前草稿，便于切换分支
git stash pop
git stash apply
git stash list
git stash apply stash@{1}
git stash clear

git reset HEAD file1 // 取消暂存区的文件快照(即恢复成最后一个提交版本)，这不会影响工作目录的文件修改。
git reset --hard HEAD^ // 将整个项目回溯到以前的某个版本，可以使用 "git reset"。可以选择的参数包括默认的 "--mixed" 和 "--hard"，前者不会取消工作目录的修改，而后者则放弃全部的修改。该操作会丢失其后的日志
git checkout -- file1 // 使用暂存区快照恢复工作目录文件，工作目录的文件修改被抛弃。
git checkout HEAD^ file1 // 直接 "签出" 代码仓库中的某个文件版本到工作目录，该操作同时会取消暂存区快照。
git checkout "@{10 minutes ago}" //直接"签出"10分钟之前代码仓库中的某个文件版本到工作目录，该操作同时会取消暂存区快照。
git checkout "@{5}" // 直接 "签出" 倒数第五次保存的某个文件版本到工作目录，该操作同时会取消暂存区快照。
git revert SHA1_HASH // 还原特定哈希值对应的提交。该还原记录作为一个新的提交。

git log 
git log -p 
git log --stat --summary 
git log V3..V7 //显示V3之后直至V7的所有历史记录 
git log V3.. //显示所有V3之后的历史记录。注意<since>..<until>中任何一个被省略都将被默认设置为HEAD。所以如果使用..<until>的话，git log在大部分情况下会输出空的。 
git log –since=”2 weeks ago” //显示2周前到现在的所有历史记录。具体语法可查询git-ref-parse命令的帮助文件。 
git log stable..experimental //将显示在experimental分支但不在stable分支的历史记录 
git log experimental..stable //将显示在stable分支但不在experimental分支的历史记录 
git log -S'你要找的内容'，就可以从全部的历史纪录，瞬間找到你要找的东西 
git blame FILE // 标注出一个指定的文件里每一行内容的最后修改者，和最后修改时间。 
git diff // 这个命令只在git add之前使用有效。如果已经add了，那么此命令输出为空 
git diff –cached // 这个命令在git add之后在git commit之前有效。 
git diff "@{yesterday}" // 比较当前和昨天的内容 
git status // 这个命令在git commit之前有效，表示都有哪些文件发生了改动 
git show 5b888 // 使用git show再加上述的commit名称来显式更详细的commit信息 
git show master // 显示分支信息 
git show HEAD // 使用HEAD字段可以代表当前分支的头（也就是最近一次commit) 
git show HEAD^ //查看HEAD的父母的信息, 可以使用^表示parent 
git show HEAD^^ //查看HEAD的父母的父母的信息 
git show HEAD~4 //查看HEAD上溯4代的信息 
git tag V3 5b888 //以后可以用V3来代替复杂的名称(5b888…) 
git show V3 
git branch stable V3 //建立一个基于V3的分支 
git grep “print” V3 //在V3中搜索所有的包含print的行 
git grep “print” //在所有的历史记录中搜索包含print的行 

git clone git://server/path/to/files // Git deamon 
git clone your.computer:/path/to/script
git pull 
git push // 在将代码提交(push)到服务器之前，首先要确认相关更新已经合并(merge)到主分支(master)。还应该先从服务器刷新(pull)最新代码，以确保自己的提交不会和别人最新提交的代码冲突。 
如果想在merge前先查看更改： 
git fetch /home/bob/myrepo master:bobworks //此命令意思是提取出bob修改的代码内容，然后放到我（rocrocket）工作目录下的bobworks分支中。之所以要放到分支中，而不是master中，就是要我先仔仔细细看看bob的开发成果，如果我觉得满意，我再merge到master中，如果不满意，我完全可以直接git branch -D掉。 

git whatchanged -p master..bobworks //用来查看bob都做了什么 
git checkout master //切换到master分区 
git pull . bobworks //如果我检查了bob的工作后很满意，就可以用pull来将bobworks分支合并到我的项目中了 

git branch: 查看当前分支 
git checkout -b/branch experimental： 创建新分支 
git checkout experimental： 切换到另一分支 
git merge experimental：合并分支 
git branch -d experimental：删除分支, 使用的是小写的-d，表示“在分支已经合并到主干后删除分支”。 
git branch -D experimental：删除分支, 表示“不论如何都删除分支”，-D使用在“分支被证明失败” 

git format-patch：当你想给一个开源项目（例如Rails）提交一段代码的时候，或者你想给小组成员展示一段你并不想提交的代码，那么你还是需要 patch的，Git的'format-patch'命令良好的支持了这个功能。 
第一，利用branch命令 创建一个分支； 
第二，修改你的代码； 
第三，在该分支上提交你的修改； 
第四，使用'git format-patch'命令来生成一个patch文件，例如：'git format-patch master --stdout > ~/Desktop/tmp.patch'就是将工作分支与master主干的不同，存放在'~/Desktop'文件夹下，生成一个叫做 tmp.patch的文件（另一种简单的版本是利用diff命令，例如'git diff ..master > ~/Desktop/tmp.patch'），这样就生成了patch文件。那么别人就可以使用'git apply'命令来应用patch，例如'git apply ~/Desktop/tmp.patch'就是将patch打在当前的工作分支上 

git fsck: 不加–full参数的情况下，这个命令一般会以非常低廉的代价确保仓库在一个不错的健康状态之中。 
git count-objects: 统计有多少松散的对象，没有 repack 的对象消耗了多少硬盘空间。 
git gc: 在本地仓库进行 repack，并进行其他日常维护工作。 
git filter-branch --tree-filter `rm top/secret/file` HEAD //在所有记录中永久删除某个文件 
git rebase -i HEAD~10 // 后10个提交会出现在你喜爱的$EDITOR。通过删除行来移去提交。通过为行重新排序来为提交重新排序。用“edit”来替换“pick”来标志一个提交可修改。用“squash”来替换“pick”来将一个提交和前一个合并。 

刚刚发现程序里有一个功能出错了，即使你过去经常提交变更，Git还是可以精确的找出问题所在： 
git bisect start 
git bisect bad SHA1_OF_BAD_VERSION 
git bisect good SHA1_OF_GOOD_VERSION 
Git从历史记录中检出一个中间的状态，在这个状态上测试功能，如果还是错误的： 
git bisect bad 
如果可以工作了，则把"bad"替换成"good"。 Git会再次帮你找到一个以确定的好版本和坏版本之间的状态，经过一系列的迭代，这种二进制查询会帮你找到导致这个错误的那次提交。一旦完成了问题定位的调查，你可以返回到原始状态，键入： 
git bisect reset 
不需要手工测试每一次改动，执行如下命令可以自动的完成上面的搜索： 
git bisect run COMMAND 
Git使用指定命令（通常是一个一次性的脚本）的返回值来决定一次改动是否是正确的：命令退出时的代码0代表改动是正确的，125代表要跳过对这次改动的检查，1到127之间的其他数值代表改动是错误的。返回负数将会中断整个bisect的检查。

将 Current working directory 记为 工作目录(1) 
将 Index file 记为 暂存区(2) 
将 Git repository 记为 代码仓库(3) 
他们之间的提交层次关系是 (1) -> (2) -> (3) 
git add完成的是(1) -> (2) 
git commit完成的是(2) -> (3) 
git commit -a两者的直接结合 
从时间上看，可以认为(1)是最新的代码，(2)比较旧，(3)更旧 
按时间排序就是 (1) < (2) < (3) 

git diff得到的是从(2)到(1)的变化 
git diff –cached得到的是从(3)到(2)的变化 
git diff HEAD得到的是从(3)到(1)的变化


## check
git whatchanged
git whatchanged --since="2 weeks ago"
git log --stat
git show

## tag
git tag -a v0.0.8 -m 'version 0.0.8'
git tag -a v0.1.2 -m "发布0.1.2版本"
通常的git push不会将标签对象提交到git服务器，我们需要进行显式的操作：
git push origin v0.1.2 # 将v0.1.2标签提交到git服务器
git push origin --tags # 将本地所有标签一次性提交到git服务器

## diff
git diff "@{yesterday}"
或者一个特定版本与倒数第二个变更之间：
git diff 1b6d "master~2"
输出结果都是补丁格式，可以用 git apply 来把补丁打上


提交user.name错误,修正了，记录一下：
git rebase -i master~2
    change that pick to edit
git commit --amend --reset-author  (-C HEAD)
git rebase --continue

git config --global user.name askender
git config --global user.email askender43@gmail.com


## 新建develop分支
Git除了分布式这一大特性外，还大大强化了分支的使用。我们日常的开发工作一般不在master分支上进行，而是最好建立一个develop分支:

git checkout -b develop
开发时，最好基于develop分支再新建一个特性分支，比如我们要为网站添加一个新功能“标签支持”，就为其新建一个分支tag_support，新功能开发完成之后，将其合并到develop分支上:

git checkout develop
git merge tag_support
这就将新功能的代码合并到了开发主分支上，合并过程没有冲突的话，就可以删掉这个分支：

git branch -d tag_support


## Git配置
git config --global user.name "robbin"   
git config --global user.email "fankai@gmail.com"
git config --global color.ui true
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.br branch
git config --global core.editor "mate -w"    # 设置Editor使用textmate
git config -l  # 列举所有配置
用户的git配置文件~/.gitconfig

git help <command>  # 显示command的help
git show            # 显示某次提交的内容
git show $id

git co  -- <file>   # 抛弃工作区修改
git co  .           # 抛弃工作区修改

git add <file>      # 将工作文件修改提交到本地暂存区
git add .           # 将所有修改过的工作文件提交暂存区

git rm <file>       # 从版本库中删除文件
git rm <file> --cached  # 从版本库中删除文件，但不删除文件

git reset <file>    # 从暂存区恢复到工作文件
git reset -- .      # 从暂存区恢复到工作文件
git reset --hard    # 恢复最近一次提交过的状态，即放弃上次提交后的所有本次修改

git ci <file>
git ci .
git ci -a           # 将git add, git rm和git ci等操作都合并在一起做
git ci -am "some comments"
git ci --amend      # 修改最后一次提交记录

git revert <$id>    # 恢复某次提交的状态，恢复动作本身也创建了一次提交对象
git revert HEAD     # 恢复最后一次提交的状态
查看文件diff

git diff <file>     # 比较当前文件和暂存区文件差异
git diff
git diff <$id1> <$id2>   # 比较两次提交之间的差异
git diff <branch1>..<branch2> # 在两个分支之间比较 
git diff --staged   # 比较暂存区和版本库差异
git diff --cached   # 比较暂存区和版本库差异
git diff --stat     # 仅仅比较统计信息
查看提交记录

git log
git log <file>      # 查看该文件每次提交记录
git log -p <file>   # 查看每次详细修改内容的diff
git log -p -2       # 查看最近两次详细修改内容的diff
git log --stat      # 查看提交统计信息
tig

Mac上可以使用tig代替diff和log，brew install tig

git br -r           # 查看远程分支
git br <new_branch> # 创建新的分支
git br -v           # 查看各个分支最后提交信息
git br --merged     # 查看已经被合并到当前分支的分支
git br --no-merged  # 查看尚未被合并到当前分支的分支

git co <branch>     # 切换到某个分支
git co -b <new_branch> # 创建新的分支，并且切换过去
git co -b <new_branch> <branch>  # 基于branch创建新的new_branch

git co $id          # 把某次历史提交记录checkout出来，但无分支信息，切换到其他分支会自动删除
git co $id -b <new_branch>  # 把某次历史提交记录checkout出来，创建成一个分支

git br -d <branch>  # 删除某个分支
git br -D <branch>  # 强制删除某个分支 (未被合并的分支被删除的时候需要强制)
分支合并和rebase

git merge <branch>               # 将branch分支合并到当前分支
git merge origin/master --no-ff  # 不要Fast-Foward合并，这样可以生成merge提交

git rebase master <branch>       # 将master rebase到branch，相当于：
git co <branch> && git rebase master && git co master && git merge <branch>
Git补丁管理(方便在多台机器上开发同步时用)

git diff > ../sync.patch         # 生成补丁
git apply ../sync.patch          # 打补丁
git apply --check ../sync.patch  # 测试补丁能否成功

git stash                        # 暂存
git stash list                   # 列所有stash
git stash apply                  # 恢复暂存的内容
git stash drop                   # 删除暂存区

git pull                         # 抓取远程仓库所有分支更新并合并到本地
git pull --no-ff                 # 抓取远程仓库所有分支更新并合并到本地，不要快进合并
git fetch origin                 # 抓取远程仓库更新
git merge origin/master          # 将远程主分支合并到本地当前分支
git co --track origin/branch     # 跟踪某个远程分支创建相应的本地分支
git co -b <local_branch> origin/<remote_branch>  # 基于远程分支创建本地分支，功能同上

git push                         # push所有分支
git push origin master           # 将本地主分支推到远程主分支
git push -u origin master        # 将本地主分支推到远程(如无远程主分支则创建，用于初始化远程仓库)
git push origin <local_branch>   # 创建远程分支， origin是远程仓库名
git push origin <local_branch>:<remote_branch>  # 创建远程分支
git push origin :<remote_branch>  #先删除本地分支(git br -d <branch>)，然后再push删除远程分支
Git远程仓库管理

git remote -v                    # 查看远程服务器地址和仓库名称
git remote show origin           # 查看远程服务器仓库状态
git remote add origin git@github:robbin/robbin_site.git         # 添加远程仓库地址
git remote set-url origin git@github.com:robbin/robbin_site.git # 设置远程仓库地址(用于修改远程仓库地址)
git remote rm <repository>       # 删除远程仓库

创建远程仓库
git clone --bare robbin_site robbin_site.git  # 用带版本的项目创建纯版本仓库
scp -r my_project.git git@git.csdn.net:~      # 将纯仓库上传到服务器上

mkdir robbin_site.git && cd robbin_site.git && git --bare init # 在服务器创建纯仓库
git remote add origin git@github.com:robbin/robbin_site.git    # 设置远程仓库地址
git push -u origin master                                      # 客户端首次提交
git push -u origin develop  # 首次将本地develop分支提交到远程develop分支，并且track

git remote set-head origin master   # 设置远程仓库的HEAD指向master分支
也可以命令设置跟踪远程库和本地库

git branch --set-upstream master origin/master
git branch --set-upstream develop origin/develop

git reset HEAD^
git reset --hard origin/master
git reset --soft HEAD^
解释一下，HEAD是当前分支的最新版本。^表示父节点。当前节点的父节点，就是上一次提交的版本。

git log --pretty=oneline

https://sites.google.com/a/kingofat.com/wiki/git-tutorial
