cities = ["London", "Prague", "Salou", "Whitianga", "Nottingham"]

def hotel_cost(num_nights):
    """Calculates hotel total"""
    PRICE_PER_NIGHT = 33
    h_total = PRICE_PER_NIGHT*num_nights
    return h_total

def plane_cost(city_flight):
    """Calculates flight costs"""
    if city_flight == "London":
        p_total = 120
    elif city_flight == "Prague":
        p_total = 135
    elif city_flight == "Salou":
        p_total = 101
    elif city_flight == "Whitianga":
        p_total = 250
    elif city_flight == "Nottingham":
        p_total = 75
    return p_total

def car_rental(rental_days):
    """Calculates car rental total"""
    DAILY_RENTAL_COST = 40
    c_total = DAILY_RENTAL_COST*rental_days
    return c_total

def holiday_cost(num_nights, city_flight, rental_days):
    """Calculates the total holiday cost"""
    total = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    print(f"""
    Your total holiday cost is: £{total}

    Car Rental Subtotal: {car_rental(rental_days)}
    Hotel Subtotal: {hotel_cost(num_nights)}
    Flight Subtotal: {plane_cost(city_flight)}
    """)


print("Available Holiday Destinations:")
for i in cities:
    print(i, end=" ")
print("\n_________________________________")

# While Loops on user inputs to ensure no errors occur from misinputs
while True:
    city_flight = input("\nWhere are you flying to?\n")
    if city_flight.isalpha():
        if city_flight.capitalize() in cities:
            city_flight = city_flight.capitalize()
            break
        else:
            print("Please enter a valid option.\n")
    else:
        print("Please enter a valid option.\n")

while True:
    num_nights = input("How many nights will you be staying?\n")
    if num_nights.isnumeric():
        num_nights= int(num_nights)
        break
    else:
        print("Please enter a whole number.\n")

while True:
    rental_days = input("How many days do you want to rent a car for?\n")
    if rental_days.isnumeric():
        rental_days = int(rental_days)
        break
    else:
        print("Please enter a whole number.\n")


holiday_cost(num_nights, city_flight, rental_days)
