from Customer import Customer
from Hotel import Hotel
from Room import Room

room_list = list()
for i in range(10):
    if i<3:
        r = Room(i+1, "Single", 100, True, 1)
    elif i<7:
        r = Room(i+1, "Double", 200, True, 2)
    else:
        r = Room(i+1, "Family", 400, True, 4)
    room_list.append(r)
hotel = Hotel("Amazon",room_list)

giorgi = Customer("giorgi",5000)
mariami = Customer("mariami",200)

while True:
    print("მოგესალმებით სასტუმროში.")
    r_type = input("გთხოვთ შეიყვანოთ თქვენთვის სასურველი ოთახის ტიპი: ( Single / Double / Family )")
    days = int(input("გთხოვთ შეიყვანოთ რამდენი დღით გსურთ სასტუმროში განთავსება: "))

    print()

    if not hotel.show_available_rooms(r_type):
        continue

    r_number = int(input("აირჩიეთ სასურველი ოთახის ნომერი: "))

    hotel.book_room_for_customer(giorgi,r_number,days)


