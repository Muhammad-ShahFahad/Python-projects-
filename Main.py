student={}


def add_student():#Enter name and id of the student
    try:
        roll_id=int(input("Enter id of the student"))
    except ValueError:
        print("plz enter valid number")
        return add_student()
    if roll_id in student:
        print("id is already existed")
        return 
    name=input("Enter name of the student").upper()
    student[roll_id]={"Name":name}
    print(f"Student name:{name} and id:{roll_id} Added successfully")

def add_subject():#Enter how many subject and there name 
    try:
        roll_id=int(input("Enter id of the student"))
    except ValueError:
        print("Plz enter correct id")
        return
    if roll_id not in student:
        print("Student with this id not existed")
        return
    
    try:
         number_subject=int(input("Enter number of subject you want to enroll student"))
    except ValueError:
        print("Please Enter number")
        return
    if"Subject"not in student[roll_id]:
        student[roll_id]["Subject"]={}
    
    for i in range (number_subject):
        subject_name=input("Enter name of the subjects").upper()
        if subject_name in student[roll_id]["Subject"]:
            print(f"The Subject{subject_name}is already in subject")
        else:
            student[roll_id]["Subject"][subject_name]=None
            print("Subjects added sucessfully")
        
    

def add_marks():#Enter marks of the students
    try:
        roll_id=int(input("Enter id of the student"))
    except ValueError:
        print("Plz enter correct id")
        return
    if roll_id not in student:
        print("Student with this id not existed")
        return
    subject_name=input("Enter name of the subjects").upper()
    if subject_name not in student[roll_id]["Subject"]:
        print(f"Student is not enrolled in{subject_name}Subject ")
        return 
    try:
        marks=int(input(f"Enter mark of {subject_name} Subject"))
        
    except ValueError:
        print("Please Enter valid marks")
        return
    student[roll_id]["Subject"][subject_name]=marks
    print(f"Marks of{subject_name} entered successfully")

def add_grade(roll_id):#calculate and assign the grade of the studnets
    if not student[roll_id]["Subject"]:
        return "N/A"
    total=0
    count=0
    for marks in student[roll_id]["Subject"].values():
        if marks is not None:
            total+=marks
            count+=1
    if count==0:
        return "No marks entered"

    average=total/count
    if average>=90:
        Grade="A"
        
    elif average>=80:
        Grade="B"
        
    elif average>=70:
        Grade="C"
        
    elif average>=60:
        Grade="D"
        
    elif average<60:
        Grade="F"
        

    student[roll_id]["Grade"]=Grade
    return Grade

def result_into_file(roll_id):#save result in txt file 
    if roll_id not in student:
        print("This student not existed")
        return
    data=student[roll_id]

    with open("Student_result.txt","a") as file:
        file.write(f"Student id:{roll_id}\n")
        file.write(f"Name:{data['Name']}\n")

        if "Subject"in data:
            for subject,marks in data["Subject"].items():
                file.write(f"{subject}:{marks}\n")
        grade=add_grade(roll_id)
        file.write(f"final grade{grade}")



while True:
   print("menue")
   print("Enter 1 to add stuent :")
   print("Enter 2 to add subjets")
   print("Enter 3 to add marks")
   print("Enter 4 to show result")
   print("Enter 5 to save result")
   print("Enter 6 to exit")

   choice=int(input("Enter your choice"))
  
   if choice == 1:
        add_student()

   elif choice == 2:
        add_subject()

   elif choice == 3:
        add_marks()

   elif choice == 4:
        try:
            roll_id = int(input("Enter Student ID: "))
            if roll_id in student:
                data = student[roll_id]
                print(f"\nID: {roll_id} | Name: {data['Name']}")
                if "Subject" in data and data["Subject"]:
                    for s, m in data["Subject"].items():
                        print(f"{s}: {m}")
                else:
                    print("No subjects enrolled.")
                print(f"Final Grade: {add_grade(roll_id)}")
            else:
                print("Student with this ID does not exist.")
        except ValueError:
            print("Please enter a valid number.")
   elif choice==5:
       try:
           roll_id=int(input("Enter id of the student you want to print"))
           result_into_file(roll_id)
       except ValueError:
           print("Enter valid id")

        
   elif choice == 6:
        print("Program exited")
        break

   else:
        print("Invalid choice")
    

        

    
    

    


