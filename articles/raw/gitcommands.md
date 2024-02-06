# GIT Useful commands

---
You may add these to your .aliases

```
git add                     # ** Add New files ** 
git checkout <githubURL>    # Clone a repo
git pull					# Get changes made by others
git status                  # See local changes

git commit                  # locally save the change
git push                    # push our changes to server

# ==> Cache password
#
git config credential.helper "cache --timeout=300000"

# BRANCH
git branch                  # show branches
git fetch --all             # git fetch all brabches
git branch -r               # Show all the branches‣
```

---
### Git merge

To merge changes from say  **master** branch to branch **br1**:
1. check out the destination branch
	```git checkout br1``` # check out the destination branch

2. ```git merge master```  # merge from source 


##### Git merge specific files from master to branch

1. 


##### Git merge specific files from branch to master
    
1. 


---
<br>
## References
1. GIT Merge
https://jasonrudolph.com/blog/2009/02/25/git-tip-how-to-merge-specific-files-from-another-branch/
---
<br/>
### My git alias 
<br/> 
```
alias gita='git add'
alias gitb='git branch'
alias gitc='git commit -a -m "Commiting "'
alias gitca='git config credential.helper "cache --timeout=300000"'
alias gitco='git checkout'
alias gitcp='gitc; git push'
alias gitp='git pull'
alias gitpa='for i in */.git; do ( echo $i; cd $i/..; git pull; ); done'
alias gitpu='git push'
alias gitreset='git reset --hard origin/master; git pull origin master'
alias gits='git status'
```
