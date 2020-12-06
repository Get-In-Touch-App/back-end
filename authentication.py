import database 
import random
import string
import time


def checkLogin(username, password):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT userID FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, password))
    returnData = cursor.fetchone()
    if returnData:
        return returnData[0]
    else:
        return False


def generateAndSaveToken(userID):
    letters = string.ascii_uppercase
    token = ''.join(random.choice(letters) for i in range(69))
    db = database.getDB()
    cursor = db.cursor()
    sql = "INSERT INTO token(token, userID, expiration) VALUES (%s, %s, %s)"
    expiration = time.time()+60*60*24*7
    print ("this will expire", expiration)
    cursor.execute(sql, (token, userID, expiration))
    db.commit()
    return token 
    
def deleteToken(token):
    db = database.getDB()
    cursor = db.cursor()
    sql = "UPDATE token set expiration = 0 where token = %s"
    cursor.execute(sql, (token,))
    db.commit()
    return True

def verifyTokenValid(token):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT expiration, userId from token where token = %s"
    cursor.execute(sql, (token,))
    data = cursor.fetchone()
    if data:
        if data[0] < time.time():
            return False
        else:
            return data[1] 