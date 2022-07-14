from os import stat_result


#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
#**************************************************************************************************************
#WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

#****************************************************************
#****************************************************************

# ====== Commit changes ======
$ git status
$ git add *
$ git commit -m “MESSAGE”
$ git push origin BRANCHNAME

# ====== Create new branch ======
$ git branch BRANCHNAME
# This just created locally
# After commit a new change, new branch will created remotelly and display on bitbucket.
# Change to master:
$ git checkout master
# Remove cache file
$ git rm filename –cached

# ====== Delete branch ======
$ git branch -d BRANCHNAME
# This only can delete branch locally. And only if it has already been pushed and merged with remote branch.
$ git branch -D BRANCHNAME
# This force the branch be deleted
$ git  push  orgin --delete BRANCHNAME
# Then delete it remotely

# ====== merge ======
$ git pull <远程主机名> <远程分支名>:<本地分支名>
$ git pull
$ git pull origin
$ git pull origin master:JXT-1807-
$ git pull origin master  # 如果远程分支是当前分支，则冒号后面的部分可以省略

$ git status
$ git add FILEPATH
$ git commit -m "MESSAGE"
$ git push origin BRANCHNAME


# ====== forgot create .iginore =====
$ git rm -r --cached .  # 清除项目中所有文件的本地缓存
$ git add . 
$ git commit -m "MESSAGE"
$ git push -f  # 强制推送
$ git add -f FILEPATH  # 强制添加已忽略的文件

# ====== create a new branch and check it out at the same time ======
$ git checkout -b BRANCHNAME

# ====== merge ======
$ git checkout BRANCHNAME
$ git merge master
# git 还可以merge commit
$ git checkout COMMITNUMBER

# ====== rebase ======
$ git branch BRANCHNAME # create new branch
$ git checkout BRANCHNAME
$ git commit -m "MESSAGE"
$ git checkout master
$ git commit -m "MESSAGE"
$ git checkout BRANCHNAME 
$ git rebase master # 重定

# ====== ^ ～ ======
# 操作符^， 回到上一层
# 操作符～<数字>
$ git branch -f master HEAD~3 # f means force , move master 3 behind HEAD
$ git checkout master^ # head 回到上一层


# ====== reset ======
# moving around
$ git reset HEAD~1 # 

# ====== reverse ======
# moving around
$ git revert HEAD


# ====== cherry-pick ======
# rebase 重定
# merge commits to master
# cherry-pick is great when you know which commits you want
$ git cherry-pick COMMITNUMBER_1 COMMITNUMBER_2 # copy commit_1 和 commit_2 到当前分支

# ====== rebase ======
# 重定向，可以手动排序, re-order, 以及隐藏一些commit
$ git rebase -i HEAD~4

# ====== delete branch ======
# 删除分支
$ git branch -d BRANCHNAME

# ====== tag ======
$ git tag v1 c1 

# massage = db.Table('massage', 
#     db.Column('recording_id', db.String, db.ForeignKey('recording.id')),
#     db.Column('release_variant_id', db.String, db.ForeignKey('releasevariant.id')),
#     info={'bind_key': 'fender'}
# )
