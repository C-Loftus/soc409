# soc409
## About
This repository holds all the  code for our final project for SOC/COS 409.  For this project, our group developed a novel educational solution for teaching concepts regarding seed sovereignty. To accomplish these goals, we created a website on Heroku which hosted an educational game with a backend for storing user data. This project was intended to bring in perspectives from sustainable HCI  literature  to motivate our design.  We wanted to use reflective design principles to strength user connections to seed sovereignty.
 ## How to Use Our Website
Our website is hosted at https://soc409project.herokuapp.com/ It is recommended to not use Chrome to view this website.  The game framework we use is currently resolving a bug on Chrome-based  browsers.

 To interact with our website simply click start on the game once it has loaded. As you play you may be prompted to submit images of your plants or provide user reflections. In order to do this,  first save your game to make sure you don't lose any progress.Then, simply click on the corresponding tabs at the top of the website. This will bring you to https://soc409project.herokuapp.com/newpost where you can submit the appropriate data.


  When you complete the game you may want to learn more about the experience of other players.
  To view others' posts go to https://soc409project.herokuapp.com/allposts At  this part of the website you can see other images or delete your own if you no longer wish them to be public.

  Additionally, you can also geographically situate yourself using the map at https://soc409project.herokuapp.com/maps
    At the bottom of this page it will display all the locations of the user images. You can then mark them on the map.  We do not parse any image metadata from user uploads in order to protect user privacy. Therefore, we do not automatically display picture locations on the map. This map functionality is for user convenience more than technical reasons.

## Technical Infrastructure
There were four main technical components to our project.
 #### Ren'Py
 Ren'py is a visual novel engine that we used to create our story. Documentation for the engine can be found can be found [here](https://www.renpy.org/doc/html/). Ren'py  uses user scripts in order to create narrative driven  stories. All assets and files for our game can be found in `renpyAssets`
 #### Heroku
 Heroku  is a website hosting service that allows us to host not only HTML but also our backend code and database. We use Heroku's Postgresql  database as our way of storing user submitted content.
 #### Flask
 Flask is a backend framework that we used to read from our database  and display  the user submitted content to others.

#### Timeline JS
Timeline JS  is the tool we used to build the timeline on our website.  This tool takes a CSV file and parses it with images into a timeline that can be exported to a webpage. Documentation and more info can be found at https://timeline.knightlab.com
 ## Building From Source

This entire folder should be the projects directory for renpy. The folder titled `renpyAssets` is where is the game itself is located that we edit.

if you are using vscode and get errors from pylance or another conflicting extension do 
` ctrl -shift - p` 
and configure file associations for .rpy to renpy.

 Once this folder is loaded into Renpy,  you can compile it  into the format that can be used for web hosting.

### Editing
Script root should be in `renpyAssets/game/script.rpy`. From there you can link to other scripts.  

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
