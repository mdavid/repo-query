repo-query
==========

## Main Idea ##

Looks for all of the git, hg, svn, cvs, and bzr repositories on your computer. Tells you if they are in sync or not.

## Status ##
I have an extremely rudimentary version in `prototype/`

## Design Ideas ##
Prototype this in Python. Perhaps add some UI it Qt afterwards. Then, if it needs to be faster, redo in C++. 

## Basic Design ##

1. Scan the filesystem, starting with the home directory
2. Look for files that indicate the root of a repository (e.g. a `.git` folder or a `.hg` folder for now)
3. Build up a list of repositories, categorized by type (`git`, `hg`, etc.)
4. For each repository, check to see how the current version is in sync with the *master*

### Information to Display ###
+ Current version of remote, current branch, current version of tip

### For git ###
1. Do a `git remote update` and it should let me know if I am beind, and if so, by how many commits

### For hg ###

1. Use the [following piece of advice](http://mercurial.selenic.com/wiki/FAQ#FAQ.2FCommonProblems.How_can_I_find_out_if_there_are_new_changesets_in_a_remote_repository.3F)

### For svn ###

See [this](http://beerpla.net/2008/07/23/how-to-check-if-the-local-svn-revision-is-up-to-date/).


