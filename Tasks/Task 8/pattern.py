#I've designed this in a way that it works with any Integer value.

#save range stop as variable
#for every value in the range:
   #if the current value is greater than half of the range stop:
      #make current value equal to the range stop - current value
   #print repeatable string*current value

r_stop=10   #Tempted to make this a user input
for i in range(r_stop+1):
   if i>r_stop/2:    #Checking if program is halfway through iterations
      i=r_stop-i
   print("*"*i)