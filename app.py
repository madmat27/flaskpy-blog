from flask import (Flask, 
                    render_template, 
                    redirect, 
                    url_for,
                    request)
import json


app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/register/', methods=["GET", "POST"])
def register():
    
    if request.method == 'POST':
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password2 = request.form["password2"]
        print(username, email, password, password2)
    return render_template("register.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/logout/')
def logout():
    return redirect(url_for("index"))


@app.route('/new-article/')
def newarticle():
    return render_template("new-article.html")


if __name__ == "__main__":
    app.run(debug=True)