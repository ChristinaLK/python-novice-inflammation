#!/bin/bash

for file in 0*.md 10*.md
do
grep subtitle $file
grep -A 7 "{.objectives}" $file
grep -A 4 "{.python}" $file
done
