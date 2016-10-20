# Django-Tutorial

Follow along with the slides here: ________________
Adapted from: https://docs.djangoproject.com/en/1.10/intro/tutorial01/

We are going to build a Poll for people to vote on the project to win Semester.ly's award! (Or anything else). 

##Step 0: Clone the Repository
If you don't have git, install it here: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
Once you have it, click the Fork button above to make your own version of this repo! 

##Step 1: Install Python/Pip

Django is a web framework that works with Python. If you don't already have python, install it here: https://www.python.org/downloads/

Now, we are going to go ahead and install Django, and VirtualEnv. To do this, simply enter the repository:
```
cd \path\to\Django-Tutorial
```
and checkout the file 'requirements.txt', you'll see:
```
Django==1.9.2
virtualenv==1.11.4
```
Now let's install pip. Simply run
```
sudo python get-pip.py
```
Now you've installed pip!
##Step 2: Enter your Virtual Environment and Install Requirements
First, enter:
```
source venv/bin/activate
```
Then, execute: 
```
pip install -r --user requirements.txt
```
You will install Django version 1.9.2 and virtulenv 1.11.4

##Step 3: Boom, Workshop Done!
Try this: 
```
python manage.py runserver
```
Now, head over to 'localhost:8000' [in your favorite browser (Chrome, of course)](https://gfycat.com/IllustriousPowerfulIlsamochadegu)
Check it out! Your server is working.

####Your app works - k bai! 

##Step 4: Jk, jk - let's get to it: Write your First View

Now, you'll see in your directory the following: 
```
Django-Tutorial/
├── db.sqlite3
├── djangoworkshop
├── get-pip.py
├── manage.py
├── polls
├── README.md
├── requirements.txt
└── venv
```
This is because we've setup your app directory for you. In the future you can execute 'python manage.py startapp name_of_your_app' to do this. 

Let's go ahead and write one of those views we talked about earlier. Open the file **polls/views.py**
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Look mom! I made a web app!")
```
When a request is routed to this method, it will respond with HTTP as shown above.

In order to see the result, we need to route a url to call our view! To do this, go ahead and open **polls/urls.py** and include the following code:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
What this does is map the url matching regex '^$' (which would be localhost:8000 without anything after) to the method named 'index' in our views file. 

Go ahead and run your server again, and go to [http://localhost:8000/polls/](http://localhost:8000/polls/) - you should see your message. 

##Step 5: The Database & Migrations
Remember models? That way we represent objects, relationships and store them to the Database? 
Well, before we write one we are going to need to talk about the Database. 

You have many choices of databases, The Semester.ly team uses PostgreSQL. You can easily switch, but for simplicity, we are going to use SQLite. SQLite is included in Python, so you won’t need to install anything else to support your database.

Let's get started by executing the following command:
```bash
$ python manage.py migrate
```
We will run this any time we add or edit a model. This command automatically executes a SQL migration that tells your database how to add/remove/edit the tables used to store your objects/relationships. This is pretty magical, you don't need to write any SQL - Django will automatically transform your python into a database :). We don't have any tables yet, so this command is just initializing our database. 

In the future, when you edit the models.py file, execute the following to update your DB: 
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

##Step 6: Models
We are going to make two models: a question and a choice.

**Question** defined by a publication date, and a question text.

**Choice** defined by the text of the choice, and the tally (count).

One might say that **a question has many choices**. - to represent this relationship each Choice will point to a question to show what it belongs to. 
