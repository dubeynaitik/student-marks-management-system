
# student marks management system

print('''
================================
  STUDENT MARKS MANAGEMENT
================================
''')

students = {}

while True:
    print('''WHAT DO U WANT

1:- add student marks
2:- view result
3:- exit
''')

    user = input("ENTER YOUR CHOICE :- ").lower()

    if user == "1" or user == "add student marks":

        student_name = input("ENTER A STUDENT NAME :- ").strip().capitalize()

        if not student_name:
            print("PLEASE ENTER A STUDENT NAME!")
            continue

        student = {}
        student["NAME"] = student_name

        try:
            total_subjects = int(
                input("ENTER A TOTAL NUMBER OF SUBJECTS :- ")
            )

            if total_subjects <= 0:
                print("PLEASE ENTER AT LEAST ONE SUBJECT!")
                continue

        except ValueError:
            print("PLEASE ENTER A VALID NUMBER!")
            continue

        for i in range(total_subjects):
            subject_name = input("ENTER A SUBJECT NAME :- ").strip().capitalize()

            if not subject_name or subject_name == "Name":
                print("PLEASE ENTER A VALID SUBJECT NAME!")
                continue

            if subject_name in student:
                print("SUBJECT ALREADY EXISTS! ENTER IT AGAIN.")
                continue

            try:
                subject_marks = int(input("ENTER SUBJECT MARKS (0-100) :- "))

                if subject_marks < 0 or subject_marks > 100:
                    print("MARKS MUST BE BETWEEN 0 AND 100!")
                    continue

            except ValueError:
                print("PLEASE ENTER VALID NUMERIC MARKS!")
                continue

            student[subject_name] = subject_marks

        if len(student) - 1 != total_subjects:
            print("STUDENT RECORD INCOMPLETE. PLEASE ADD THE STUDENT AGAIN.")
            continue

        students[student_name] = student

        print("\n" + "_" * 30)
        print("STUDENT NAME:", student["NAME"])
        print("-" * 30)
        print(f"{'Subject Name':<20} {'Marks':>8}")
        print("-" * 30)

        total = 0
        passed = True

        for subject_name, subject_marks in student.items():
            if subject_name != "NAME":
                print(f"{subject_name:<20} {subject_marks:>8}")
                total = total + subject_marks

                if subject_marks < 33:
                    passed = False

        maximum_marks = total_subjects * 100
        percentage = (total / maximum_marks) * 100

        if not passed:
            grade = "F"
            result = "FAIL"
        elif percentage >= 90:
            grade = "A+"
            result = "PASS"
        elif percentage >= 80:
            grade = "A"
            result = "PASS"
        elif percentage >= 70:
            grade = "B"
            result = "PASS"
        elif percentage >= 60:
            grade = "C"
            result = "PASS"
        elif percentage >= 45:
            grade = "D"
            result = "PASS"
        else:
            grade = "E"
            result = "PASS"

        print("_" * 30)
        print("TOTAL MARKS:", total, "/", maximum_marks)

        print("_" * 30)
        print("PERCENTAGE:", round(percentage, 2), "%")

        print("_" * 30)
        print("GRADE:", grade)

        print("_" * 30)
        print("RESULT:", result)

        print("_" * 30)

    elif user == "2" or user == "view result":

        search_name = input("ENTER STUDENT NAME :- ").strip().capitalize()

        if search_name in students:
            student = students[search_name]

            print("\n" + "_" * 30)
            print("STUDENT NAME:", student["NAME"])
            print("-" * 30)
            print(f"{'Subject Name':<20} {'Marks':>8}")
            print("-" * 30)

            total = 0
            subject_count = 0
            passed = True

            for subject_name, subject_marks in student.items():
                if subject_name != "NAME":
                    print(f"{subject_name:<20} {subject_marks:>8}")
                    total = total + subject_marks
                    subject_count = subject_count + 1

                    if subject_marks < 33:
                        passed = False

            maximum_marks = subject_count * 100
            percentage = (total / maximum_marks) * 100

            if not passed:
                grade = "F"
                result = "FAIL"
            elif percentage >= 90:
                grade = "A+"
                result = "PASS"
            elif percentage >= 80:
                grade = "A"
                result = "PASS"
            elif percentage >= 70:
                grade = "B"
                result = "PASS"
            elif percentage >= 60:
                grade = "C"
                result = "PASS"
            elif percentage >= 45:
                grade = "D"
                result = "PASS"
            else:
                grade = "E"
                result = "PASS"

            print("_" * 30)
            print("TOTAL MARKS:", total, "/", maximum_marks)

            print("_" * 30)
            print("PERCENTAGE:", round(percentage, 2), "%")

            print("_" * 30)
            print("GRADE:", grade)

            print("_" * 30)
            print("RESULT:", result)

            print("_" * 30)

        else:
            print("STUDENT NOT FOUND!")

    elif user == "3" or user == "exit":
        print("THANK YOU FOR USING STUDENT MARKS MANAGEMENT!")
        break

    else:
        print("INVALID CHOICE! PLEASE SELECT 1, 2 OR 3.")
