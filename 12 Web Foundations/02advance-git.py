# # show differences before stage:
# git diff
# # @@ -1, +3,5 @@
# → file a(-),old: witch line changed in main file, count of showing lines,
#   file b(+),new: witch line changed in main file, count of showing lines
#
# # show staged difference:
# git diff --stagged
#
# # all of difference
# git diff HEAD
# git diff HEAD <file name>
#
# # diff of several branch heads:
# git diff main nahal  # < > < >
#
# # summery of commits:
# git log --online
# git diff <hash> <hash>
#
# # switch between branches with no commit
# git stash
# git stash pop
# git stash clear
#
# # return to old commits:
# git checkout <hash>
# git log
# git status
# git branch bugfix
# git switch main
#
# # ignore unstaged changes:
# git restore <filename>
# # unstage changed file:
# git restore --staged <filename>
#
# # delete commits from history but keep changes:
# git reset <hash>
#
# # delete unwanted changes of an old commit with keeping commit history
# # (just add a revert commit before that commit)
# git revert <hash>
#
# # history in one clean line (*just u can use it before push*)
# git rebase --continue
#
# # merge some commits for cleaner commit history (i:interactive) (*just u can use it before push*)
#
# # pick, reword(change message of commit), edit, squash, fixup
# git rebase -i HEAD~3
# reword <hash> <message> <filename>
# fixup <hash> <message> <filename>
# fixup <hash> <message> <filename>
#
# # shortcuts in global:
# git config --global --edit
# [alias]
#     st = status
#     ll = log --oneline
#  --> https://github.com/GitAlias/gitalias.git
#
# in github: pull request
# setting/branches
#
# git remote add upstream https://github.com/GitAlias/gitalias.git
# git remote -v
# git pull upstream
#
# # tags: app version
# -> semantic version: major release. miner release. patch release
# git tag v1.0.0
# git tag v1.0.0-beta <hash>
# git push --tags
# git tag -a 3Dmode v1.2.0
#
#
# # branching model: gitflow, githubflow, gitlabflow,...
# gitflow: main : tag
#          develop : CI
#          feature branches (--no-ff)
#          release (bug fix)
#          hotfixes
#
#
