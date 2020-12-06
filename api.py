import database
import json

def getUsers():
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT userID, username, email  FROM users"
    cursor.execute(sql)
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return str(items)
    else:
        return {"Error":"no users available"}

def sendMessage(message, sender, receiver):
    try:
        db = database.getDB()
        cursor = db.cursor()
        sql = "INSERT INTO messages (content, sender, receiver) VALUES (%s, %s, %s)"
        cursor.execute(sql, (message, sender, receiver))
        db.commit()
        messageSent = sendViaPreferredMethod(content, sender, receiver)
        if messageSent:
            return {"Send Message":"Success"}
        else:
            return {"Error":"Message send failed"}
    except:
        return {"Error":"Send message did not update the database"}

def getSentMessages(userID):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT * FROM messages WHERE sender = %s"
    cursor.execute(sql, (userID,))
    returnData = cursor.fetchall()
    if returnData:
        items = [dict(zip([key[0] for key in cursor.description], row)) for row in returnData]
        return str(items)
    else:
        return {"Error":"no users available"}

def sendViaPreferredMethod(content, sender, receiver):
    db = database.getDB()
    cursor = db.cursor()
    sql = "SELECT contactMethodFlags FROM users WHERE userID = %s"
    cursor.execute(sql, (receiver,))
    data = cursor.fetchone()
    if data:
        userFlagValue = data[0]
        sql = "SELECT id, contactMethodName, contactMethodFlagValue FROM contactMethodFlags where contactMethodFlags < %s"
        cursor.execute(sql, (userFlagValue))
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


    

# def sendMessageViaEmail(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()
#     sql = "SELECT email from users where userID = %s"
#     cursor.execute(sql, (receiver,))
#     data = cursor.fetchone():
#     if data:
#         email = data[0]

#     else:
#         return False


# def sendMessageViaText(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()

# def sendMessageViaVoiceCall(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()

# def sendMessageViaTwitterDM(content, sender, receiver):
#     db = database.getDB()
#     cursor.db.cursor()
