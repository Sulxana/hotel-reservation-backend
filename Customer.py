from Room import Room

class Customer:
    def __init__(self,name:str, budget:float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []

    def add_room(self, rooms:Room, nights):
        if not rooms in self.booked_rooms:
            if self.pay_for_booking(rooms.calculate_price(nights)):
                self.booked_rooms.append(rooms)
                rooms.is_available = False
                print(f"{self.name} - დაჯავშნა ოთახიN:{rooms.room_number}. მიმდინარე ბალანსი - {self.budget}")
            else:
                print(f"{self.name} - ვერ დაჯავშნა ოთახიN:{rooms.room_number}"
                      f" არასაკმარისი ბალანსის გამო. მიმდინარე ბალანსი - {self.budget}")
        else:
            print(f"{self.name} - ვერ დაჯავშნა ოთახიN:{rooms.room_number}, რადგან უკვე დაჯავშნილი იყო")

    def remove_room(self,rooms:Room):
        if rooms in self.booked_rooms:
            self.booked_rooms.remove(rooms)
            rooms.is_available = True
            print(f"{self.name} - გააუქმა ოთახიN:{rooms.room_number}-ის ჯავშანი")
        else:
            print(f"{self.name} - ვერ გააუქმა ოთახიN:{rooms.room_number}-ის ჯავშანი, რადგან არ ყოფილა დაჯავშნილი")

    def pay_for_booking(self,total_price:float):
        if self.budget > total_price:
            self.budget -= total_price
            return True
        else:
            return False

    def show_booking_summary(self):
        for x in self.booked_rooms:
            print(f"{self.name} დაჯავშნა ოთახი N:{x.room_number} - {x.price_per_night}₾(დღე)")


