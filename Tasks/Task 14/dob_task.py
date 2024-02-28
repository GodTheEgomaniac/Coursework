file = open("DOB.txt", "r") # Had some issues with file opening. This should work on reviewers end.
x = []
first_name_list = []
birthdate_list = []

# This loops through all lines in DOB.txt
for line in file:
    x = line.split(None, 2)
    full_name = x[0] + " " + x[1]
    first_name_list.append(full_name)

    birthdate = x[2].strip()
    birthdate_list.append(birthdate)
file.close()

# Displays information in requested format
print("Names: ")
for row in first_name_list:
    print(row)

print("\nBirthdates: ")
for row in birthdate_list:
    print(row)