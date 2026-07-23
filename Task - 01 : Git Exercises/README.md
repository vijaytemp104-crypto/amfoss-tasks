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
git add .
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


