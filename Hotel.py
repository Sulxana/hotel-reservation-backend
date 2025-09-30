import logging
from ctypes import c_wchar

from Room import Room
from Customer import Customer

class Hotel:
    def __init__(self,name:str,rooms:list,booking_log:list):
        self.name = name
        self.rooms = rooms
        self.booking_log = booking_log
    def show_available_rooms(self, r_type: str = None):
        for x in self.rooms:
            if x.room_type ==r_type and x.is_available == True:
                print(x)


    def book_room_for_customer(self, customer: Customer, room_number: int, nights):
        for x in self.rooms:
            if x.room_number ==room_number:
                customer.add_room(x)
                break

    def calculate_total_booking(self, room_number: int, nights: int):
        for x in self.rooms:
            if x.room_number == room_number:
                total = x.calculate_price(nights)
                return total
        return 0
    def log_booking(self, customer: Customer, rooms: Room):
        logging.info(customer.show_booking_summary())

    def cancel_booking(self, customer: Customer, room_number: int):
        for x in self.rooms:
            if x.room_number == room_number:
                customer.remove_room(x)
                break




