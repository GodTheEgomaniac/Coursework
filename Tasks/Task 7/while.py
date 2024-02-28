#save input variable with starting value 0
#save total variable with starting value 0
#save iteration variable with starting value 0
#while input is not -1:
    #ask user to input a new value for variable
    #convert input from string to float or integer
    #if input is not -1:
        #add the input value to the total value
        #increase iteration value by 1
#calculate and print the average

new_input=0
total=0
iteration=0
print("\nThis program will give you the mean average of all the \
numbers you enter.\nEntering '-1' will make this program stop asking \
for inputs and calculate the mean.\n")
while new_input!=-1:
    new_input=input("Enter '-1' to calculate mean.\nEnter new number: ")
    new_input=float(new_input)
    if new_input!=-1:   #makes sure -1 isn't part of the end result
        total+=new_input
        iteration+=1
print("The mean of all your inputs: " +str(total/iteration))