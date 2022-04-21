#!/bin/sh

# outdir=~/Github/renpy-7.4.11-sdk
# zip -r myfiles.zip $outdirh/*

echo "Enter your  commit message"
read message
git pull
git add .
git commit -am "$message"
git push heroku master
