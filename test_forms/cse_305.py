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
        dbm.add_new_user(email, password)
        return homepage()
    return render_template('signup.html', title='Signup', form=form)    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
#        username = form.username.data
#        password = form.password.data
#        email = form.email.data
        return homepage()
    return render_template('login.html', title='Login', form=form)

@app.route('/hotels', methods=['GET', 'POST'])
def hotels():
    return render_template('hotels.html', title='Hotels')

@app.route('/car_rentals', methods=['GET', 'POST'])
def car_rentals():
    return render_template('car_rentals.html', title='Car Rentals')

@app.route('/flights', methods=['GET', 'POST'])
def flights():
    return render_template('flights.html', title='Flights')

@app.route('/cruises', methods=['GET', 'POST'])
def cruises():
    return render_template('cruises.html', title='Cruises')

if __name__ == '__main__':
    app.run()

