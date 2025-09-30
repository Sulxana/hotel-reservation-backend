from Room import Room
import pytest
class Customer:
    def __init__(self,name:str, budget:float, score = 0):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.__score = score
    def add_room(self, rooms:Room, nights):
        if not rooms in self.booked_rooms:
            if self.pay_for_booking(rooms.calculate_price(nights)):
                self.booked_rooms.append((rooms, nights))
                rooms.is_available = False

                if rooms.room_type == "Single":
                    self.__score += 50
                elif rooms.room_type == "Double":
                    self.__score += 100
                else:
                    self.__score += 250

                print(f"{self.name} - დაჯავშნა ოთახიN:{rooms.room_number}. მიმდინარე ბალანსი - {self.budget}")
                print(f"შენ გაქვს დაგროვებული: {self.__score} ქულა.")

            else:
                print(f"{self.name} - ვერ დაჯავშნა ოთახიN:{rooms.room_number}"
                      f" არასაკმარისი ბალანსის გამო. მიმდინარე ბალანსი - {self.budget}")
        else:
            print(f"{self.name} - ვერ დაჯავშნა ოთახიN:{rooms.room_number}, რადგან უკვე დაჯავშნილი იყო")

    def remove_room(self,rooms:Room):
        for r, nights in self.booked_rooms:
            if r is rooms or r.room_number == rooms.room_number:
                self.booked_rooms.remove((r, nights))
                r.is_available = True
                print(f"{self.name} - გააუქმა ოთახიN:{r.room_number}-ის ჯავშანი")
                return
        else:
            print(f"{self.name} - ვერ გააუქმა ოთახიN:{rooms.room_number}-ის ჯავშანი, რადგან არ ყოფილა დაჯავშნილი")

    def pay_for_booking(self,total_price:float):
        if self.budget >= total_price:
            self.budget -= total_price
            return True
        else:
            return False

    def show_booking_summary(self):
        summaries = []
        for room, day in self.booked_rooms:
            line = f"{self.name} დაჯავშნა ოთახი N:{room.room_number} - {room.price_per_night}₾(დღე), {day} დღით"
            summaries.append(line)  # სიაში დამატება
        return summaries
