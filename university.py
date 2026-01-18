from datetime import datetime

student_register = {}
bscs_count = 0
bsen_count = 0
bscs_start_hour = 9  # BSCS tests start at 9:00 AM
bsen_start_hour = 13 # BSEN tests start at 1:00 PM

def register_form():
    name = input("Enter your name: ").strip()
    if not name.isalpha():
        print("Please enter a valid name")
        return

    father_name = input("Enter your father name: ").strip()
    if not father_name.isalpha():
        print("Please enter a valid father name")
        return

    mobile_number = input("Enter mobile number (+xxxxxxxxxxxx): ").strip()
    if not mobile_number.startswith("+") or not mobile_number[1:].isdigit() or len(mobile_number) != 13:
        print("Invalid mobile number")
        return

    try:
        percentage = int(input("Enter your 2nd year percentage: "))
    except ValueError:
        print("Please enter numeric percentage")
        return

    gmail = input("Enter your Email: ").strip().lower()
    if not gmail.endswith("@gmail.com"):
        print("Email must end with @gmail.com")
        return

    program = input("Enter degree program (BSEN / BSCS): ").strip().upper()
    if program not in ["BSEN", "BSCS"]:
        print("Invalid program")
        return

    student_register[name] = {
        "Father_name": father_name,
        "Mobile_number": mobile_number,
        "Email": gmail,
        "Percentage": percentage,
        "Program": program
    }

    # Auto assign roll number and time slot
    assign_roll_number_and_slot(name)

    with open("university.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Father Name: {father_name}\n")
        file.write(f"Phone Number: {mobile_number}\n")
        file.write(f"Email: {gmail}\n")
        file.write(f"Percentage: {percentage}\n")
        file.write(f"Program: {program}\n")
        file.write(f"Roll Number: {student_register[name]['Roll_number']}\n")
        file.write(f"Time Slot: {student_register[name]['Time_slot_start']} - {student_register[name]['Time_slot_end']}\n")
        file.write("-"*30 + "\n")

    print(f"Student {name} registered successfully!")

def assign_roll_number_and_slot(name):
    global bscs_count, bsen_count, bscs_start_hour, bsen_start_hour

    program = student_register[name]["Program"]

    if program == "BSCS":
        bscs_count += 1
        roll = f"CS-{bscs_count:03d}"
        start_time = f"{bscs_start_hour:02d}:00"
        end_hour = bscs_start_hour + 1
        end_time = f"{end_hour:02d}:00"
        bscs_start_hour += 1

    elif program == "BSEN":
        bsen_count += 1
        roll = f"EN-{bsen_count:03d}"
        start_time = f"{bsen_start_hour:02d}:00"
        end_hour = bsen_start_hour + 1
        end_time = f"{end_hour:02d}:00"
        bsen_start_hour += 1

    else:
        print("Invalid program")
        return

    student_register[name]["Roll_number"] = roll
    student_register[name]["Time_slot_start"] = start_time
    student_register[name]["Time_slot_end"] = end_time

    print(f"Roll number assigned: {roll}")
    print(f"Time slot assigned: {start_time} - {end_time}")

def check_for_eligibility():
    name = input("Enter name to check eligibility: ").strip()
    if name not in student_register:
        print("Student not found")
        return

    fname = input("Enter father name: ").strip()
    if student_register[name]["Father_name"].lower() != fname.lower():
        print("Father name not matched")
        return

    percentage = student_register[name]["Percentage"]
    program = student_register[name]["Program"]

    if program == "BSEN" and percentage >= 90:
        print("Eligible for Engineering")
    elif program == "BSCS" and percentage >= 70:
        print("Eligible for Computer Science")
    else:
        print("Sorry, not eligible")

def check_time_slot():
    roll_input = input("Enter your roll number to check your time slot: ").strip().upper()
    found = False

    for name, info in student_register.items():
        if info.get("Roll_number") == roll_input:
            found = True
            start_time = info.get("Time_slot_start")
            end_time = info.get("Time_slot_end")

            if not start_time or not end_time:
                print("No time slot assigned yet.")
                return

            print(f"Your assigned time slot: {start_time} - {end_time}")
            break

    if not found:
        print("Invalid roll number.")

def give_test():
    roll_input = input("Enter your roll number to start test: ").strip().upper()
    found = False

    for name, info in student_register.items():
        if info.get("Roll_number") == roll_input:
            found = True
            start_time = info.get("Time_slot_start")
            end_time = info.get("Time_slot_end")

            if not start_time or not end_time:
                print("No time slot assigned yet. Cannot give test.")
                return

            now = datetime.now().time()
            start_time_obj = datetime.strptime(start_time, "%H:%M").time()
            end_time_obj = datetime.strptime(end_time, "%H:%M").time()

            if start_time_obj <= now <= end_time_obj:
                print(f"Welcome {name}! You can take the test now.")
                # Here you can add actual test questions
            else:
                print(f"Not your time slot. Test allowed between {start_time} and {end_time}.")
            break

    if not found:
        print("Invalid roll number.")

# Menu-driven loop
while True:
    print("\n--- University System Menu ---")
    print("1. Register Student")
    print("2. Check Eligibility")
    print("3. Check Your Time Slot")
    print("4. Give Test")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        register_form()
    elif choice == "2":
        check_for_eligibility()
    elif choice == "3":
        check_time_slot()
    elif choice == "4":
        give_test()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
