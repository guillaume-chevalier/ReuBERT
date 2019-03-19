#!/bin/sh

files = $(git diff --cached --name-only --diff-filter=ACM | paste -s -d",")
newFiles = `echo $files | tr ',' ' '`

yapf -ri -vv -e env . && git add $newFiles

