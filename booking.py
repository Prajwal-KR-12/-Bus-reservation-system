from db import cursor, db


def book_ticket():
    name = input("Enter passenger name: ")
    phone = input("Enter phone number: ")

    bus_id = int(input("Enter bus ID: "))
    seat_number = int(input("Enter seat number: "))

    # check if bus exists
    cursor.execute(
        "SELECT * FROM _buses WHERE bus_id=%s",
        (bus_id,)
    )

    if not cursor.fetchone():
        print("Invalid Bus ID")
        return

    # check if seat already booked
    cursor.execute(
        "SELECT * FROM _bookings WHERE bus_id=%s AND seat_number=%s",
        (bus_id, seat_number)
    )

    if cursor.fetchone():
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

    booking_id = cursor.lastrowid

    print("\nTicket booked successfully!")
    print("Your Booking ID:", booking_id)
    print("Keep this ID safe for cancellation.\n")


def cancel_ticket():
    booking_id = input("Enter your Booking ID: ")

    # show booking before deleting
    cursor.execute(
        """
        SELECT p.name, b.bus_id, b.seat_number
        FROM _bookings b
        JOIN _passengers p
        ON b.passenger_id = p.passenger_id
        WHERE b.booking_id=%s
        """,
        (booking_id,)
    )

    booking = cursor.fetchone()

    if not booking:
        print("Invalid Booking ID!")
        return

    print("\nBooking Found:")
    print("Passenger:", booking[0])
    print("Bus ID:", booking[1])
    print("Seat:", booking[2])

    confirm = input("Confirm cancellation (y/n): ")

    if confirm.lower() != "y":
        print("Cancellation aborted")
        return

    cursor.execute(
        "DELETE FROM _bookings WHERE booking_id=%s",
        (booking_id,)
    )

    db.commit()

    print("Ticket cancelled successfully.")
def view_bookings():

    cursor.execute("""
        SELECT p.name, p.phone, b.bus_id, b.seat_number, b.booking_id
        FROM _bookings b
        JOIN _passengers p
        ON b.passenger_id = p.passenger_id
    """)

    bookings = cursor.fetchall()

    if not bookings:
        print("No bookings found.")
        return

    print("\nAll Bookings:\n")

    for b in bookings:
        print("Passenger:", b[0])
        print("Phone:", b[1])
        print("Bus ID:", b[2])
        print("Seat:", b[3])
        print("Booking ID:", b[4])
        print("----------------------")