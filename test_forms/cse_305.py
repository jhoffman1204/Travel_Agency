from flask import Flask, render_template, request, flash
from text_form import SubmissionForm, LoginForm, UserSignupForm
from db_manager import dbm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'

@app.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html', title='HomePage')
    

@app.route('/', methods=['GET', 'POST'])
def signup():
    #  POST REQUEST #
    if request.method=='POST':
        print ("POSTING")
        # Registering
        if "confirm-password" in request.form:
#            print("Checking passwords")
            username = request.form['username']
            password = request.form['password']
            passwordConfirm = request.form['confirm-password']
#            print("Password: " + password)
#            print("Password Confirm: " + passwordConfirm)
            # Add to database
            if password == passwordConfirm:
                value = dbm.add_new_user(username,password)
                if value:
                    flash('Account created successfully')
                else:
                    flash('Username in use')
                return render_template('edwardHTML/login-register.html', title='Signup')
            # Error
            else:
                flash('Passwords do not match', 'failure')
                return render_template('edwardHTML/login-register.html', title='Signup')
        # Logging in 
        else:
            value = dbm.does_user_exist()
            if value == 1:
                return render_template('homepage.html', title='Homepage')
            elif value == 0:
                flash('Username does not exist')
                return render_template('edwardHTML/login-register.html', title='Signup')
            elif value == -1:
                flash('Incorrect password')
                return render_template('edwardHTML/login-register.html', title='Signup')
            else:
                flash('Unexpected error. Please try again')
                return render_template('edwardHTML/login-register.html', title='Signup')     
    # GET REQUEST #
    else:
        return render_template('edwardHTML/login-register.html', title='Signup')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
#        username = form.username.data
#        password = form.password.data
#        email = form.email.data
        return homepage()
    return render_template('login.html', title='Login', form=form)

@app.route('/Flight', methods=['GET', 'POST'])
def Flight():
    flight = ['a' , 'b' , 'c']
    return render_template('Flight.html', flight=flight)

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

