# List to store all student records
Students = []

# Starting student ID (auto-incremented)
student_id = 101

# Menu control variable
choice = "-1"

# Main program loop
while choice != "6":
    print("\n--------------------------------------")
    print("Welcome to The Student Data Organizer!")
    print("--------------------------------------\n")

    print("Select an Option ::")
    print("--------------------")
    print("1. Adding the Student")
    print("2. Display all the Students")
    print("3. Update the Student Information")
    print("4. Delete Student")
    print("5. Display the subjects offered")
    print("6. Exit")
    print("--------------------")

    choice = input("Enter your choice: ").strip()

    match choice:

        # Add a new student record
        case "1":
            print("\n------------------------")
            print(f"The Student ID will be {student_id}")

            name = input("Enter the name of Student : ").strip()
            age = int(input("Enter the age of Student : "))
            grade = input("Enter the grade of Student : ").strip()
            dob = input("Enter the birth date (YYYY-MM-DD) : ").strip()

            # Store subjects as a set to avoid duplicates
            subject = {
                item.strip()
                for item in input(
                    "Enter the Subject (Separated by COMMA) : "
                ).split(",")
                if item.strip()
            }

            # Create and save student information
            Students.append({
                "name": name,
                "age": age,
                "grade": grade,
                "ID_DOB": (student_id, dob),
                "subject": subject
            })

            print("\nStudent is Added successfully!")
            print("------------------------\n")

            # Generate next unique student ID
            student_id += 1

        # Display all stored students
        case "2":
            if Students:
                print("\n--------ALL Students--------")

                for student in Students:
                    subjects = ", ".join(sorted(student["subject"]))

                    print(
                        f"Student ID: {student['ID_DOB'][0]} | "
                        f"Name: {student['name']} | "
                        f"Age: {student['age']} | "
                        f"Grade: {student['grade']} | "
                        f"Subjects: {subjects}"
                    )

                print("----------------------------")
            else:
                print("\n----------------------------")
                print("There are no Students in the list")
                print("----------------------------")

        # Update an existing student's information
        case "3":
            print("\n----------------------------")

            input_id = int(input("Enter the id of the Student : "))
            found = False

            for index, student in enumerate(Students):
                if student["ID_DOB"][0] == input_id:
                    found = True

                    print(
                        f"Enter the changes of the Student named {student['name']}"
                    )

                    age = int(
                        input("Enter the age of Student to Update : ")
                    )
                    grade = input(
                        "Enter the grade of Student to Update : "
                    ).strip()

                    subject = {
                        item.strip()
                        for item in input(
                            "Enter the Subject (Separated by COMMA) : "
                        ).split(",")
                        if item.strip()
                    }

                    # Update selected fields
                    Students[index]["age"] = age
                    Students[index]["grade"] = grade
                    Students[index]["subject"] = subject

                    print("The Student is Updated successfully!")
                    print("----------------------------")
                    break

            if not found:
                print("The Student ID is invalid!")
                print("Enter the Student ID properly")
                print("----------------------------")

        # Delete a student record by ID
        case "4":
            print("\n----------------------------")

            input_id = int(input("Enter the id of Student to Delete : "))
            found = False

            for index, student in enumerate(Students):
                if student["ID_DOB"][0] == input_id:
                    found = True

                    print(
                        f"Are you sure to delete the student {student['name']}"
                    )

                    choose = input("Yes / No : ").strip()

                    if choose.lower() == "yes":
                        del Students[index]
                        print("Student is deleted")
                    else:
                        print("Deletion cancelled")

                    print("----------------------------")
                    break

            if not found:
                print("The Student ID is invalid!")
                print("Enter the Student ID properly")
                print("----------------------------")

        # Display all unique subjects offered
        case "5":
            if Students:
                subs = set()

                # Collect subjects from all students
                for student in Students:
                    subs.update(student["subject"])

                print("\n--------ALL Subjects--------")
                print(", ".join(sorted(subs)))
                print("----------------------------")
            else:
                print("There are no students in list")
                print("----------------------------")

        # Exit the application
        case "6":
            print("\nGoodByeeee!")
            print("----------------------------")
            break

        # Handle invalid menu choices
        case _:
            print("Enter the valid input!")
            print("----------------------------")
