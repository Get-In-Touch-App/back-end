from flask import session, request, redirect, url_for, render_template
from app import app 
import authentication
import api

@app.route('/')
@app.route('/index')
def index():
    return "hi world!!!!"


@app.route('/superSecretCodePath')
def secret():
    return '<h1>you shouldnt be seeing this; an agent will stop by to correct this</h1>'


@app.route('/login', methods = ['POST', 'GET'])
def login():
    print(request)
    print(dir(request))
    if request.method == 'POST':
        print ("post it")
        username = request.form['username'];
        password = request.form['password'];
        userId = authentication.checkLogin(username, password)
        if (userId):
            session['isLoggedIn'] = True;
            session['username'] = username;
            session['userId'] = userId;
            return render_template('loginSuccess.html', user=username)
        else:
            return render_template('loginFail.html')
    else:
        return render_template('login.html')


@app.route('/loginAPI', methods = ['POST', 'GET'])
def apiLogin():
    print(request)
    print(request.json)
    print(request.json['username'])
    if(request.json and request.json['username'] and request.json['password']):
        username = request.json['username']
        password = request.json['password']
        userId = authentication.checkLogin(username, password)
        if userId:
            session['isLoggedIn'] = True;
            session['username'] = username; 
            session['userId'] = userId;
            return {"Login":"Success"}
        else:
            return {"Error":"authenticationFailure"}
    else:
        return {"Error": "Username and password not sent as json request"}


@app.route('/sessionTest', methods = ['POST', 'GET'])
def sessiontest():
    print(session)
    return (session)


@app.route('/getUsers', methods = ['POST', 'GET'])
def getUsers():
    if session and session['isLoggedIn']:
        return api.getUsers()
    else:
        return {"Error":"User Not Logged In"}


@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    session.clear()
    return {"logout":"Success"}


@app.route('/sendMessage', methods=['POST', 'GET'])
def sendMessage():
    if session and session['isLoggedIn']:
        if(request.json and request.json['message'] and request.json['receiver']):
            message = request.json['message']
            receiver = request.json['receiver']
            sender = session['userId']
            return api.sendMessage(message, sender, receiver)
        else:
            return {"Error":"message and receiver fields not present in json"}
    else:
        return {"Error":"User Not Logged In"}

@app.route('/getSentMessages/<int:userID>', methods=['POST', 'GET'])
def getAllMessagesSentByUserID(userID):
    if session and session['isLoggedIn']:
        return api.getSentMessages(userID)
    else:
        return {"Error":"User Not Logged In"}  
