Exercise 1: Master
Commands Used :1) git start next
I used this command to start the master exercise. It prepared the
repository and created the required Git history for the task.

Exercise 2: commit-one-file
1)git start commit-one-file
It was used to start the
`commit-one-file` exercise. It prepared the repository and created the
files required for the task.
2)git add A.txt
3)git git commit -m "Added A"

Exercise 3: commit-one-file-staged
1)git reset
Other commands:
git add A.txt
git commit -m "Added A.txt"

Exercise 4: ignore-them
1)vim ./.gitignore
I used made a .gitignore file and edited it on vim editor(personal fav) to ignore the given files.
Other commands:
git add a
git commit -m "Added .gitignore"

Exercise 5: Chase branch
1)git merge escape
The chase-branch branch was behind the escaped branch by two commits.
I used git merge escaped while I was on chase-branch.Since there were
no conflicting commits,Git performed a fast-forward merge and moved
chase-branch to the same commit as escaped.

Exercise 13: fix-old-type
git rebase -i HEAD~2
git commit --amend
git rebase --continue
i used interactive rebase to go back and edit the older commit because the typo was not in the latest commit , then i changed wordl to world in file.txt and also fixed the commit message using git commit --amend after that i continued the rebase and got a conflict so i kept the corrected line along with the newer changes removed the conflict markers and continued the rebase again , finally i checked the history and verified the exercise.

Exercise 14: commit-lost
1)git reflog
2) git reset --hard 4a8cd43
i used git reflog to find the old commit because after using git commit --amend the previous commit was not visible in normal git log , reflog showed where HEAD was pointing before so i checked the old commit hash and then used git reset --hard <4a8cd43> to move the commit-lost branch back to that original commit and finally verified the exercise.

Exercise 15:split-commit
1)git reset HEAD~1
I used `git reset HEAD~1` to remove the last commit without deleting the file changes , then i staged and committed `first.txt` first and after that staged and committed `second.txt` separately , finally i checked the commit history and verified the exercise.

Exercise 16: too-many-commits
I checked the last two commits using `git log -2` and since both had very small changes i used `git rebase -i HEAD~2` , then I kept the first commit as `pick` and changed the second one to `squash` so both commits were combined into one....easy peasy:

Exercise 17: executable
1)chmod +x script .sh
The `script.sh` file was not executable so i used `chmod +x script.sh` to add execute permission , then i staged and committed the permission change so the script can be run directly using `./script.sh` without using `bash script.sh` every time.

Exercise 18:

