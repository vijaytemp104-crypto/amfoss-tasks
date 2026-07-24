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

Exercise 6: merge-conflict
1)git merge another-piece-of-work
I used git merge to bring the changes from another-piece-of-work into my current branch , this caused a conflict so i opened the conflicted file manually combined both changes removed the conflict markers then staged and committed the resolved file.

Exercise 7: save-your-work
1)git stash push
2)git stash pop
I used git stash to temporarily save my unfinished changes so i could fix and commit the urgent bug first , after that i used git stash pop to restore my previous work then added the final line and committed the completed work.

Exercise 8: change-branch-history
1)git rebase hot-bugfix
I used git rebase hot-bugfix to replay my current branch changes on top of the bug fix branch , this changed the history into a straight line where the bug fix came first and my work came after it.

Exercise 9: remove-ignored
1)git rm --cached ignored.txt
The file was already tracked before it was added to .gitignore so git was still tracking it , i used git rm --cached ignored.txt to remove it only from git tracking while keeping the actual file on my system then committed the change.

Exercise 10: case-sensitive-filename
1)mv File.txt file.txt
2)git add -A
I used mv to rename File.txt to file.txt then used git add -A so git could detect and stage the rename , after that i committed the lowercase filename.

Exercise 11: fix-typo
1)vim file.txt
2)git add file.txt
3)git commit --amend -m "Add Hello world"
I corrected the typo from wordl to world inside file.txt then staged the file and used git commit --amend to update the latest commit along with its commit message , finally i verified the exercise.

Exercise 12: forge-date
1)git commit --amend --date="1987-01-01" --no-edit
I used git commit --amend with the date option to change the date of the latest commit to 1987-01-01 , and --no-edit kept the existing commit message unchanged then i verified the exercise.

Exercise 13: fix-old-typegit rebase -i HEAD~2git commit --amendgit rebase --continuei used interactive rebase to go back and edit the older commit because the typo was not in the latest commit , then i changed wordl to world in file.txt and also fixed the commit message using git commit --amend after that i continued the rebase and got a conflict so i kept the corrected line along with the newer changes removed the conflict markers and continued the rebase again , finally i checked the history and verified the exercise.

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

Exercise 18:commit-parts
1)git add -p file.txt
In this task I had different changes for task 1 and task 2 inside the same file , so I used git add -p file.txt to stage only selected parts of the file , first I pressed s to split the big change into smaller hunks then used y for task 1 changes and n for the remaining ones , after committing task 1 I added the leftover changes normally and made the second commit then verified the exercise.

Exercise 19: pick-your-favourates
1)git cherry-pick
2)git merge --squash
I used `git cherry-pick feature-a` and `git cherry-pick feature-b` to bring both features as separate commits into the current branch , then i used `git merge --squash feature-c` to combine both commits of feature c into one , there was a conflict in `program.txt` so i manually kept all the required changes from features A B and C removed the conflict markers then staged the file and committed feature c as a single commit.

Exercise 20:rebase-complex

1)git rebase --onto
I used `git rebase --onto your-master 8e22462` to move only the two bug fix commits from `rebase-complex` onto `your-master` , here `your-master` was the new base and `8e22462` was the old base so git selected only the commits after it from my current branch , this way the issue-555 commits were not included and only the bug fixes were added.

Exercise 21:invalid-order

I used `git rebase -i HEAD~2` to open commits in interactive mode , after that i swapped the order of the two commit lines saved the file and git recreated the history in the new order.

Exercise 22:find-swearwords
1)git log -S
I used `git log -S"shit" --oneline -- words.txt list.txt` to find all the old commits where the word was added , then i started an interactive rebase from the parent of the oldest commit and marked those commits as `edit` , whenever git stopped i replaced `shit` with `flower` in the required file used `git commit --amend --no-edit` to update that old commit and continued the rebase .

Exercise 23: find-bug
1)git bisect
2)openssl enc -base64 -A -d 
In this task i used `git bisect` to find the first commit where the bug was introduced , i marked `1.0` as good and current `HEAD` as bad then used a command which decoded the base64 text and checked for the word `jackass` , git automatically tested different commits using binary search and found commit `#78` as the first bad commit , after that i pushed that commit to the `find-bug` branch for verification and the exercise passed.



