#!/usr/bin/sh

if type python -v &> /dev/null ; then
	echo "Couldn't find Python on your computer..." 
	read -n1 -r -p "Press any key to continue..." key
	exit 0
fi

if type pip -v &> /dev/null ; then 
	echo "Couldn't find pip on your computer..." 
	read -n1 -r -p "Press any key to continue..." key
	exit 0
else
	pip install pynput
	pip install pillow
	read -n1 -r -p "Press any key to continue..." key
fi