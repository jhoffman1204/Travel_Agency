CREATE TABLE Transportation (
	transportation_ID 	INTEGER,
	transportation_type	VARCHAR(255),
	PRIMARY KEY (transportation_ID),
	CHECK transportation_ID > 0
);

CREATE TABLE Groups(	
	Id INTEGER,
	purpose VARCHAR(255),
	source_location VARCHAR(255), 
	destination_location VARCHAR(255),
	group_size VARCHAR(255),
	PRIMARY KEY (groupID) ,
	CHECK Id > 0 
);

CREATE TABLE Group_Passengers (
	Id INTEGER,
	groupID INTEGER,
	age INTEGER,
	Name VARCHAR(255),
	gender VARCHAR(255),
	PRIMARY KEY (Id),
	FOREIGN KEY(groupID) REFERNCES Groups(ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK ( groupID>0 AND Id >0 AND age>0 )
);

CREATE TABLE Payment (
	card_number INTEGER,
	card_expiration_date DATE, 
	payment_type VARCHAR(255),
	PRIMARY KEY (card_number),
	CHECK(card_number>0)
);
	
CREATE TABLE Location (
	location_ID INTEGER,
	city_name VARCHAR(255), 
	payment_type VARCHAR(255),
	PRIMARY KEY (location_ID),
	CHECK (location_ID>0)
);
	
CREATE TABLE Accomodation (
	address VARCHAR(255),
	discount INTEGER, 
	rate_per_night INTEGER,
	PRIMARY KEY (address),
	CHECK (discount>0 AND rate_per_night >0
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
	arrival_date DATE,
	depart_date DATE,
	fare INTEGER,
	PRIMARY KEY (cruise_number),
	FOREIGN KEY (cruise_number) REFERENCES Transportation(transportation_ID) ,
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK(cruise_number >0 AND depart_date <= arrival_date)
); 
	
CREATE TABLE Cruise_destinations (
	cruise_number INTEGER,
	destination VARCHAR (255), 
	PRIMARY KEY (cruise_number, destination) 
	FOREIGN KEY(cruise_number) REFERENCES Cruise(cruise_number)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK(cruise_number >0
);
	
CREATE TABLE Car_rental (
	confirmation_ID INTEGER,
	car_type VARCHAR(255), 
	rent INTEGER,
	PRIMARY KEY (confirmation_ID)
	FOREIGN KEY (confirmation ID) REFERENCES Transportation (transportation_ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK(confirmation_ID>0)
);
CREATE TABLE Flight (
	flight_number INTEGER,
	carrier VARCHAR(255), 
	class VARCHAR(255),
	depart_date DATE,
	arrival_date DATE,
	fare INTEGER,
	destination VARCHAR,
	PRIMARY KEY (flight_number)
	FOREIGN KEY (flight_number) REFERENCES Transportation(transportation_ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK(flight_number >0 AND fare>0 AND depart_date <= arrival_date)
) ;
	
CREATE TABLE Reviews (
	passenger_ID INTEGER,
	groupID INTEGER, 
	rating INTEGER,
	detailed_review VARCHAR(255),
	PRIMARY KEY (passengerID),
	FOREIGN KEY(passenger_ID) REFERENCES Group_Passengers(Id),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK( rating BETWEEN 1 AND 5),
	CHECK( passenger_ID >0 AND groupID >0)
);
		
CREATE TABLE Group_Transportation (
	transportation_ID INTEGER,
	mode_of_transport VARCHAR(255),
	groupID INTEGER,
	travel_date DATE,
	PRIMARY KEY (transportation_ID, groupID, mode_of_transport),
	FOREIGN KEY(transportationID) REFERENCES Transportation(transportation_ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREGIN KEY(groupID) REFERENCES Groups(ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK (transportation_ID>0 AND mode_of_transport>0)
);
	
CREATE TABLE Group_Payment (
	card_number INTEGER,
	groupID INTEGER,
	price INTEGER,
	PRIMARY KEY (card_number, groupID),
	FOREIGN KEY(card_number) REFERENCES Payment(card_number),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREIGN KEY(groupID) REFERENCES Groups(ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION

);
	
CREATE TABLE Group_Accomodation (
	address VARCHAR(255),
	groupID INTEGER,
	cost INTEGER,
	reservation_date DATE,
	PRIMARY KEY (address, groupID, reservation_date), 
	FOREIGN KEY (groupID) REFERENCES Groups(ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREIGN KEY (address) REFERENCES Accommodation(address),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	CHECK (groupID >0 AND cost>0 )
);
	
CREATE TABLE Transports_to (
	location_ID INTEGER,
	transportation_ID INTEGER,
	travel_date DATE,
	PRIMARY KEY (transportation_ID, location_ID, travel_date),
	FOREIGN KEY (transportation_ID) REFERENCES Transportation(transportation_ID),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREIGN KEY (location_ID) REFERENCES Location(location_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION

):


CREATE TABLE Transportation_Reviews (
	passengerID INTEGER,
	transportation_ID INTEGER, 
	review_date DATE,
	PRIMARY KEY (passengerID, transportation_ID),
	FOREIGN KEY(passengerID) REFERENCES Group_Passengers(Id),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREIGN KEY(transportation_ID) REFERENCES Transportation(transportation_ID)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION

);


CREATE TABLE Accomodation_Reviews (
	passengerID INTEGER,
	address VARCHAR (255), 
	review_date DATE,
	PRIMARY KEY (passengerID, address),
	FOREIGN KEY(passengerID) REFERENCES Group_Passengers(Id),
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
	FOREIGN KEY(address) REFERENCES Accommodation(address)
		ON UPDATE CASCADE 
		ON DELETE NO ACTION
);

ALTER TABLE Groups ADD CONSTRAINT Group_in_Group_Passengers
	CHECK ( NOT EXISTS ( 
		SELECT * 
		FROM Groups G 
		WHERE NOT EXISTS 
			( SELECT * 
			FROM Group_Passengers P 
			WHERE G.Id = P.groupID ) ) );

ALTER TABLE Transportation ADD CONSTRAINT Transportation_in_transports_to
	CHECK ( NOT EXISTS ( 
		SELECT * 
		FROM Transportation T 
		WHERE NOT EXISTS 
			( SELECT * 
			FROM Transports_to D 
			WHERE T.transportation_ID = D.transportation_ID ) ) );

ALTER TABLE Groups ADD CONSTRAINT Group_in_group_payment
	CHECK ( NOT EXISTS ( 
		SELECT * 
		FROM Groups G 
		WHERE NOT EXISTS 
			( SELECT * 
			FROM Group_Payment P 
			WHERE G.Id = P.groupID ) ) );


