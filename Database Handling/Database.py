import psycopg2

connect = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres",
                           password = 32134, port = 5432)
cur = connect.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person(
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1,'Simon', 24, 'M'),
(2,'Elezabeth', 22, 'F'),
(3,'Max', 26, 'M'),
(4,'Jimmy', 28, 'M');
""")

connect.commit() # This saves everything I have done.

cur.close() # This closes the cursor indicating that I am done giving queries.
connect.close() # This closes the database completely.