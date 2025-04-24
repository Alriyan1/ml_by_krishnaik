from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask tutorial!'

@app.route("/index")
def index():
    return 'welcome to index page'


if __name__ == '__main__':
    app.run(debug=True)