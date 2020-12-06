import database
import json
import smtplib 

def getUsers():
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT userID, username, email  FROM users"
    cursor.execute(sql)
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return {"getUsers":items}
    else:
        return {"Error":"no users available"}

def sendMessage(message, sender, receiver):
    # try:
    db = database.getDB()
    cursor = db.cursor()
    sql = "INSERT INTO messages (content, sender, receiver) VALUES (%s, %s, %s)"
    cursor.execute(sql, (message, sender, receiver))
    db.commit()
    messageSent = sendViaPreferredMethod(message, sender, receiver)
    if messageSent:
        return {"Send Message":"Success"}
    else:
        return {"Error":"Message send failed"}
    # except:
    #     return {"Error":"Send message did not update the database"}

def getSentMessages(userID):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT * FROM messages WHERE sender = %s"
    cursor.execute(sql, (userID,))
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return {"getSentMessages":items}
    else:
        return {"Error":"no users available"}

def getUserSendMethods(userID):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT a.id, a.contactMethodName, a.contactMethodFlagValue from contactMethodFlags a inner join users b on a.contactMethodFlagValue & b.contactMethodFlags and b.userID = %s"
    cursor.execute(sql, (userID,))
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return {"getUserSendMethods":items}
    else:
        return {"Error":"no send methods available"}

def getAllSendMethods():
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT id, contactMethodName, contactMethodFlagValue from contactMethodFlags"
    cursor.execute(sql)
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return {"getAllSendMethods":items}
    else:
        return {"Error":"no send methods available"}

def getUserInformation(userID):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT email, phone, twitter, contactMethodFlags from users where userID = %s"
    cursor.execute(sql, (userID,))
    print (sql, userID)
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return {"userInformation":items}
    else:
        return {"Error":"no data available"}

def editUserInformation(userId, email, phone, twitter, contactMethodFlags):
    db = database.getDB()
    cursor = db.cursor()
    sql = "UPDATE users set email = %s, phone = %s, twitter = %s, contactMethodFlags = %s WHERE userID = %s"
    cursor.execute(sql, (email, phone, twitter, contactMethodFlags, userId))
    db.commit()
    return True  


def sendViaPreferredMethod(content, sender, receiver):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT contactMethodFlags FROM users WHERE userID = %s"
    cursor.execute(sql, (receiver,))
    data = cursor.fetchone()
    if data:
        userFlagValue = data[0]
        sql = "SELECT id, contactMethodName, contactMethodFlagValue FROM contactMethodFlags where contactMethodFlagValue <= %s"
        cursor.execute(sql, (userFlagValue,))
        availableFlags = cursor.fetchall()
        if availableFlags:
            for x in range(0, len(availableFlags)):
                if availableFlags[x][2] & userFlagValue:
                    if availableFlags[x][1] == "email":
                        sendMessageViaEmail(content, sender, receiver)
                    # if availableFlags[x][1] == "text":
                    #     sendMessageViaText(content, sender, receiver)
                    # if availableFlags[x][1] == "voice call":
                    #     sendMessageViaVoiceCall(content, sender, receiver)
                    # if availableFlags[x][1] == "twitter DM":
                    #     sendMessageViaTwitterDM(content, sender, receiver)
        return True


    

def sendMessageViaEmail(content, sender, receiver):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT email from users where userID = %s"
    cursor.execute(sql, (receiver,))
    data = cursor.fetchone()
    if data:
        email = data[0]
        try:
            #login to smtp server to send email
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            gmail_user='getaholdofmenexient@gmail.com'
            gmail_password = 'SuperSecretPassword1'
            server.login(gmail_user, gmail_password)
            #get username of sender so we know who is sending this message
            sql = "SELECT username from users where userID = %s"
            cursor.execute(sql, (sender,))
            sender = cursor.fetchone()[0]
            # Message = "!!!Urgent Message from john doe: " + 
            message = "!!!Urgent message from " + str(sender) + " " +  str(content)
            print (message)
            server.sendmail(gmail_user, email, message)
            print(gmail_user, email, message)
            return True
        except:
            print("Email exceptioned out")
            return False

    else:
        print("No data")
        return False


def sendMessageViaText(content, sender, receiver):
    db = database.getDB()
    cursor.db.cursor()
    sql = "SELECT phone from users where userID = %s"
    cursor.execute(sql, (receiver,))
    data = cursor.fetchone()
    if data:
        email = data[0]


# def sendMessageViaVoiceCall(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()

# def sendMessageViaTwitterDM(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()
