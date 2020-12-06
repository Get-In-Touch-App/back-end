import mysql.connector


def getDB():
    db = mysql.connector.connect(host="localhost", user="getAholdOfMe", password="aholdGetter", database="getAholdOfMe")
    return db


#sql instructions: 
#CREATE DATABASe getAholdOfMe
#CREATE USER 'getAholdOfMe'@'localhost' IDENTIFIED BY 'aholdGetter';
#GRANT ALL PRIVILEGES ON getAholdOfMe.* TO 'getAholdOfMe'@'localhost';
#copy all text in db.sql and paste it in the database window thing. 


#python instructions (this assumes you have the codebase downloaded along with python3 and you're in the back-end directory): 
#WINDOWS:
#    POWERSHELL
#        .\venv\Scripts\Activate.ps1
#        $env:FLASK_APP="getInTouch.py"
#        $env:FLASK_ENV="development"
#        flask run
#    CMD 
#        .\vent\Scripts\activate.bat
#        set FLASK_APP=app.py
#        set FLASK_ENV=development
#        flask run
#UNIX:
#    python3 -m pip install venv
#    python3 venv venv
#    ./venv/bin/activate
#    export FLASK_APP=app.py
#    export FLASK_ENV=development
#run "pip install flask"
#run "pip install mysql-connector-python"
#run "pip install flask cors"
#run "flask run"
    