print("------STUDENT RECORDS-------")

records = []

# 1. Add student
def add_student():
    name = input("Enter your name: ")
    roll_no = input("Enter your roll number: ")
    course = input("Enter your course: ")
    marks = int(input("Enter your marks: "))

    records.append([name, roll_no, course, marks])
    print("Record saved!!!!")

# 2. Display students
def display_student():
    if records:
        print("-------------------")
        print("Students records")
        print("-------------------")
        for record in records:
            print(f"Name: {record[0]}")
            print(f"Roll no: {record[1]}")
            print(f"Course: {record[2]}")
            print(f"Marks: {record[3]}")
            print("-------------------")
    else:
        print("No records found!!!")

# 3. Search student
def search_student():
    if records:
        roll_no = input("Enter roll number to search: ")

        for index, record in enumerate(records):
            if roll_no == record[1]:
                return record   
        return None             
    else:
        print("No records found!!!")
        return None
# 4. Update student
def update_marks():
    if records:
        roll_no = input("Enter roll number to update: ")

        for record in records:
            if roll_no == record[1]:   
                print("---------------------")
                print("Record Found!")
                print("---------------------")
                print(f"Name: {record[0]}")
                print(f"Roll no : {record[1]}")
                print(f"Course : {record[2]}")
                print(f"Marks: {record[3]}")
                print("----------------------")

                new_marks = int(input("Enter marks to update: "))
                record[3] = new_marks  
                print("Record Successfully Updated....")
                return
        print("Record Not Found!")   
    else:
        print("No records found!!!")

#5 . Delete student
def delete_student():
    student = search_student()
    if student is not None:
        records.remove(student)
        print("Record Deleted!")
    else:
        print("Record not found!!!")


#6. Sort
def sort_student():
    if records:
        records.sort(key=lambda x:x[3], reverse=True)
        print("Records Sorted by marks Successfully...")
    else:
        print("Record not found!!!")

# ----------------- MENU -----------------
while True:
    print("---------------------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student ")
    print("6. Sort Students ")
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
            print(f"Name: {student[0]}")
            print(f"Roll no: {student[1]}")
            print(f"Course: {student[2]}")
            print(f"Marks: {student[3]}")
        else:
            print("Record not found!!!")
    elif choice == '4':
        update_marks()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        sort_student()
    elif choice == '7':
        print("Thankyou!")
        break
    else:
        print("Invalid Choice.")
