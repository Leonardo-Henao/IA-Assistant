#!/bin/bash

# IA-Assistant folder path
dir="/home/lhenaoll/Disk2/Projects/Personal/IA-Assistant"

# File where the GOOGLE_API_KEY environment variable is assigned
src_enviroments="/home/lhenaoll/.dotfiles/.zshrc"

cd $dir
source .env/bin/activate
source $src_enviroments
python ./start.py
