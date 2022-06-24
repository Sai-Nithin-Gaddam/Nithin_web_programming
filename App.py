from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/Login", methods=['GET'])
def get_login():
    return render_template('Rogin.html')

@app.route("/Login", methods=['POST'])
def post_login():
    username = request.form.get("uname", "<missing uname>")
    password = request.form.get("pwd", "<missing pwd>")

@app.route("/Register", methods=['GET'])
def get_register():
    return render_template('Register.html')

@app.route("/Register", methods=['POST'])
def post_register():
    username = request.form.get("uname", "<missing uname>")
    password = request.form.get("pwd", "<missing pwd>")
    repeat_password = request.form.get("repeat_pwd", "<missing repeat_pwd>")