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
            token = authentication.generateAndSaveToken(userId)
            # print(token)
            return {"Login":"Success", "token":token, "userID":userId}
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
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            return api.getUsers()
        else:
            return {"error":"Token is invalid"}
    if session and session['isLoggedIn']:
        return api.getUsers()
    else:
        return {"Error":"User Not Logged In"}


@app.route("/logout", methods = ['POST', 'GET'])
def logout():
    session.clear()
    if request.json and request.json['token']:
        authentication.deleteToken(request.json['token'])
        return {"Logout": "Success"}
    return {"logout":"Success"}


@app.route('/sendMessage', methods=['POST', 'GET'])
def sendMessage():
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            if(request.json['message'] and request.json['receiver']):
                message = request.json['message']
                receiver = request.json['receiver']
                sender = tokenIsValid
                return api.sendMessage(message, sender, receiver)
            else:
                return {"Error": "we need token, message, receiver and sender to successfully send message"}
        else:
            return {"Error":"Token is invalid"}

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

@app.route('/getSentMessages', methods=['POST', 'GET'])
def getAllMessagesSentByUserID():
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            return api.getSentMessages(tokenIsValid)
        else:
            return {"Error":"Invalid token"}

    if session and session['isLoggedIn']:
        userID = session['userId']
        return api.getSentMessages(userID)
    else:
        return {"Error":"User Not Logged In"}  

@app.route('/getUserSendMethods/<int:userID>', methods=['POST', 'GET'])
def getUserSendMethods(userID):
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            return api.getUserSendMethods(userID)
        else:
            return {"Error":"Invalid token"}

    if session and session['isLoggedIn']:
        return api.getSentMessages(userID)
    else:
        return {"Error":"User Not Logged In"}  

@app.route('/getAllSendMethods', methods=['POST', 'GET'])
def getAllSendMethods():
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            return api.getAllSendMethods()
        else:
            return {"Error":"Invalid token"}

    if session and session['isLoggedIn']:
        return api.getAllSendMethods()
    else:
        return {"Error":"User Not Logged In"}  

@app.route('/editUserInformation', methods=['POST', 'GET'])
def updateUserInformation():
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            if(request.json['email'] and request.json['phone'] and request.json['twitter'] and request.json['contactMethodFlags']):
                email = request.json['email']
                phone = request.json['phone']
                twitter = request.json['twitter']
                contactMethodFlags = request.json['contactMethodFlags']
                userId = tokenIsValid
                api.editUserInformation(userId, email, phone, twitter, contactMethodFlags)
                return  api.getUserInformation(tokenIsValid)
                
        else:
            return {"Error":"Invalid token"}

    if session and session['isLoggedIn']:
        email = request.json['email']
        phone = request.json['phone']
        twitter = request.json['twitter']
        userID = session['userId']
        contactMethodFlags = request.json['contactMethodFlags']
        api.editUserInformation(userID, email, phone, twitter, contactMethodFlags)
        return  api.getUserInformation(userID)
    else:
        return {"Error":"User Not Logged In"}  

@app.route('/getUserInformation', methods=['POST', 'GET'])
def getUserInformation():
    if request.json and request.json['token']:
        tokenIsValid = authentication.verifyTokenValid(request.json['token'])
        if tokenIsValid:
            return api.getUserInformation(tokenIsValid)
        else:
            return {"Error":"Invalid token"}

    if session and session['isLoggedIn']:
        return api.getUserInformation()
    else:
        return {"Error":"User Not Logged In"}  

