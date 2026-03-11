from db import cursor

def view_buses():

    cursor.execute("SELECT * FROM _buses")

    buses = cursor.fetchall()

    print("\nAvailable Buses:\n")

    for bus in buses:
        print("Bus ID:", bus[0])
        print("Bus Name:", bus[1])
        print("Route:", bus[2], "→", bus[3])
        print("Total Seats:", bus[4])
        print("----------------------")