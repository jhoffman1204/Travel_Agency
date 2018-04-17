from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SubmissionForm(FlaskForm):
    name = StringField('Name') # validators=[DataRequired()])
    text = TextAreaField('Your Story') # validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class LoginForm(FlaskForm):
    username = StringField('Name')
    password = StringField('Password')
    email = StringField('Email')
    submit = SubmitField('Submit')
    
class UserSignupForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField('Submit')
    
    
