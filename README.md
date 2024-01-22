# for_git_course

➜  ~ cd Desktop/for_git_course 
➜  for_git_course git init

Initialized empty Git repository in /Users/denisburguto/Desktop/for_git_course/.git/

➜  for_git_course git:(master) ✗ git branch -m main
➜  for_git_course git:(main) ✗ git remote add origin git@github.com:DenisBurguto/for_git_course.git
➜  for_git_course git:(main) ✗ git pull origin main
From github.com:DenisBurguto/for_git_course
 * branch            main       -> FETCH_HEAD
➜  for_git_course git:(main) ✗ git add main.py 
➜  for_git_course git:(main) ✗ git commit -m "initial commit"
➜  for_git_course git:(main) ✗  git push --set-upstream origin main

Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 610 bytes | 610.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:DenisBurguto/for_git_course.git
   baf2acd..17765c7  main -> main
branch 'main' set up to track 'origin/main'.
