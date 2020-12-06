import database 

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