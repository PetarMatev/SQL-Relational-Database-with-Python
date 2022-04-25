
# creating composite key in SQL
create_table_takes_apartment = """
CREATE TABLE takes_apartment (
  guest_id INT,
  reservation_id INT,
  PRIMARY KEY(guest_id, reservation_id),
  FOREIGN KEY(guest_id) REFERENCES guest(guest_id) ON DELETE CASCADE,
  FOREIGN KEY(reservation_id) REFERENCES reservation(reservation_id) ON DELETE CASCADE
  );
"""


populate_table_takes_apartment = """
INSERT INTO takes_apartment
 (guest_id, reservation_id)values(%s,%s)
"""