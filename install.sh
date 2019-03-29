#!/usr/bin/sh

if type python -v &> /dev/null then	echo "Couldn't find Python on your computer..."
if type pip &> /dev/null then echo "Couldn't find pipi on your computer..."

pip install pynput
pip install pillow