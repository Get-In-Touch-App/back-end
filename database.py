import mysql.connector


def getDB():
    db = mysql.connector.connect(host="localhost", user="getAholdOfMe", password="aholdGetter", database="getAholdOfMe")
    return db