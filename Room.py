from datetime import datetime


class Room:
    def __init__(self, r_number: int, r_type: str, price_per_night: float, is_available: bool, max_guests: int):
        self.room_number = r_number
        self.room_type = r_type
        self.price_per_night = price_per_night
        self.is_available = is_available
        self.max_guests = max_guests

    def book_room(self):
        self.is_available = False
        print(f"თქვენ დაჯავშნეთ {self.room_number} ოთახი {self.max_guests} სტუმარზე")

    def release_room(self):
        self.is_available = True
        print(f"თქვენ გამოხვედით {self.room_number} ოთახიდან ")

    @staticmethod
    def calculate_koeficienti():
        month = datetime.today().month
        match month:
            case 1 | 2 | 3 | 4 | 5:
                mult = 2
            case 6 | 7 | 8 | 9:
                mult = 3
            case _:
                mult = 1
        return mult

    def calculate_price(self, nights: int):
        mult = Room.calculate_koeficienti()
        return self.price_per_night * nights * mult

    def __str__(self):
        if self.is_available:
            return f"ოთახიN:{self.room_number}, {self.max_guests} სტუმარზე, ამ ეტაპზე თავისუფალია და მისი ფასია {self.price_per_night}"
        else:
            return f"ოთახიN:{self.room_number}, {self.max_guests} სტუმარზე, ამ ეტაპზე დაკავებულია"
