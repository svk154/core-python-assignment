class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
    
def calculate_average_marks(students):
    average_marks = {}
    for name, marks in students.items():
        student = Student(name, marks)
        average_marks[name] = student.calculate_average()
    return average_marks

def find_top_performer(students):
    top_student = None
    highest_average = -1
    
    for name, marks in students.items():
        student = Student(name, marks)
        average = student.calculate_average()
        if average > highest_average:
            highest_average = average
            top_student = name
    
    return top_student

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}

average_marks = calculate_average_marks(students)
print(f"Average Marks: {average_marks}")

top_performer = find_top_performer(students)
print(f"Top Performer: {top_performer}")
