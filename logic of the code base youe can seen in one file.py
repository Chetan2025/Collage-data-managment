class Collage:
    def __init__(self, lst):
        self.name = lst[0]
        self.add = lst[1]
        self.mob = lst[2]
        self.roll = lst[3]
        self.sub = lst[4] if len(lst) > 4 else None
        self.cgpa = lst[5] if len(lst) > 5 else None

    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Mobile: {self.mob}")
        print(f"Address: {self.add}")
        if self.sub:
            print(f"Subject: {self.sub}")
        if self.cgpa:
            print(f"CGPA: {self.cgpa}")
        print("-----------------------------")


# Main Program Starts
print("Hello, welcome to collage data management....!")

dic = {}
while True:
    type = int(input("""enter the type of work  
                     1.adding data 
                     2. display data
                     3. To stop  (pres the no. only...): \t """))
    if type == 3 :
        print("Thankyou for use our softwere...")
        break
    elif type == 1:
        while True:
            section = input(f"""\nEnter the section: 
        (existing sections are: {list(dic.keys())})
        If create a new section then press -> 'n' <-: """).strip()

            if section.lower() == "n":
                x = input("Enter the new section name: ").strip().capitalize()
                if x not in dic:
                    dic[x] = {}  
                    print(f"Section '{x}' added successfully!")
                else:
                    print(f"Section '{x}' already exists.")
                continue 

            section = section.capitalize()
            if section not in dic:
                print(f"Section '{section}' does not exist. Please create it first by pressing 'n'.")
                continue  # Ask for section again

            # Student Data Input Block
            name = input("Enter Name: \t")
            roll = input("Enter Roll No.: \t")

            if roll in dic[section]:
                print(f"Roll No. {roll} already exists in section {section}.")
                continue

            add = input("Enter Address: \t")
            mob = input("Enter Mobile Number: \t")
            sub = input("Enter Subject (Optional, press Enter to skip): \t")
            cgpa = input("Enter CGPA (Optional, press Enter to skip): \t")

            data = [name, add, mob, roll]
            if sub:
                data.append(sub)
            if cgpa:
                data.append(cgpa)

            student = Collage(data)
            dic[section][roll] = student  # Store object with Roll No. as key

            #for the stop the ..block of code
            cont = input("Do you want to add another student? (y/n): ").strip().lower()
            if cont != 'y':
                break


    elif type == 2:
    # Search & Display Options
        while True:
            type_of_display = int(input("""\nEnter the printing data type:
            1. Print all student data of a section
            2. Print data of a specific student (Section + R5oll No.)
            3. Exit
            Enter your choice: """))

            if type_of_display == 1:
                sec = input("Enter Section Name: ").strip().capitalize()
                if sec in dic:
                    print(f"\n--- Students in Section {sec} ---")
                    if not dic[sec]:
                        print("  No students in this section.")
                    else:
                        for roll_no, student_obj in dic[sec].items():
                            student_obj.display_data()
                else:
                    print(f"Section '{sec}' does not exist.")

            elif type_of_display == 2:
                sec = input("Enter Section Name: ").strip().capitalize()
                roll = input("Enter Roll No: ").strip()
                if sec in dic and roll in dic[sec]:
                    print(f"\nStudent found in Section {sec}:")
                    dic[sec][roll].display_data()
                else:
                    print("Student not found. Please check Section and Roll No.")

            elif type_of_display == 3:
                break

            else:
                print("Enter the correct option (1, 2, or 3).")
    else:
        print("Enter the correct option (1, 2, or 3).")



        