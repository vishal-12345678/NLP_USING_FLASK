from flask import Flask,render_template,request,redirect         #with remder templates we can directly import html ffiles instead
                                                 # writing them into the function
        # one more thing to notee down is this pycharm here is server and the website we receive output is a client
        # we have to create mutiple routes to run it on differnet servers so we create various routes for it
        # flask has its own server no ther server will be needed
from db import database
import api

app=Flask(__name__)

dbo=database()

@app.route('/')

def index():
    return render_template('login.html')
 #   return "<h1 style='color:blue'> hello world </h1>"   # this is one way to create to create a html body  directly

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform registration',methods=['post'])  # we have two methods get and post post is used for confidential data pass
def perform_registration():                           # perform registration  route will bring data from html to app.py than to json
    name=request.form.get('user_ka_naam')             # these route function will help u to redirect to some web pages
    email=request.form.get('user_ka_email')
    password=request.form.get('user_ka_password')     # to fetch details from html we are using this perform registration route

    response=dbo.insert(name,email,password)          # pass these name , email, pass to function and store output in response

    if response:
        return render_template('login.html',message="registration successful , proceed to login")   # this is optional essage only visible if we go to login page after registration
    else:
        return render_template('register.html',message="Email already exist")

@app.route('/perform login',methods=['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')
    response=dbo.search(email,password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html',message="incorrect email or password try again")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform ner',methods=['post'])
def perform_ner():
    text=request.form.get('ner text')
    response=api.ner(text)
    print(response)

    return render_template('ner.html', response=response)







app.run(debug=True)

#all html file of flask will be stored in directory named templated