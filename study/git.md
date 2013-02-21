git diff "@{yesterday}"

或者一个特定版本与倒数第二个变更之间：
$ git diff 1b6d "master~2"

输出结果都是补丁格式，可以用 git apply 来把补丁打上。也可以试一下：
$ git whatchanged --since="2 weeks ago"

git config --global --get-regexp alias
git diff origin/HEADa

提交user.name错误,修正了，真是折腾，记录一下：
git rebase -i master~2
    change that pick to edit
git commit --amend --reset-author  (-C HEAD)
git rebase --continue

git config --global user.name askender
git config --global user.email askender43@gmail.com
