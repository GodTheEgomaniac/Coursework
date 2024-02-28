#print instructions to user
#save user input as a variable converted to lowercase
#if input is investment:
    #ask user for deposit sum
    #ask user for interest rate
    #ask user for their investment duration
    #ask user whether they want simple of compound calculation
    #if simple:
        #calculate simple interest
        #display answer in user-friendly manner
    #elif compound:
        #calculate compound interest
        #display answer in user-friendly manner
    #else user doesnt enter valid option:
        #ask user to enter a valid option
#elif input is bond:
    #ask user for value of their house
    #ask user for interest rate
    #ask user for their planned length of repayment
    #calculate repayment per month
    #output repayment per month in a user friendly way
#else:
    #ask user to enter one of the two options

import math
template="__________________________________\n\
Deposit Total:          £{}\n\
Interest Rate:          {}%\n\
Investment Duration:    {} years\n\n\
End Total:              £{}\n\
__________________________________"

print("investment - to calculate the amount of interest you'll \
earn on your investment\nbond       - to calculate the \
amount you'll have to pay on a home loan\n\nEnter either \
'investment' or 'bond' from the menu above to proceed:")
#Chose to print in one statement taking advantage of the backslash
while True:
    calculator=input().lower()
    #Investment Calculation
    if calculator=="investment":
        deposit=float(input("Deposit Sum: £"))
        i_APR=float(input("Interest Rate(%): "))
        invest_duration=int(input("Duration of Investment(Years): "))

        print("Enter whether you want 'simple' or 'compound' interest")
        while True:
            interest=input().lower()
            if interest=="simple":
                simple=deposit*(1+(i_APR/100)*invest_duration)
                print(template.format(deposit,i_APR,invest_duration,round(simple,2)))
                break
            elif interest=="compound":
                compound=deposit*math.pow((1+(i_APR/100)),invest_duration)
                print(template.format(deposit,i_APR,invest_duration,round(compound,2)))
                break
            else:
                print("\nPlease enter a valid option!\nsimple/compound: ")
                continue
        break

    #Bond Calculation
    elif calculator=="bond":
        house_value=float(input("Value of Building: £"))
        b_APR=float(input("Interest Rate(%): "))
        bond_duration=int(input("Planned length of repayment(Months): "))
        repayment=((b_APR/100/12)*house_value)/(1-(1+(b_APR/100/12))**(-bond_duration))

        print(f"__________________________________\n\
Building Value:      £{house_value}\n\
Interest Rate:       {b_APR}%\n\
Length of Bond:      {bond_duration} months\n\n\
Repayment per month: £{round(repayment,2)}\n\
__________________________________")
        break
        
    else:
        print("\nPlease enter a valid option!\ninvestment/bond: ")
        continue