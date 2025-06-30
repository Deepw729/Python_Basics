students = {}

while True:
    print("1. Add student")
    print("2. Update student grade.")
    print("3. Print all student grades.")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(f"{name} already exists with grade {students[name]}. Use choice 2 to update.")
        else:
            grade = input("Enter student grade: ")
            students[name] = grade
            print(f"Added {name} with grade {grade}")
    
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter student grade: ")
            students[name] = grade
            print(f"{name} updated with grade {grade}.")
        else:
            print(f"{name} not found. Use choice 1 to add new student.")
    
    elif choice == "3":
        if not students:
            print("No student data found.")
        else:
            for name, grade in students.items():
                print(f"{name} : {grade}")
    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")


