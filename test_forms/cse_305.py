from flask import Flask, render_template, request, flash
from text_form import SubmissionForm, LoginForm, UserSignupForm
from db_manager import dbm
from object_file import Flight_Obj, Hotel_Obj

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'

current_user = ""

cart_id = []

# need to be able to return flights, hotels and cruises
def get_current_cart_items():
    # need current items added to the cart
    for id in cart_id:
        # dbm.retrieve_item(id)
        print(id)
    
    return cart_id

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
            username = request.form['username']
            password = request.form['password']
            value = dbm.does_user_exist(username, password)
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
        return homepage()
    return render_template('login.html', title='Login', form=form)

@app.route('/hotels', methods=['GET', 'POST'])
def hotels():
    hotels = dbm.retrieve_hotels()
    return render_template('hotels.html', title='Hotels',hotels=hotels)

@app.route('/hotels/<id>', methods=['GET', 'POST'])
def hotels_id(id):
    cart_id.append(id)
    hotels = dbm.retrieve_hotels()
    return render_template('hotels.html', title='Hotels',hotels=hotels)

@app.route('/flights/', methods=['GET', 'POST'])
def flights():
	flights = dbm.retrieve_flights()
	return render_template('flights.html', title='Flights', flights=flights)

@app.route('/flights/<id>', methods=['GET', 'POST'])
def flights_id(id):
    cart_id.append(id)
    flights = dbm.retrieve_flights()
    return render_template('flights.html', title='Flights', flights=flights)

@app.route('/cruises', methods=['GET', 'POST'])
def cruises():
    cruises = dbm.retrieve_cruises()
    return render_template('cruises.html', title='Cruises',cruises=cruises)

@app.route('/cruises/<id>', methods=['GET', 'POST'])
def cruises_id(id):
    cart_id.append(id)
    cruises = dbm.retrieve_cruises()
    return render_template('cruises.html', title='Cruises',cruises=cruises)    

@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    get_current_cart_items()
    return render_template('profile.html', title='Profile')

@app.route('/profile/<id>', methods=['GET', 'POST'])
def profile_ids(id):
    return render_template('profile.html', title='Profile')

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    items = get_current_cart_items()
    flights, hotels, cruises = dbm.retrieve_items(items)
    print(flights)
    print(hotels)
    print(cruises)
    return render_template('cart.html', title='Cart',
    flights = flights, hotels = hotels, cruises=cruises)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():

    return render_template('checkout.html', title='Cart')

@app.route('/checkout_complete', methods=['POST'])
def checkout_complete():
    card_type = request.form['type']
    card_num = request.form['cardnum']
    card_month = request.form['month']
    card_year = request.form['year']
    card_cvv = request.form['cvv']
    print(card_type)
    print(card_num)
    print(card_month)
    print(card_year)
    print(card_cvv)

    date = str(card_year) + "-" + str(card_month) + "-00"

    dbm.create_payment(card_num , date, card_cvv, card_type)

    return render_template('checkout_review.html', title='Cart')

@app.route('/car_rentals', methods=['GET', 'POST'])
def car_rentals():
    return render_template('car_rentals.html', title='Car Rentals')


if __name__ == '__main__':
    app.run()




