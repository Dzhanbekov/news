# news

#unpack zip file and open it in vscode or pycharm or another integrated development environment
#then in your laptor should to be downloaded Docker "https://www.docker.com/get-started/"

#then open terminal and find projects directory and write this command:

Docker-compose build

#wait some minute and write next command:

docker-compose up

#project is run, you can open "http://localhost:8000/news/" and create new post

#command for create super user
docker-compose exec web python manage.py createsuperuser.


###
#Instruction for use this project: "http://localhost:8000/news/" is mainpage

#in the navbar you can see 5 hyperlink:

#first icon MainPage is all news without pagination
#second link for create new news, picture is optionly
#third link for show news by 10
#fourth link for show news by 40
#fivth link for show news by 50




