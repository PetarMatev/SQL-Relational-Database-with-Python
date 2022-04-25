create_table_host = """
CREATE TABLE host (
  host_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  address VARCHAR(100),
  nationality VARCHAR(40)
  );
"""

populate_table_host = """
INSERT INTO host
 (host_id,
 first_name,
 last_name,
 phone_no,
 address,
 nationality
 )values(%s,%s,%s,%s,%s,%s)
"""