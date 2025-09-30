import logging
from Room import Room
from Customer import Customer
logging.basicConfig(filename='booking.log', level=logging.INFO, format='%(asctime)s - %(message)s',encoding="UTF-8")

class Hotel:
    def __init__(self,name:str,rooms:list):
        self.name = name
        self.rooms = rooms
        self.booking_log = list()
    def show_available_rooms(self, r_type: str = None):
        result = list()
        for x in self.rooms:
            if x.room_type ==r_type and x.is_available == True:
                result.append(x)

        if not result:
            print(f"სამწუხაროდ {r_type} ოთახები ყველა დაჯავშნილია")
        else:
            for room in result:
                print(room)

        return  result

    def book_room_for_customer(self, customer: Customer, room_number: int, nights):
        for x in self.rooms:
            if x.room_number == room_number:
                customer.add_room(x,nights)
                break

    def calculate_total_booking(self, room_number: int, nights: int):
        for x in self.rooms:
            if x.room_number == room_number:
                total = x.calculate_price(nights)
                return total
        return 0

    def log_booking(self, customer: Customer):
        summary = customer.show_booking_summary()
        for s in summary:
            logging.info(f"{s}")

    def cancel_booking(self, customer: Customer, room_number: int):
        for x in self.rooms:
            if x.room_number == room_number:
                customer.remove_room(x)
                break




