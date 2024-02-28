# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" #SyntaxError: String needs to be surrounded by quotation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  #LogicalError: Incorrect placement of variables in f-string
                                                                                            #SyntaxError: F-string need an 'f' before the quotations

print(full_spec) #SyntaxError: Print function requires parentheses