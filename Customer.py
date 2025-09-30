from Room import Room

class Customer:
    def __init__(self,name,budget,booked_rooms):
        self.name = name
        self.budget = budget
        self.booked_rooms = booked_rooms

    def add_room(self, rooms:Room):
        pass
    def remove_room(self,rooms:Room):
        pass
    def pay_for_booking(self,total_price:float):
        pass
    def show_booking_summary(self):
        pass
