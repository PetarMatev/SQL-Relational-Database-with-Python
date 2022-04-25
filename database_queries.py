query_on_cleaner_01 = """
SELECT * FROM cleaner;
"""

query_on_cleaner_02 = """
SELECT cleaner_id, first_name, address FROM cleaner;
"""

query_on_guest_03 = """
SELECT *
FROM guest
WHERE nationality = "Austrian";
"""

query_on_reservation_04 = """
SELECT * 
FROM reservation
WHERE payment_method = "bank transfer"
ORDER BY website ASC;
"""

query_on_guest_05 = """
SELECT first_name, last_name
FROM guest
WHERE last_name IN ('Evans', 'Smith', 'Fowler', 'Moody');
"""

# Aliasing
query_on_reservation_06 = """
SELECT payment AS 'Reservation Payout', length_of_stay AS 'Length of Reservation (Days)'
FROM reservation
WHERE payment_method = 'bank transfer';
"""

# using average (AVG).
query_on_reservation_07 = """
SELECT website, AVG(length_of_stay)
FROM reservation
GROUP BY website;
"""

# using count
query_on_reservation_08 = """
SELECT payment_method, COUNT(length_of_stay)
FROM reservation
WHERE payment_method = 'Bank Transfer';
"""

# INNER JOINs:
query_on_inner_joins_09 = """
SELECT reservation.reservation_id, reservation.website, reservation.country, reservation.host,
cleaner.first_name, cleaner.last_name
FROM reservation
JOIN cleaner
ON reservation.cleaner = cleaner.cleaner_id
"""

query_on_inner_joints_on_host_10 = """
SELECT reservation.host, reservation.reservation_id, reservation.website, reservation.cleaner,
host.first_name, host.last_name, host.address
FROM reservation
JOIN host
ON reservation.host = host.host_id
WHERE reservation.website = 'Airbnb.com' AND reservation.host = 15;
"""


query_on_inner_joints_on_host_11 = """
SELECT host.first_name, host.last_name
FROM host
JOIN takes_apartment ON takes_apartment.reservation_id = reservation.reservation.id
JOIN guest ON takes_apartment.guest_id = guest.guest_id
WHERE takes_apartment.guest_id = (SELECT takes_apartment.guest_id WHERE reservation.host = 15);
"""



# SELECT participant.first_name, participant.last_name
# FROM participant
# JOIN takes_course ON takes_course.participant_id = participant.participant_id
# JOIN course ON takes_course.course_id = course.course_id
# WHERE takes_course.course_id = (SELECT takes_course.course_id WHERE course.teacher = 6);