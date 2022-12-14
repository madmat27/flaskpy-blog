from flask import (Flask, 
                    render_template, 
                    redirect, 
                    url_for,
                    request)
from forms import RegisterForm


app = Flask(__name__)

app.config["SECRET_KEY"] = 'my_secret'


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")


@app.route('/register/', methods=["GET", "POST"])
def register():
    
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        password2 = form.password2.data

        print(username, email, password, password2)
    return render_template("register.html", pageForm = form)


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