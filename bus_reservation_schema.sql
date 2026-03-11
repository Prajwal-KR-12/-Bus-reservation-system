CREATE DATABASE bus_reservations;
USE bus_reservations;

CREATE TABLE _buses (
bus_id INT AUTO_INCREMENT PRIMARY KEY,
bus_name VARCHAR(50) NOT NULL,
source VARCHAR(50) NOT NULL,
destination VARCHAR(50) NOT NULL,
total_seats INT NOT NULL
);

CREATE TABLE _passengers (
passenger_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
phone VARCHAR(15) NOT NULL
);

CREATE TABLE _bookings (
booking_id INT AUTO_INCREMENT PRIMARY KEY,
bus_id INT,
passenger_id INT,
seat_number INT,

FOREIGN KEY (bus_id) REFERENCES _buses(bus_id),
FOREIGN KEY (passenger_id) REFERENCES _passengers(passenger_id),

UNIQUE (bus_id, seat_number)
);

INSERT INTO _buses (bus_name, source, destination, total_seats)
VALUES
('KSRTC Express','Mysore','Bangalore',40),
('KSRTC Express','Shivamogga','Bangalore',40),
('VRL Travels','Bangalore','Hubli',40);


SELECT p.name, b.bus_id, b.seat_number
FROM _bookings b
JOIN _passengers p
ON b.passenger_id = p.passenger_id;

SELECT 
p.name AS Passenger,
b.bus_id,
b.seat_number
FROM _bookings b
JOIN _passengers p
ON b.passenger_id = p.passenger_id;

SELECT seat_number
FROM _bookings
WHERE bus_id = 1;
DELETE FROM _bookings
WHERE booking_id = 1;
SELECT * FROM _buses;
