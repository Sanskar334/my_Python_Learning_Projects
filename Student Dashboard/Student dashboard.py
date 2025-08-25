import json
class Student_details:
    def __init__(self, name, id, course, grade, attendance):
        self.student_name = name
        self.student_id = id
        self.course_enrolled = course
        self.grade = grade
        self.attendance_percentage = attendance

    def save_to_dictionary(self):
        return {
            "Name": self.student_name,
            "ID": self.student_id,
            "Course": [self.course_enrolled],
            "Grade": self.grade,
            "Attendance": f"{self.attendance_percentage}%"
        }
    
class Input_details:
    def save_student(self, student):
        try:
            with open("student_details.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("File not found, creating a new one.")
            data = []
        data.append(student.save_to_dictionary())

        with open("student_details.json", "w") as file:
            json.dump(data, file, indent=4)

    def student_input(self):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        course = input("Enter course enrolled: ")
        grade = input("Enter grade: ")
        attendance = input("Enter attendance percentage: ")

        details = Student_details(name, id, course, grade, attendance)
        self.save_student(details)

    def delete_student(self):
        id = input("Enter student ID to delete: ")
        with open("student_details.json", "r") as file:
            data = json.load(file) # load is use to read a json file
            if id in [student['ID'] for student in data]:
                data = [student for student in data if student['ID'] != id]
                with open("student_details.json", "w") as file:
                    json.dump(data, file, indent=4) # dump is used to write a json file.
                print(f"Student with ID {id} deleted.")


class Read_JSON:
    def __init__(self): # Because I want this to get executed automatically.
        with open ("student_details.json", "r") as file:
            data = json.load(file)
            for student in data:
                print(f'''Name: {student['Name']}
    ID: {student['ID']}
    Course: {student['Course']}
    Grade: {student['Grade']}
    Attendance: {student['Attendance']}
    ''')
            # print(data[0])
            # print(data[0]['Name'])

dashboard_input = Input_details()
# dashboard_input.student_input()
dashboard_input.delete_student()

# Read_JSON()