# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
"""
Git is a tool that tracks changes to your code
GitHub is where you can store your code on the internet (cloud)
Git Bash is a terminal that works with Git and allows you to interface with it
"""

# 2) What’s the difference between the terminal and the command line?
"""
A command line is within a terminal, and is the place the user can type things to be interpreted by the terminal program
"""

# 3) How does Windows PowerShell differ from Git Bash?
"""
Windows Powershell uses the default Windows built in command structures, whereas Git Bash uses Linux/Unix based ones
"""

# 4) What’s the difference between Anaconda, conda, and Python?
"""
Python is the language
Conda is a package installer
Anaconda is the two above + pre-installed libraries and allows you to import libraries conveniently
"""

# 5) What is VS Code? 
"""
It's a code editor where you can write code
"""

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
"""
Jupyter Lab is more comprehensive and comes with features like a terminal, file browser, etc. whereas Notebook is just a code editor
"""

# 7) What does ~/ mean?
"""
Home directory
"""

# 8) What’s the difference between an absolute path and a relative path?
"""
Absolute is starting from the largest file and all the nested files, but relative is just relative to your current file location
"""

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
"""
absolute: ~/austin/python_decal_sp26/course_assignments/homework2
relative: course_assignments/homework2
"""

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
"""
cd ..
"""

# 11) What would rm ./ do in your current directory? (Don’t try it!)
"""
it permanently deletes everything in your current directory
"""

# 12) What do the following commands do?
# git add
# git commit
# git push
"""
add: staging
commit: snapshot
push: uploading to github
"""

# 13) What's the difference between "git add ." and "git add <file>"?
"""
. stages all files in the current directory, but <file> only stages a specific file
"""

# 14) What do "git status" and "git log -1" do?
"""
git status shows what's been saved and what hasn't
log -1 shows the most recent commit
"""

# 15) What’s the difference between cloning a repository and pulling from it?
"""
clone downloads the repository from github for the first time, whereas pull updates it once it's already been downloaded
"""

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
"""
that copying paths on windows is super annoying because the windows way of formatting paths uses backslashes instead of forwardslashes
"""

# 17) What’s a question you still have? What’s something you’re confused about?
"""
howcome there isn't a way to program on the cloud, and keep everything synced? using the terminal seems like it will be easy to forget things.
"""

# 18) Tell me a fun fact!
"""
A T-rex couldn't rotate its hands to point down, instead, they were perpetually pointing towards each other almost as if they were clapping.
"""

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
import math as math
print(math.pow(2,3)) #takes the first number and raises it to the power of the second. I like it because it sounds fun to say: POW!