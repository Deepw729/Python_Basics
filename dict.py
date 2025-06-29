# Defining the dictionary
students = {
    "1" : {"Ram" : "A"},
    "2" : {"Sita" : "C"}
}

# Get input from user
student_id = input("Enter student id: ")
 
# Use get() to access student data
student_data = students.get(student_id)

if student_data:
    print(f"Student {student_id} found. Updating details.")
else:
    print(f"Student {student_id} not found. Adding new student.")
    student_data = {}

# Ask for name and grade
name = input("Enter name: ")
grade = input("Enter grade: ")

# Update student data
student_data["name"] = name
student_data["grade"] = grade

# Save back to dictonary
students[student_id] = student_data

# Display updated dictionary
print("\nUpdated Student Data:")
for sid, data in students.items():
    if isinstance(data, dict) and "name" in data and "grade" in data:
        print(f"ID: {sid}, Name: {data['name']}, Grade: {data['grade']}")
    else:
        print(f"ID: {sid} has invalid or incomplete data: {data}")