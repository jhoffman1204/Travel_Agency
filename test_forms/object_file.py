class Flight_Obj:
    def __init__(self, flight_number, carrier, classt, depart_date, arrival_date, fare, destination):
        self.flight_number = flight_number
        self.carrier = carrier
        self.classt = classt
        self.depart_date = depart_date
        self.arrival_date = arrival_date
        self.fare = fare
        self.destination = destination

class Hotel_Obj:
    def __init__(self,accomodation_id, name,address, rate_per_night ):
        self.accomodation_id = accomodation_id
        self.name = name
        self.address = address
        self.rate_per_night = rate_per_night

class Cruise_Obj:
    def __init__(self,cruise_number,source_location, dest_location, arrival_date, depart_date, fare):
        self.cruise_number = cruise_number
        self.source_location = source_location
        self.dest_location = dest_location
        self.arrival_date = arrival_date
        self.depart_date = depart_date
        self.fare = fare

class Group:
    def __init__(self,group_id,group_name,purpose, source_location, destination_location, group_size):
        self.group_id = group_id
        self.group_name = group_name
        self.purpose = purpose
        self.source_location = source_location
        self.destination_location = destination_location
        self.group_size = group_size