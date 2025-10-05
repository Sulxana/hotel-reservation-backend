import pytest
from Customer import Customer
from Hotel import Hotel
from Room import Room


def test_pay_for_booking():
    c = Customer("Saba", 1000)

    # პირველი გადახდა
    assert c.pay_for_booking(100) == True
    assert c.budget == 900


    assert c.pay_for_booking(999) == False
    assert c.budget == 900

    # მცირე გადახდა, რომელიც წარმატებულია
    assert c.pay_for_booking(10) == True
    assert c.budget == 890



def book_room_for_customer(self, customer: Customer, room_number: int, nights):
        for x in self.rooms:
            if x.room_number == room_number:
                customer.add_room(x,nights)
                break
h = Hotel("ss",[])
def test_book_room_for_customer():
    # შექმენი ოთახები
    room1 = Room(1, "Single", 100, True, 1)
    room2 = Room(2, "Double", 200, True, 2)
    rooms = [room1, room2]

    # შექმენი სასტუმრო და მომხმარებელი
    hotel = Hotel("TestHotel", rooms)
    customer = Customer("Saba", 5000)

    # დაჯავშნა 2 ღამე
    hotel.book_room_for_customer(customer, 1, 2)
    assert len(customer.booked_rooms) == 1

    hotel.book_room_for_customer(customer, 1, 2)
    assert len(customer.booked_rooms) == 2