import psycopg2

def enter_details():
    student_id = int(input("\nEnter student's ID: "))
    name = str(input("\nEnter name: "))
    student_class = str(input("\nEnter class: "))
    admission_number = str(input("\nEnter admission number: "))
    percentage = int(input("\nEnter percentage (only number): "))
    attendance = int(input("\nEnter attendance (only number): "))
    age = int(input("\nEnter age: "))
    gender = str(input("\nEnter 'M' for male, 'F' for female and 'O' for others: "))

    # cur.execute("""INSERT INTO students(Student_ID, Name, Class, Admission_Number, Percentage, Attendance, Age, Gender)
    #     VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    #     """)
    return (student_id, name, student_class, admission_number, percentage, attendance, age, gender)

def edit_details(cur):
    identify = str(input("\nWhose details you want to edit? (enter his/her Student ID): "))
    cur.execute("""SELECT name FROM students WHERE Student_ID = %s""", (identify,))
    holder_name = cur.fetchone()
    edit = str(input(f"\nwhat do you want to edit in {holder_name}'s details: "))
    if edit in ["Student_ID", "Name", "Class", "Admission_Number", "Percentage", "Attendance", "Age", "Gender"]:
        new = input(f"\nEnter new value for {edit}: ")
        cur.execute(f"""UPDATE students SET {edit} = %s WHERE Student_ID = %s""", (new, identify,))
    return (identify, holder_name, edit)

def read(cur):
    identify = str(input("\nWhose details you want to read? (enter his/her Student ID): "))
    cur.execute("""SELECT * FROM students WHERE Student_ID = %s;""", (identify,))
    details = cur.fetchall()
    print(details)

def remove_details(cur):
    identify = str(input("\nWhose details you want to delete? (enter his/her Student ID): "))
    cur.execute("""DELETE FROM students WHERE Student_ID = %s""", (identify,))
    print("\nStudent deleted.")

with psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres",
password = 32134, port = 5432) as connect:
    with connect.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS students(
                    Student_ID INT PRIMARY KEY,
                    Name VARCHAR(255),
                    Class VARCHAR(10),
                    Admission_Number VARCHAR(10),
                    Percentage INT,
                    Attendance VARCHAR(10),
                    Age INT,
                    Gender CHAR
);
""")    
        # Run these one by one to avoid unexpected errors. You can also use Match Case or if else statements to let user decide what to do.
        # e = enter_details()
        # cur.execute("""INSERT INTO students(Student_ID, Name, Class, Admission_Number, Percentage, Attendance, Age, Gender)
        # VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
        # """, e)

        # read(cur)
        # edit_details(cur)
        # remove_details(cur)
    connect.commit()