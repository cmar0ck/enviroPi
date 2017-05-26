#!/bin/bash

echo
echo "Firing up EnviroPi:"
echo "###################"
echo

read -p "Do you want logs to be written to 'nohup.out'? (y/n) " choice
case "$choice" in   
  y|Y ) echo;
  	echo "starting 'sensors2db.py'";
  	nohup python sensors2db.py & 
  	echo "starting 'simpleserver.py'";
	nohup python simpleserver.py & 
	echo "starting 'timelapse.py'";
	nohup python timelapse.py & 
	echo 
	echo "(enter 'tail -f nohup.out' to monitor logs)";;
  n|N ) echo;
  	echo "starting 'sensors2db.py'";
	nohup python sensors2db.py </dev/null >/dev/null 2>&1 & 
	echo "starting 'simpleserver.py'";
	nohup python simpleserver.py </dev/null >/dev/null 2>&1 & 
	echo "starting 'timelapse.py'";
	nohup python timelapse.py </dev/null >/dev/null 2>&1 & 
	echo;
	echo "(no logs will be written to nohup.out)";;
  * ) 	echo "invalid input";;
esac
echo

echo
echo "...done!"
echo
