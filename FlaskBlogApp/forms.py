from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(label="Username", 
                           validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                       Length(min=3, max=15, message='Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες')])

    email = StringField(label="Email", 
                        validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                    Email(message='Παρακαλώ εισάγετε ένα έγκυρο email')])

    password = StringField(label="Κωδικός", 
                           validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                       Length(min=3, max=15, message='Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες')])

    password2 = StringField(label="Επιβεβαίωση Κωδικού", 
                           validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                       Length(min=3, max=15, message='Αυτό το πεδίο πρέπει να είναι από 3 έως 15 χαρακτήρες'),
                                       EqualTo('password', message="Τα 2 πεδία password πρέπει να είναι τα ίδια")])

    submit = SubmitField(label="Εγγραφή")


class LoginForm(FlaskForm):
    email = StringField(label="Email", 
                        validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                    Email(message='Παρακαλώ εισάγετε ένα έγκυρο email')])

    password = StringField(label="Κωδικός", 
                           validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό')])

    submit = SubmitField(label="Είσοδος")


class NewArticleForm(FlaskForm):
    article_title = StringField(label="Τίτλος άρθρου", 
                           validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                       Length(min=3, max=50, message='Αυτό το πεδίο πρέπει να είναι από 3 έως 50 χαρακτήρες')])

    article_body = TextAreaField(label="Κείμενο Άρθρου", 
                        validators=[DataRequired(message='Αυτό το πεδίο δε μπορεί να είναι κενό'),
                                    Length(min=5, message='Το κείμενο του άρθρου πρέπει να είναι τουλάχιστον 5 χαρακτήρες')])


    submit = SubmitField(label="Αποστολή")