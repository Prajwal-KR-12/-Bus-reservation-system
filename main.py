from bus import view_buses
from booking import book_ticket, cancel_ticket, view_bookings

while True:

    print("\n--- Bus Reservation System ---")
    print("1 View Buses")
    print("2 Book Ticket")
    print("3 Cancel Ticket")
    print("4 View Bookings")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        view_buses()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        cancel_ticket()

    elif choice == "4":
        view_bookings()

    elif choice == "5":
        print("Exiting program")
        break

    else:
        print("Invalid choice")