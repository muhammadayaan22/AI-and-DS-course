print("------ STUDENT RECORDS (Using List of Dictionaries) -------")

records = []

# 1. Add student
def add_student():
    name = input("Enter your name: ")
    roll_no = input("Enter your roll number: ")   # keep as string for easy comparison
    course = input("Enter your course: ")
    marks = int(input("Enter your marks: "))

    student = {
        "name": name,
        "roll_no": roll_no,
        "course": course,
        "marks": marks
    }

    records.append(student)
    print("Record saved!!!!")

# 2. Display students
def display_student():
    if records:
        print("-------------------")
        print("Students records")
        print("-------------------")
        for student in records:
            print(f"Name: {student['name']}")
            print(f"Roll no: {student['roll_no']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            print("-------------------")
    else:
        print("No records found!!!")

# 3. Search student
def search_student():
    if records:
        roll_no = input("Enter roll number to search: ")

        for student in records:
            if roll_no == student['roll_no']:
                return student   # ✅ return only the student record
        return None             # if not found
    else:
        print("No records found!!!")
        return None

# 4. Update student
def update_student():
    student = search_student()
    if student is not None:
        new_marks = int(input("Enter new marks: "))
        student['marks'] = new_marks
        print("Marks updated successfully!!!")
    else:
        print("Record not found!!!")

# 5. Delete student
def delete_student():
    student = search_student()
    if student is not None:
        records.remove(student)
        print("Record deleted successfully!!!")
    else:
        print("Record not found!!!")

# 6. Sort students
def sort_students():
    if records:
        sorted_list = sorted(records, key=lambda x: x['marks'], reverse=True)
        print("------ Sorted Students ------")
        for student in sorted_list:
            print(f"Name: {student['name']}, Roll no: {student['roll_no']}, "
                  f"Course: {student['course']}, Marks: {student['marks']}")
        print("----------------------------------------")
    else:
        print("No records found!!!")

# ----------------- MENU -----------------
while True:
    print("\n---------------------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students")
    print("7. Exit")
    print("----------------------")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_student()
    elif choice == '3':
        student = search_student()
        if student is not None:
            print("------ Student Found -----")
            print(f"Name: {student['name']}")
            print(f"Roll no: {student['roll_no']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
        else:
            print("Record not found!!!")
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        sort_students()
    elif choice == '7':
        print("Thankyou!!")
        break
    else:
        print("Invalid Choice.")
