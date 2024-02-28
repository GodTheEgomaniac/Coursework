#Get user to input string
#Make list of even numbers
#Make a variable to count each iteration
#Make variable with a blank string to store iterated letters

#for every character in the input:
    #if the number of iterations is in the even list:
        #change character to uppercase and add to new string
    #else:
        #simply add the character to the new string unchanged
    #Increase the iteration counter by 1

#Print result


LINE = "--------------------------"
print(f"{LINE}\nCase Changer Mk.1\n{LINE}")

user_string = input("Enter a word or phrase: ")
even_list = [x for x in range(len(user_string)) if x % 2==0] 
#The idea behind saving a list of even numbers is so the program
#doesn't have to calculate even numbers every iteration. 
#Won't calculate more evens than it needs.

#Alternating case for characters
def case_char_changer():
    iter_counter = 0
    changed_string = ""

    for i in user_string.lower():
        if iter_counter in even_list:
            changed_string += i.upper()
        else:
            changed_string += i
        iter_counter += 1
    return changed_string

#Alternating case for words
def case_word_changer():    
    sliced = user_string.upper().split()
    iter_counter = 0
    spliced = []
    for i in sliced:
        if iter_counter in even_list:
            i=i.lower()
            spliced.append(i)
        else:
            spliced.append(i)
        iter_counter += 1

    changed_string = " ".join(spliced)
    return changed_string

#Main Body
print("\nChoose whether you would like the cases changed for every word \
or every character.\n")
while True:     #While loop to ensure a valid input
    choice = input("Please enter 'word' or 'character': ")

    if choice.lower() == "word":
        output = case_word_changer()
        break
    elif choice.lower() == "character":
        output = case_char_changer()
        break
    else:
        print("Please enter a valid input!")

print(f"\nI've alternated the case of your input: \n{output}")
