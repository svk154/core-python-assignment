class CinemaHall:
    def __init__(self, total_seats, booked_seats=None):
        self.total_seats = total_seats
        self.booked_seats = set(booked_seats) if booked_seats else set()

    def book_seat(self, seat_number):
        if seat_number in self.booked_seats:
            print(f"Seat {seat_number} is already booked.")
        elif seat_number < 1 or seat_number > self.total_seats:
            print(f"Invalid seat number! Please choose between 1 and {self.total_seats}.")
        else:
            self.booked_seats.add(seat_number)
            

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            
        else:
            print(f"Seat {seat_number} is not booked yet.")

    def get_available_seats(self):
        return sorted(set(range(1, self.total_seats + 1)) - self.booked_seats)

total_seats = 10
booked_seats = [2, 5, 7]

cinema = CinemaHall(total_seats, booked_seats)

cinema.book_seat(3)

cinema.cancel_seat(5)

print("Available seats:", cinema.get_available_seats())
