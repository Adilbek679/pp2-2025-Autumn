# git config --global user.name "Adilbek679"
# git config --global user.email "a_pirnazarov@kbtu.kz"  
# git config --global init.defaultBranch main
# git config --global core.autocrlf input
# git config --global core.safecrlf warn
# mkdir work
# cd work
# touch hello.html
# git init 
# Инициализирован пустой репозиторий Git в /Users/adilbekpirnazarov/work/.git/
# git add hello.html
# git commit -m "Initial Commit"
# [main (корневой коммит) f6c96cc] Initial Commit
#  1 file changed, 0 insertions(+), 0 deletions(-)
# create mode 100644 hello.html

# $ git status
# On branch main
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
# 	modified:   hello.html

# no changes added to commit (use "git add" and/or "git commit -a")

# git add hello.html
# git status

# $ git add hello.html
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 	modified:   hello.html

# git commit
# |
# # Please enter the commit message for your changes. Lines starting
# # with '#' will be ignored, and an empty message aborts the commit.
# #
# # On branch main
# # Changes to be committed:
# #       modified:   hello.html
# #

# $ git commit
# [main 78433de] Added h1 tag
#  1 file changed, 1 insertion(+), 1 deletion(-)

# $ git status
# On branch main
# nothing to commit, working tree clean

# git add hello.html

# git status
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 	modified:   hello.html

# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
# 	modified:   hello.html

# git commit -m "Added standard HTML page tags"
# git status

# $ git commit -m "Added standard HTML page tags"
# [main 46afaff] Added standard HTML page tags
#  1 file changed, 5 insertions(+), 1 deletion(-)
# $ git status
# On branch main
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
# 	modified:   hello.html

# no changes added to commit (use "git add" and/or "git commit -a")

# $ git add .
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 	modified:   hello.html


# $ git commit -m "Added HTML header"
# [main b7614c1] Added HTML header
#  1 file changed, 2 insertions(+)

# git logv
# $ git log
# commit c42cd0130a8d9d3b3d59ef57f2fdfc3df4a6afa9 (HEAD -> main)
# Author: Adilbek679 <a_pirnazarov@kbtu.kz>
# Date:   Thu Sep 18 21:54:03 2025 +0500

#     Added HTML header

# commit c42cd0130a8d9d3b3d59ef57f2fdfc3df4a6afa9 (HEAD -> main)
# Author: Adilbek679 <a_pirnazarov@kbtu.kz>
# Date:   Thu Sep 18 21:54:03 2025 +0500

#     Added standard HTML page tags

# commit c42cd0130a8d9d3b3d59ef57f2fdfc3df4a6afa9 (HEAD -> main)
# Author: Adilbek679 <a_pirnazarov@kbtu.kz>
# Date:   Thu Sep 18 21:54:03 2025 +0500

#     Added h1 tag

# commit c42cd0130a8d9d3b3d59ef57f2fdfc3df4a6afa9 (HEAD -> main)
# Author: Adilbek679 <a_pirnazarov@kbtu.kz>
# Date:   Thu Sep 18 21:54:03 2025 +0500

#     Initial commit

# git log --pretty=oneline
# c42cd0130a8d9d3b3d59ef57f2fdfc3df4a6afa9 (HEAD -> main) Initial Commit

# git log --oneline --max-count=2
# git log --oneline --since="5 minutes ago"
# git log --oneline --until="5 minutes ago"
# git log --oneline --author="Your Name"
# git log --oneline --all

# c42cd01 (HEAD -> main) Initial Commit
# c42cd01 (HEAD -> main) Initial Commit
# c42cd01 (HEAD -> main) Initial Commit

# git log --pretty=format:"%h %ad | %s%d [%an]" --date=short
# c42cd01 2025-09-18 | Initial Commit (HEAD -> main) [Adilbek679]

# git config --global format.pretty '%h %ad | %s%d [%an]'
# git config --global log.date short

# git log
# c42cd01 2025-09-18 | Initial Commit (HEAD -> main) [Adilbek679]

# git checkout <hash>
# cat hello.html
# $ git checkout 5836970
# Note: switching to '5836970'.

# You are in 'detached HEAD' state. You can look around, make experimental
# changes and commit them, and you can discard any commits you make in this
# state without impacting any branches by switching back to a branch.

# If you want to create a new branch to retain commits you create, you may
# do so (now or later) by using -c with the switch command. Example:

#   git switch -c <new-branch-name>

# Or undo this operation with:

#   git switch -

# Turn off this advice by setting config variable advice.detachedHead to false

# HEAD is now at 5836970 Initial commit
# $ cat hello.html
# Hello, World!

# git switch main
# cat hello.html

# $ git switch main
# Previous HEAD position was 5836970 Initial commit
# Switched to branch 'main'
# $ cat hello.html
# <html>
#   <head>
#   </head>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>

# git tag v1
# git log

# c42cd01 2025-09-18 | Initial Commit (HEAD -> main, tag: v1) [Adilbek679]

# git checkout v1^
# cat hello.html

# $ git checkout v1^
# Note: switching to 'v1^'.

# You are in 'detached HEAD' state. You can look around, make experimental
# changes and commit them, and you can discard any commits you make in this
# state without impacting any branches by switching back to a branch.

# If you want to create a new branch to retain commits you create, you may
# do so (now or later) by using -c with the switch command. Example:

#   git switch -c <new-branch-name>

# Or undo this operation with:

#   git switch -

# Turn off this advice by setting config variable advice.detachedHead to false

# HEAD is now at 46afaff Added standard HTML page tags
# $ cat hello.html
# <html>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>

# git tag v1-beta
# git log

# c42cd01 2025-09-18 | Initial Commit (HEAD -> main, tag: v1-beta, tag: v1) [Adilbek679]

# git checkout v1
# git checkout v1-beta
# HEAD сейчас на c42cd01 Initial Commit
# HEAD сейчас на c42cd01 Initial Commit

# git switch main
# Переключились на ветку «main»

# git status
# $ git status
# On branch main
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git restore <file>..." to discard changes in working directory)
# 	modified:   hello.html

# no changes added to commit (use "git add" and/or "git commit -a")

# git restore hello.html
# git status
# cat hello.html

# $ git restore hello.html
# $ git status
# On branch main
# nothing to commit, working tree clean
# $ cat hello.html
# <html>
#   <head>
#   </head>
#   <body>
#     <h1>Hello, World!</h1>
#   </body>
# </html>

# git add hello.html
# $ git status
# On branch main
# Changes to be committed:
#   (use "git restore --staged <file>..." to unstage)
# 	modified:   hello.html

# git restore --staged hello.html
# git restore hello.html
# git status

# $ git restore hello.html
# $ git status
# On branch main
# nothing to commit, working tree clean
