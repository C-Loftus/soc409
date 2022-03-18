# soc409
this entire folder should be the projects directory for renpy. The folder titled `renpyAssets` is where is the game itself is located that we edit.

if you are using vscode and get errors from pylance or another conflicting extension do 
` ctrl -shift - p` 
and configure file associations for .rpy to renpy.

## Editing
script root should be in `renpyAssets/game/script.rpy`. from there you can link to other scripts

## Deploying 
```
$ heroku login
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
You must have the Heroku cli  installed to do that.

## Testing locally
```
# install dependencies
pipenv install 
# run from project root (you can also do pipenv run python3 wsgi.py)
pipenv run flask run
```
