from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label="Username")
    email = StringField(label="Email")
    password = StringField(label="Κωδικός")
    password2 = StringField(label="Επιβεβαίωση Κωδικού")
    submit = SubmitField(label="Εγγραφή")