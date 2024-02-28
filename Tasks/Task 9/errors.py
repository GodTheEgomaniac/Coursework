# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") #SyntaxError: Missing parentheses
print("\n") #SyntaxError: Incorrect indentation(Line 6, Line 15) and missing parentheses

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" #SyntaxError: Can't define variable with '=='
age = int(age_Str) #RuntimeError: Incompatible characters in 'age_Str' to cast it to integer
print("I'm " + str(age) + " years old.")    #RuntimeError: Can't concatenate integer to string without casting as string
                                            #~LogicalError: Would have contained tautology if 'age_Str' wasn't edited and could have called 'age_str' rather than 'age'

# Variables declaring additional years and printing the total years of age
years_from_now = 3    #LogicalError: Variable does not need to be string
total_years = age + years_from_now  #RuntimeError: Can't add string to integer

print ("The total number of years: " + str(total_years)) #SyntaxError: Missing parentheses
                                                        #RuntimeError: incorrect variable name and needs casting as string
                                                        #LogicalError: Quotations turn variable name into literal string

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 #RuntimeError: Incorrect variable name

print ("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old")   #SyntaxError: Missing parentheses
                                                                                    #RuntimeError: Variable needs casting as string
                                                                                    #LogicalError: Calculation doesn't include extra months

#HINT, 330 months is the correct answer