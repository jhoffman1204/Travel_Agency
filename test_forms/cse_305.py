from flask import Flask, render_template, redirect
from text_form import SubmissionForm, LoginForm, UserSignupForm
from db_manager import dbm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'

@app.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', title='HomePage')
    

@app.route('/', methods=['GET', 'POST'])
def signup():
    form = UserSignupForm()
    if form.validate_on_submit():
        password = form.password.data
        email = form.email.data
        x = dbm.add_new_user(email, password)
        if x:
            return homepage()
    return render_template('edwardHTML/login-register.html', title='Signup', form=form)    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
#        username = form.username.data
#        password = form.password.data
#        email = form.email.data
        return homepage()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()

