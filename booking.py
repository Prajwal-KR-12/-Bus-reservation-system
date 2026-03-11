from db import cursor, db

def book_ticket():

    name = input("Enter passenger name: ")
    phone = input("Enter phone number: ")

    bus_id = int(input("Enter bus ID: "))
    seat_number = int(input("Enter seat number: "))

    # check if seat already booked
    cursor.execute(
        "SELECT * FROM _bookings WHERE bus_id=%s AND seat_number=%s",
        (bus_id, seat_number)
    )

    result = cursor.fetchone()

    if result:
        print("Seat already booked!")
        return

    # insert passenger
    cursor.execute(
        "INSERT INTO _passengers (name, phone) VALUES (%s,%s)",
        (name, phone)
    )

    passenger_id = cursor.lastrowid

    # insert booking
    cursor.execute(
        "INSERT INTO _bookings (bus_id, passenger_id, seat_number) VALUES (%s,%s,%s)",
        (bus_id, passenger_id, seat_number)
    )

    db.commit()

    print("Ticket booked successfully!")
def cancel_ticket():

    booking_id = input("Enter booking ID: ")

    cursor.execute(
        "DELETE FROM _bookings WHERE booking_id=%s",
        (booking_id,)
    )

    db.commit()

    print("Booking cancelled successfully")

def view_bookings():

    cursor.execute("""
        SELECT p.name, b.bus_id, b.seat_number
        FROM _bookings b
        JOIN _passengers p
        ON b.passenger_id = p.passenger_id
    """)

    bookings = cursor.fetchall()

    print("\nAll Bookings:\n")

    for b in bookings:
        print("Passenger:", b[0])
        print("Bus ID:", b[1])
        print("Seat:", b[2])
        print("--------------------")