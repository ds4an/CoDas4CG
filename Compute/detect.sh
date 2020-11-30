#!/bin/bash
cfiles=`find . -name "*.py"`
for file in $cfiles
do
str1=`basename $file`
#pylint $file --disable R,C >> report/${str1%%.*}.txt 
pylint $file -r n --disable R,C,W
done
