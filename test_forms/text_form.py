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

class GroupCreationForm(FlaskForm):
    group_name = StringField('Group Name')
    purpose = StringField('Purpose')
    group_size = StringField('Group Size')
    source_location = StringField('Source Location')
    destination_location = StringField('Destination Location')
    submit = SubmitField('Submit')

class AddUserForm(FlaskForm):
    groupname = StringField('Group Name')
    username = StringField('Username')
    submit2 = SubmitField('Add User')
