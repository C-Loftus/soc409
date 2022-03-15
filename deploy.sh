#!/bin/sh
heroku login
echo "Enter your  commit message"
read message
git pull
git add .
git commit -am "$message"
git push heroku master