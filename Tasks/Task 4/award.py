#get input for name
#get input for swimming time
#get input for cycling time
#get input for running time
#calculate overall time in variable
#if time is 100 or less
    #give highest award
#elif time is 105 or less
    #give second highest award
#elif time is 110 or less
    #give third highest award
#otherwise give no award
#make an f-string containing end results in user friendly format
#print the f-string

name=input("Competitors Name: ")
s_time=int(input("Time taken Swimming in Minutes: "))
c_time=int(input("Time taken Cycling in Minutes: "))
r_time=int(input("Time taken Running in Minutes: "))
time=s_time+c_time+r_time;del s_time;del c_time;del r_time

if time<=100:
    award="Provincial Colours"
elif time<=105:
    award="Provincial Half Colours"
elif time<=110:
    award="Provincial Scroll"
else:
    award="no award"

user_output=f"{name} completed the events in {time} minutes \
awarding them {award}."
print(user_output)