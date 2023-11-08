from flask import Flask #The FLASK framework (the webserver)
from flask import render_template  # For opening and read the HTML file and showing them as the webpage
from flask import request  #Allows me to get stuff from the URL (the ?)

from flask import redirect, url_for, g # Use images from the static folder
#from projects import Project


app=Flask(__name__)
# Change DATABASE
#app.config['DATABASE'] = 'database.db'
#db = Project('database.db')
#db.create_table()

@app.route("/")  
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/home") 
def home():
    return render_template('home.html')

@app.route("/listings") 
def listings():
    return render_template('listings.html')

@app.route("/mylistings") 
def mylistings():
    return render_template('mylistings.html')

@app.route("/reviews") 
def reviews():
    return render_template('reviews.html')

@app.route("/inbox") 
def inbox():
    return render_template('inbox.html')


@app.route("/login") 
def login():
    return render_template('login.html')

@app.route("/signup") 
def signup():
    return render_template('signup.html')



app.run(debug=True)