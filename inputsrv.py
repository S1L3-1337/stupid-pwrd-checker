from flask import Flask
from flask import render_template, redirect, url_for, request, jsonify
from main import hash_pwrd, regex

app = Flask(__name__)


@app.route("/")
def mainpg(any=None):
    return render_template('index.html')


@app.route("/<any>")
def redirect_mainpg(any=None):
    return redirect(url_for('mainpg'))


@app.route("/hash", methods=['POST'])
def hashed_password():
    data = request.get_json()
    email = data['email']
    password = data['password']
    regex(email, password)
    return jsonify({'hash': hash_pwrd(password)})
