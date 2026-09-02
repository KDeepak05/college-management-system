students = []

def add_student(name):
    students.append(name)
    print(f"Student {name} added.")

def display_students():
    if not students:
        print("No students in the list.")
    else:
        print("List of students:")
        for student in students:
            print(student)

def search_student(name):
    if name in students:
        print(f"Student {name} found.")
    else:
        print(f"Student {name} not found.")

