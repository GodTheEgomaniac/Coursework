#Brendan's Favourite snacks

#save product information as tuple(s)

cookies=("Triple Chocolate Cookies","Cookies containing a\
combination of Milk, White, and Dark Chocolate.","£1.80")
sweets=("Haribo Tangfastics","Soft gelatin-based sweets\
coated in sugar with a tangy taste.","£1.25")
drink=("Innocent Strawberries Pineapple and Apples Smoothie","\
Blended fruits and juices combined into a sweet mixture \
with a smooth texture.", "£3.00")
savoury=("Mini Babybel Light", "Small, round pieces of cheese\
perfect for a lunchbox, coated in a layer of peelable \
red wax.","£2.10")
snacks=(cookies,sweets,drink,savoury)
def display():
    longest=0
    for i in snacks:
        if len(i) > longest:
            longest=len(i)
    print(display_template)

#Main Body
#While loop to ensure valid input
while True:
    print("To see information on Brendan's favourite snacks")
    user_selection=input("Enter 'cookies', 'sweets', 'drink',\
 or 'savoury':")
    if user_selection not in ["cookies","sweets","drink","savoury"]:
        print("Enter a valid option")
    else:
        break


    
#Template to print any selection in the same format
longest=0
display_template=f"{"_"*longest}\n\
Name: {snacks[0]}\n\
Description: {snacks[1]}\n\
Price: {snacks[2]}\n\
{"_"*longest}" #Undefined Variable until later. Syntax and Logical Error


if snacks=="cookies":
    snacks=cookies
    display


elif snacks=="sweets":
    snacks=sweets
    display

elif snacks=="drink":
    snacks=drink
    display

elif snacks=="savoury":
    snacks=savoury
    display
