# PASSENGER CLASS
class Passenger:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.passport = ""
        self.reservation = ""
        self.contact_no = ""

    def set_name(self, name):
        self.name = name

# FLIGHT CLASS
class Flight:
    def __init__(self):
        self.flight_number = ""
        self.departure_location = ""
        self.destination = ""
        self.date = ""
        self.time = ""
        self.gate = ""

    def set_flight_details(self, flight_number, departure_location, destination, date, time, gate):
        self.flight_number = flight_number
        self.departure_location = departure_location
        self.destination = destination
        self.date = date
        self.time = time
        self.gate = gate

# BOARDING PASS CLASS
class BoardingPass:
    def __init__(self):
        self.passenger = None
        self.flight = None
        self.seat_number = ""
        self.electronic_ticket_number = ""

    def set_boarding_pass_details(self, passenger, flight, seat_number, electronic_ticket_number):
        self.passenger = passenger
        self.flight = flight
        self.seat_number = seat_number
        self.electronic_ticket_number = electronic_ticket_number

    def update_boarding_pass(self, new_flight_details):
        self.flight.set_flight_details(**new_flight_details)

    def display_boarding_pass(self):
        print("Boarding Pass:")
        print(f"Passenger: {self.passenger.name}")
        print(f"Flight Number: {self.flight.flight_number}")
        print(f"Departure Location: {self.flight.departure_location}")
        print(f"Destination: {self.flight.destination}")
        print(f"Date: {self.flight.date}")
        print(f"Time: {self.flight.time}")
        print(f"Gate: {self.flight.gate}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Electronic Ticket Number: {self.electronic_ticket_number}")

# PRE-INPUTTED DATA
passenger = Passenger()
passenger.set_name("Abdulla Alhammadi")

flight = Flight()
flight.set_flight_details("EY81", "AUH", "MXP", "2024-03-01", "3:10 AM", "Gate 10")

boarding_pass_info = {
    "passenger": passenger,
    "flight": flight,
    "seat_number": "12A",
    "electronic_ticket_number": "1234"
}

# CREATE BOARDINGPASS OBJECT
boarding_pass = BoardingPass()
boarding_pass.set_boarding_pass_details(**boarding_pass_info)

# DISPLAY INITIAL BOARDING PASS DETAILS
boarding_pass.display_boarding_pass()

# USER INPUT TO UPDATE BOARDINGPASS OBJECT
update_choice = input("Do you wish to update the boarding pass? (Yes/No): ")

if update_choice.lower() == "yes":
    new_flight_details = {
        "flight_number": input("Enter updated flight number: "),
        "departure_location": input("Enter updated departure location: "),
        "destination": input("Enter updated destination: "),
        "date": input("Enter updated date: "),
        "time": input("Enter updated time: "),
        "gate": input("Enter updated gate: ")
    }

    # UPDATE AND DISPLAY THE BOARDING PASS WITH NEW INFORMATION
    boarding_pass.update_boarding_pass(new_flight_details)
    boarding_pass.display_boarding_pass()
else:
    print("Boarding pass not updated.")



