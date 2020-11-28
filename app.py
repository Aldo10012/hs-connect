from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    return render_template("signup.html")


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)