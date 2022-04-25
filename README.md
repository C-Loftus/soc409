# soc409
## About
This repository holds all the  code for our final project for SOC/COS 409.  For this project, our group developed a novel educational solution for teaching concepts regarding seed sovereignty. To accomplish these goals, we created a website on Heroku which hosted an educational game with a backend for storing user data. This project was intended to bring in perspectives from sustainable HCI  literature  to motivate our design.  We wanted to use reflective design principles to strength user connections to seed sovereignty.
 ## How to Use Our Website
Our website is hosted at https://soc409project.herokuapp.com/ It is recommended to not use Chrome to view this website.  The game framework we use is currently resolving a bug on Chrome-based  browsers.

 To interact with our website simply click start on the game once it has loaded.  as you play you may be prompted to submit images of your plants or provide user reflections. In order to do this,  first save your game to make sure you don't lose any progress.Then, simply click on the corresponding tabs at the top of the website.  These tabs will bring you to forms where you can submit the appropriate data.

  To view others' posts go to https://soc409project.herokuapp.com/allPosts At  this part of the website you can see other images or delete your own if you no longer wish them to be public.


 ## Building From Source

This entire folder should be the projects directory for renpy. The folder titled `renpyAssets` is where is the game itself is located that we edit.

if you are using vscode and get errors from pylance or another conflicting extension do 
` ctrl -shift - p` 
and configure file associations for .rpy to renpy.

 Once this folder is loaded into Renpy,  you can compile it  into the format that can be used for web hosting.

### Editing
Script root should be in `renpyAssets/game/script.rpy`. From there you can link to other scripts

### Deploying 
```
$ heroku login
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
You must have the Heroku cli  installed to do that.

## Testing locally
If you wish to test the website locally you can do so using pipenv. 
```
# install dependencies
pipenv install 
# run from project root (you can also do pipenv run python3 wsgi.py)
pipenv run flask run
```
