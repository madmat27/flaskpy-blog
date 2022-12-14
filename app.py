from flask import (Flask, 
                    render_template, 
                    redirect, 
                    url_for,
                    request)
from forms import RegisterForm, LoginForm, NewArticleForm


app = Flask(__name__)

app.config["SECRET_KEY"] = 'ac705a4bd56725c32496cfbb757526fb'


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
    return render_template("register.html", form = form)


@app.route('/login/', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        print(email, password)

    return render_template("login.html", form = form)


@app.route('/logout/')
def logout():
    return redirect(url_for("index"))


@app.route('/new-article/', methods=["GET", "POST"])
def newarticle():

    form = NewArticleForm()

    if request.method == 'POST' and form.validate_on_submit():
        article_title = form.article_title.data
        article_body = form.article_body.data

        print(article_title, article_body)

    return render_template("new-article.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)