#!/bin/bash

# run by "./containerize <dir_path>"

echo "starting ..."
python filespawn.py $1
cd $1

echo "done"
