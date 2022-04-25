create_table_guest = """
CREATE TABLE guest (
  guest_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  address VARCHAR(100),
  nationality VARCHAR(40)
  );
"""

populate_table_guest = """
INSERT INTO guest
 (guest_id,
 first_name,
 last_name,
 phone_no,
 address,
 nationality
 )values(%s,%s,%s,%s,%s,%s)
"""