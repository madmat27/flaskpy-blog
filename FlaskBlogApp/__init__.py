from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = 'ac705a4bd56725c32496cfbb757526fb'

from FlaskBlogApp import routes