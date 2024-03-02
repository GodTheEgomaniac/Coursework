from math import pow

# - __Defining Functions and String Templates__
def input_check(input):
    """Checks if user input is convertable to int or float"""
    # First checks if input is int to prevent every int being assigned float
    if input.isnumeric():
        return int(input)
    elif input.replace(".","").isnumeric():
        return float(input)
    else:   # Returns input otherwise input would become NoneType
        return input

def numeric_error():
    """Prints error message"""
    ERROR_MARKER = "\t!!!\t"    # Noticable and easy to read markers
    print("\n{}Input must be a number{}\n".format(ERROR_MARKER,ERROR_MARKER))

def ask_for_number(msg):
    """Asks for numeric input and handles potential errors"""
    while True:
        num_in = input("{}".format(msg))
        num_in = input_check(num_in)
        if type(num_in) == str:
            numeric_error()
            continue
        else:
            break
    return num_in

def calc_simple(deposit, i_APR, invest_duration):
    """Calculates simple interest"""
    return deposit*(1+(i_APR/100)*invest_duration)

def calc_compound(deposit, i_APR, invest_duration):
    """Calculates compound interest"""
    return deposit*pow((1+(i_APR/100)),invest_duration)

def calc_repayment(b_APR, house_value, bond_duration):
    """Calculates repayment for bond"""
    return ((b_APR/100/12)*house_value)/(1-(1+(b_APR/100/12))**(-bond_duration))

i_template = "__________________________________\n\
Deposit Total:\t\t£{}\n\
Interest Rate:\t\t{}%\n\
Investment Duration:\t{} years\n\n\
End Total:\t\t£{}\n\
__________________________________"

b_template = "__________________________________\n\
Building Value:\t£{}\n\
Interest Rate:\t{}%\n\
Length of Bond:\t{} months\n\n\
Repayment per month: £\t{}\n\
__________________________________"
# - __Main Body__
print("investment - to calculate the amount of interest you'll \
earn on your investment\nbond       - to calculate the \
amount you'll have to pay on a home loan\n\nEnter either \
'investment' or 'bond' from the menu above to proceed:")
# Chose to print in one statement taking advantage of the backslash
calculator = ""
while calculator != "investment" and calculator != "bond":
    calculator = input().lower() # Removes case sensitivity from input

    # - Investment Calculation
    if calculator == "investment":
        deposit = ask_for_number("Deposit Sum: £")
        i_APR = ask_for_number("Interest Rate(%): ")
        invest_duration = ask_for_number("Duration of Investment(Years): ")

        print("Enter whether you want 'simple' or 'compound' interest")
        interest = ""
        while interest != "simple" and interest != "compound":
            interest = input().lower()
            
            if interest == "simple":
                simple = calc_simple(deposit, i_APR, invest_duration)
                print(i_template.format(deposit,i_APR,invest_duration,round(simple,2)))
                
            elif interest == "compound":
                compound = calc_compound(deposit, i_APR, invest_duration)
                print(i_template.format(deposit,i_APR,invest_duration,round(compound,2)))
                
            else:
                print("\nPlease enter a valid option!\nsimple/compound: ")
                continue


    # - Bond Calculation
    elif calculator == "bond":
        house_value = ask_for_number("Value of Building: £")
        b_APR = ask_for_number("Interest Rate(%): ")
        bond_duration = ask_for_number("Planned length of repayment(Months): ")
        repayment = calc_repayment(b_APR, house_value, bond_duration)

        print(b_template.format(house_value,b_APR,bond_duration,round(repayment,2)))

        
    else:
        print("\nPlease enter a valid option!\ninvestment/bond: ")
        continue