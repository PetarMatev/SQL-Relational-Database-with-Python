create_table_reservation = """
CREATE TABLE reservation (
  reservation_id INT PRIMARY KEY,
  num_guests INT,
  length_of_stay INT,
  payment FLOAT,
  commission FLOAT,
  website VARCHAR(20),
  country VARCHAR(40),
  payment_method VARCHAR(20),
  host INT,
  cleaner INT
  );
"""


populate_table_reservation = """
INSERT INTO reservation
 (reservation_id,
  num_guests,
  length_of_stay,
  payment,
  commission,
  website,
  country,
  payment_method,
  host,
  cleaner)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""