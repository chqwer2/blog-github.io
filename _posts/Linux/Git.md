### Git Authentication

Clone with CLI

```
conda install gh --channel conda-forge
gh auth login
```

```
git status # How to omit 
```

### Git Status

```
'git status'不显示untracked files
git status -uno
```

### Git Push

```
git push -f   "force local branch commit to cover the remote commit"
```

### How to squash commits into one

```
git log --graph --decorate --pretty=oneline --abbrev-commit    # to print all the commits
# Check how many commits together
```

```
# Picking and Squashing
git rebase -i HEAD~7             # [number of commits]
```



### Branch

```
git branch -r    # remote
git branch -r | grep MOD-22266        # Or
git branch -a | grep MOD-22266

git fetch origin  

从当前分支拉copy开发分支
git checkout -b ibis35-dev
```

detached HEAD status

```
git fetch
git branch my-new-branch
git checkout -b my-new-branch
# Add -b parameter which creates a local branch from the remote
# Or
git switch -c <new branch name>

```



### Exclude

```
git status > log
mv log ./git/info/exclude
```

### Git Checkout & Pull 

```
git pull origin tachyon-RDI-10 --rebase 
git checkout tachyon-RDI-10

git branch remote | grep MOD-22266
```

**you are in 'detached HEAD' state.**

maybe duplicated branch

# don’t add origin, checkout the branch after origin

### Git Stash

```
git stash apply + version
```

### Merge

![image-20221220103924736](C:\Users\calvchen\AppData\Roaming\Typora\typora-user-images\image-20221220103924736.png)

```
git mergetool
```



### Commit

```
git commit --amend   然后
git push -f          就会把上一个commit删掉 添加一个
```

### Find Git History 

```
git log --pretty=oneline --follow filename  --- 显示某个文件的修改历史，加上--follow后即使文件被移动过也可以查看历史
```

