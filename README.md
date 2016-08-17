# We Meet: London Cafes Django Project
***Web App that displays curated places/cafes to Hack in London***	
# Content

1. [Description](#description)
4. [Setup](#setup)
5. [Contributing](#contributing)


# Description
This is volunteer idea to create a web app that will display and allow searching of curated cafes places that are team friendly to go and spend some time hacking together on a project.

The user can come to the website and search bases on London postcode/locations to find a curated list of cafes matching that criteria. The cafes should be shown on a map as well.
Each cafe will be handpicked and “features” ranked like wifi signal, how great is the coffee/food and space etc.

## Tech
- Django (a Python framework)
- Front end SASS/HTML5 and a frontend framework perhaps Bootstrap or Concise CSS
- Gulp or Grunt for frontend build
- Possibly JS for some interactions/ lazy loading images etc
- Github
- Heroku for free hosting
- Perhaps AWS/Cloud Flare CDN for image storage
- Github Issues for tasks
- Slack for group chats/standups etc

## Team
- [Bibiana](https://github.com/BibianaC) - Back End
- [Emiliana](https://github.com/emilianas) - Back End, Front End
- [Ichi](https://github.com/Icicleta) - Back End
- [Karen](https://github.com/neraks) - Front End
- [Lili](https://github.com/lili2311) - PM, Front End, Back End
- [Lucy](https://github.com/LucyMac) - Front-end
- [Nandhini](https://github.com/Nandhini31) - Back End, Front End
- [Natalia](https://github.com/natalia-z) - Front End
- [Nori] (https://github.com/denesnori) - Back End, Front End
- [Nuria](https://github.com/nuria-gs) - Front End (Learning)
- [Raquel](https://github.com/raquel-ucl) - Back End, Front End



# Setup
## Tools
1. **Terminal**: [iTerm2](https://www.iterm2.com/) (MacOSX), [Terminator](http://gnometerminator.blogspot.co.uk/p/introduction.html) (Linux) or use your preffered one.
2. **Text Editor**: [Sublime Text](http://www.sublimetext.com/) or you preffered one.

## Dev Enviroment Setup
1. [Install Git](http://git-scm.com/download/mac)
2. Clone the repo: `git clone git@github.com:womenhackfornonprofits/london-cafes-django.git`
3. Get [Virtual Env](https://virtualenv.pypa.io/en/latest/installation.html) 
4. Get [virtualend wrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)
5. Create a new virtual enviroment for the project `mkvirtualenv london_cafes`
6. Use this enviroment or change to this from another by using: `workon london_cafes`
7. Go to project folder: `pip install -r requirements.txt`
8. Go to project folder: `pip install -r requirements.test`
9. Get [Postgres](http://www.postgresql.org/)
10. Create empty db for now locally, `createdb london_cafes`
11. Start the server: `python manage.py runserver`
12. Go inside frontend folder: 
	
	```cd frontend```
13. Install all the dependencies:

	 ```npm install```

## Running the project locally
1. Go inside the django app directory: 

	```cd london_cafes```
2. Run django server:
	
	```python manage.py runserver```
	
3. The project is now running on `http://127.0.0.1:8000/`, go to that address in your browser. 

## Front End changes
1. Make css and javascript changes in the ```frontend``` folder
2. Make any HTML changes in the Django templates located in `london_cafes/london_cafes/templates`
3. Use `grunt default` in the frontend folder to build, watch and copy all the required files automatically into the Django static folder.

# Contributing
Please follow a few guidelines in order to contribute to the project:

1. Pick an issue in the [backlog](https://github.com/womenhackfornonprofits/we-meet-django/issues) and assign it to yourself.
2. Always create a new branch `git branch branch_name` and all changes you make should be in that branch.
3.  Make the changes needed then save and commit them:
	- Use `git status` to see what changes there are that can be committed.
	- To add a file to be commited: ```git add filename``` *(this will stage the file for a commit)*
	- Once all files you want to commit are added you can  commit the changes ```git commit``` and make sure to add a meaningful message to describe what changes you have made.
4. [Raise a Pull Request](## How to raise a Pull Request
) so other teammembers can review the changes before they are merged5. 
5. Have at least 1 team member review your code *(ideally 2)* and once you receive a :+1: you can merge the code.



	
## How to raise a Pull Request
In order to raise a Pull Request with your changes:

- Save and commit your changes
- Push your changes and create a pull request: `git push origin your_branch_name`
- Go to the [repo](https://github.com/womenhackfornonprofits/we-meet-django) and you should see a green button "Raise a Pull Request"
![](https://help.github.com/assets/images/help/pull_requests/pull-request-click-to-create.png)
- Describe all the changes you have made in details and save.

