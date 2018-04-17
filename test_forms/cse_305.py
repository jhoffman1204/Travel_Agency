from flask import Flask, render_template, redirect
from text_form import SubmissionForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        return "Welcome, " + username + " / " + password + " / " + email
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
