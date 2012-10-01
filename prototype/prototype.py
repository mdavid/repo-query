#!/usr/bin/env python


import os
import sys
import re
import subprocess



rootdir = "/home/stevejb/Projects"
ignore_folders = "/home/stevejb/backups"

git_repos = []

for (path, dirs, files) in os.walk(rootdir):    
    # print path
    # print dirs
    # print files
    for file in dirs:
        if re.search('^\.git$', file):
            print path
            git_repos.append(path)



## for each repository, check the status
repo_status = []
for repodir in git_repos:
    os.chdir(repodir)
    x = subprocess.check_output(["git", "status"])
    repo_status.append(x)

## from here, it is a matter of parsing and displaying each
## repo status 
