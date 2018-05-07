from flask import Flask, render_template, request, flash
from text_form import SubmissionForm, LoginForm, UserSignupForm, GroupCreationForm, AddUserForm
from db_manager import dbm
from object_file import Flight_Obj, Hotel_Obj

app = Flask(__name__)
app.config['SECRET_KEY'] = 'somesecretkey'

current_user = ""
current_user_id = 0
current_total_price = 0
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
    global current_user
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
                current_user = username
                return render_template('homepage.html', title='Homepage', name=current_user)
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

@app.route('/flights_specific', methods=['GET', 'POST'])
def flights_specific():
    arrival = request.form['Arrival Date']
    depart =  request.form['Departure Date']
    dest=request.form['To']



    print(arrival)
    print(depart)

    flights = dbm.filter_flights(arrival, depart, dest)

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

@app.route('/create_group', methods=['GET', 'POST'])
def create_group():

    groups = dbm.retrieve_group(dbm.get_user_id(current_user))
    form = GroupCreationForm()
    form2 = AddUserForm()
    if form.validate_on_submit():
        if(form2.groupname.data != "" and form2.username.data != ""):
            group_id = dbm.get_group_id(form2.groupname.data)
            user_id = dbm.get_user_id(form2.username.data)
            dbm.add_user_group(user_id,group_id)
        else:
            group_name = form.group_name.data
            purpose = form.purpose.data
            group_size = form.group_size.data
            source_location = form.source_location.data
            destination_location = form.destination_location.data
            dbm.create_group(group_name, purpose, source_location, destination_location, group_size)

            userID = dbm.get_user_id(current_user)
            groupID = dbm.get_group_id(group_name)
            dbm.add_user_group(userID , groupID)
            return homepage()
    
    return render_template('create_group.html', title='Create', form=form, groups=groups, form2=form2)


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    items = get_current_cart_items()
    global flights
    global hotels
    global cruises
    flights, hotels, cruises = dbm.retrieve_items(items)
    total_cost=0
    for flight in flights:
    	total_cost+=flight.fare
    for hotel in hotels:
    	total_cost+=hotel.rate_per_night
    for cruise in cruises:
    	total_cost+=cruise.fare
    return render_template('cart.html', title='Cart',
    flights = flights, hotels = hotels, cruises=cruises, cost=total_cost)

@app.route('/checkout/<price>', methods=['GET', 'POST'])
def checkout(price):
    global current_total_price
    current_total_price = price
    return render_template('checkout.html', title='Cart', price=price, submit_failed=False)

@app.route('/checkout_complete', methods=['POST'])
def checkout_complete():
    card_type = request.form['type']
    card_num = request.form['cardnum']
    print(card_num)
    card_month = request.form['month']
    card_year = request.form['year']
    card_cvv = request.form['cvv']
    group = request.form['group']

    if (card_type == "") or (card_num == "") or (card_month == "") or (card_year == "") or (card_cvv == "") or (group == ""):
        checkout(0)
        return render_template('checkout.html', title='Cart', price=current_total_price, submit_failed=True)

    date = str(card_year) + "-" + str(card_month) + "-00"

    print(current_total_price)

    if(dbm.get_payment(card_num) == False):
        dbm.create_payment(card_num , date, card_cvv, card_type)

    dbm.create_Group_Payment(card_num, dbm.get_group_id(group), current_total_price)

    for flight in flights:
    	dbm.create_Group_transportation(flight.flight_number, dbm.get_group_id(group))
    for hotel in hotels:
    	dbm.create_Group_transportation(hotel.accomodation_id, dbm.get_group_id(group))
    for cruise in cruises:
    	dbm.create_Group_Accomodation(cruise.cruise_number, dbm.get_group_id(group))


    del cart_id[:]

    return render_template('checkout_review.html', title='Cart')

@app.route('/password_change', methods=['POST'])
def password_change():
    global current_user
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    confirm_password = request.form['new_password_confirm']
    
    # Checks old password against database
    check_old_password = dbm.get_user_password(current_user, old_password)
    if check_old_password == 1:
        # Checks to make sure new_password and confirm_passwod match
        if new_password == confirm_password:
            dbm.set_user_password(current_user, new_password)
            return render_template('profile.html', title='Profile', passwordSuccessMessage='Password has been updated')
        else:
            return render_template('profile.html', title='Profile', passwordErrorMessage='New passwords do not match')
    else:
        return render_template('profile.html', title='Profile', passwordErrorMessage='Incorrect Password')

@app.route('/car_rentals', methods=['GET', 'POST'])
def car_rentals():
    return render_template('car_rentals.html', title='Car Rentals')


if __name__ == '__main__':
    app.run()




