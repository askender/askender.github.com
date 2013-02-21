git diff "@{yesterday}"

或者一个特定版本与倒数第二个变更之间：
$ git diff 1b6d "master~2"

输出结果都是补丁格式，可以用 git apply 来把补丁打上。也可以试一下：
$ git whatchanged --since="2 weeks ago"

git config --global --get-regexp alias
git diff origin/HEADa