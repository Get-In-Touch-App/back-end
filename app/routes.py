from app import app 

@app.route('/')
@app.route('/index')
def index():
    return "hi world!!!!"

@app.route('/superSecretCodePath')
def secret():
    return '<h1>you shouldnt be seeing this; an agent will stop by to correct this</h1>'
    