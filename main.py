from Customer import Customer
from Hotel import Hotel
from Room import Room

#შემყავს ხელით რამდენიმე ოთახი
room_list = list()

#ფასები სეზონურად
Single = 100 * Room.calculate_koeficienti()
Double = 200 * Room.calculate_koeficienti()
Family = 400 * Room.calculate_koeficienti()

for i in range(10):
    if i<3:
        r = Room(i+1, "Single", Single, True, 1)
    elif i<7:
        r = Room(i+1, "Double", Double, True, 2)
    else:
        r = Room(i+1, "Family", Family, True, 4)
    room_list.append(r)

# HOTEL and CUSTOMER
hotel = Hotel("Amazon",room_list)
giorgi = Customer("giorgi",3000)

print("მოგესალმებით სასტუმროში.")
while True:
    q = input("გსურთ ოთახის დაჯავშნა? ( კი / არა ) ")
    if q == "არა":
        break
    r_type = input("გთხოვთ შეიყვანოთ თქვენთვის სასურველი ოთახის ტიპი: ( Single / Double / Family )")
    days = int(input("გთხოვთ შეიყვანოთ რამდენი დღით გსურთ სასტუმროში განთავსება: "))

    print()
    # ვამოწმებ მაქვს თუარა დაუჯავშნელი ოთახი
    if not hotel.show_available_rooms(r_type):
        continue

    r_number = int(input("აირჩიეთ სასურველი ოთახის ნომერი: "))

    hotel.book_room_for_customer(giorgi,r_number,days)
    hotel.log_booking(giorgi)

    q1 = input("გსურთ ჯავშნის გაუქმება? ( კი / არა ) ")
    if q1 == "კი":
        for room,nights,price in giorgi.booked_rooms:
            print(f"{room.room_number} - {room.room_type}")
        q3 = int(input("რომლის გაუქმება გსურთ?(ოთახის ნომერი) "))
        hotel.cancel_booking(giorgi,q3)

    print("=========================================================\n")

booking_summary = giorgi.show_booking_summary()
for s in booking_summary:
    print(s)

