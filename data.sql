CREATE TABLE Transportation (
	transportation_ID 	INTEGER,
	transportation_type	VARCHAR(255),
	PRIMARY KEY (transportation_ID)
);
CREATE TABLE Groups(
    groupID INTEGER AUTO_INCREMENT,
	purpose VARCHAR(255),
	source_location VARCHAR(255), 
	destination_location VARCHAR(255),
	group_size VARCHAR(255),
	PRIMARY KEY (groupID)
);
CREATE TABLE Group_Passengers (
	Id INTEGER AUTO_INCREMENT,
	groupID INTEGER,
	age INTEGER,
	Name VARCHAR(255),
	gender VARCHAR(255),
	PRIMARY KEY (Id),
	FOREIGN KEY(groupID) REFERENCES Groups(groupID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Payment (
	card_number INTEGER,
	card_expiration_date DATE, 
	payment_type VARCHAR(255),
	PRIMARY KEY (card_number)
);
CREATE TABLE Location (
	location_ID INTEGER AUTO_INCREMENT,
	city_name VARCHAR(255), 
	payment_type VARCHAR(255),
	PRIMARY KEY (location_ID)
);
CREATE TABLE Accomodation (
    name VARCHAR(255),
	address VARCHAR(255),
	rate_per_night INTEGER,
	PRIMARY KEY (address)
);
CREATE TABLE Accomodation_facilities (
	address VARCHAR(255), 
	facilities VARCHAR(255),
	PRIMARY KEY (address, facilities),
	FOREIGN KEY (address) REFERENCES Accomodation(address)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Cruise (
	cruise_number INTEGER,
	source_location VARCHAR(255), 
    dest_location VARCHAR(255),
	arrival_date DATE,
	depart_date DATE,
	fare INTEGER,
	PRIMARY KEY (cruise_number),
	FOREIGN KEY (cruise_number) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
); 
CREATE TABLE Cruise_destinations (
	cruise_number INTEGER AUTO_INCREMENT,
	destination VARCHAR (255), 
	PRIMARY KEY (cruise_number, destination),
	FOREIGN KEY(cruise_number) REFERENCES Cruise(cruise_number)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Car_rental (
	confirmation_ID INTEGER,
	car_type VARCHAR(255), 
	rent INTEGER,
	PRIMARY KEY (confirmation_ID),
	FOREIGN KEY (confirmation_ID) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Flight (
	flight_number INTEGER,
	carrier VARCHAR(255), 
	classt VARCHAR(255),
	depart_date DATE,
	arrival_date DATE,
	fare INTEGER,
	destination VARCHAR(255),
	PRIMARY KEY (flight_number),
	FOREIGN KEY (flight_number) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);	
CREATE TABLE Reviews (
	userId INTEGER, 
	rating INTEGER,
    review_target VARCHAR(255),
	detailed_review VARCHAR(255),
	PRIMARY KEY (userId)
);		
CREATE TABLE Group_Transportation (
	transportation_ID INTEGER AUTO_INCREMENT,
	mode_of_transport VARCHAR(255),
	groupID INTEGER,
	travel_date DATE,
	PRIMARY KEY (transportation_ID, groupID, mode_of_transport),
	FOREIGN KEY(transportation_ID) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY(groupID) REFERENCES Groups(groupID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Group_Payment (
	card_number INTEGER,
	groupID INTEGER,
	price INTEGER,
	PRIMARY KEY (card_number, groupID),
	FOREIGN KEY(card_number) REFERENCES Payment(card_number)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY(groupID) REFERENCES Groups(groupID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);	
CREATE TABLE Group_Accomodation (
	address VARCHAR(255),
	groupID INTEGER,
	cost INTEGER,
	reservation_date DATE,
	PRIMARY KEY (address, groupID, reservation_date), 
	FOREIGN KEY (groupID) REFERENCES Groups(groupID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY (address) REFERENCES Accomodation(address)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Transports_to (
	transportation_ID INTEGER,
    location_ID INTEGER,
	travel_date DATE,
	PRIMARY KEY (transportation_ID, location_ID, travel_date),
	FOREIGN KEY (transportation_ID) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY (location_ID) REFERENCES Location(location_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Transportation_Reviews (
	passengerID INTEGER,
	transportation_ID INTEGER, 
	review_date DATE,
	PRIMARY KEY (passengerID, transportation_ID),
	FOREIGN KEY(passengerID) REFERENCES Group_Passengers(Id)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY(transportation_ID) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Accomodation_Reviews (
	passengerID INTEGER,
	address VARCHAR (255), 
	review_date DATE,
	PRIMARY KEY (passengerID, address),
	FOREIGN KEY(passengerID) REFERENCES Group_Passengers(Id)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION,
	FOREIGN KEY(address) REFERENCES Accomodation(address)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);
CREATE TABLE Users (
    userId INT AUTO_INCREMENT,
    email VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY(userId)
);