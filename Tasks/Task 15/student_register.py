FILLER = "_"*10
print(FILLER + "Student Registering Service"+ FILLER + "\n")

# while loop to ensure no errors occur due to misinput
while True:
    student_n = input("Enter amount of students: ")
    if student_n.strip().isnumeric() == False:
        print("Input a whole number!\n")
        continue
    break

# Writes to file IDs for specified amount of students
with open("reg_form.txt", "w") as file:
    for student_ID in range(int(student_n)):
        student_ID = input("Enter Student's ID number: ")
        file.write(student_ID + "."*30 + "\n")