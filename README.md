# soc409
this entire folder should be the projects directory for renpy. The folder titled `game_project` is where is the game itself is located that we edit.

if you are using vscode and get errors from pylance or another conflicting extension do 
` ctrl -shift - p` 
and configure file associations for .rpy to renpy.

## Editing
edits should be in the [main script file](game_project/game/script.rpy)

## Deploying 
```
$ heroku login
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
You must have the Heroku cli  installed to do that.