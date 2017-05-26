#!/bin/bash

echo
echo "Terminating EnviroPi processes..."
echo 

pkill -9 -f sensors2db.py
pkill -9 -f simpleserver.py
pkill -9 -f timelapse.py

echo "...done!"
echo
