# Most Important Git Commands

# --Git clone--
# Syntax for git clone is 

# git clone <url of the repository>

# Git clone is for copying the codes from remoter
# repository to our local. 

# --Git branch--
# Syntax for git branch is 

# git branch <branch name>

# This command will create a new branch in the remote 
# repository. 

# How can I view all of the branches? 

# git branch --list

# How can i delete the branch ? 

# git branch -d <branch name>


# -- Git checkout

# When we use git checkout command we can jump from 
# one branch to another.

# git checkout <name of the branch> 

# Changes in your current branch must be committed or 
# stashed before you switch. 


# How can I learn information for my branch? 

# using 

# git status 

# command we can gather information about our branch. 



# Git add

# We use it to add files in next commit. 
# Let's say you make changes and you want to commit 
# those changes. 
# First you need to add those files so you can commit. 

# -Add a single file.
# git add <file>

# -Everything at once
# git add -A


# Git commit 

# It makes changes ready to be pushed.
# Everytime we commit files we have to provide 
# a message. 

# git commit -m "Your commit message."


# Git push

# It will take all the committed codes and 
# store it in the remote repository.

# git push <branchName>