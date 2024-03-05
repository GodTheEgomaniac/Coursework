### --- OOP Email Simulator --- ###
from string import punctuation
# --- Email Class --- #
class Email:

    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):

        self.has_been_read = True

# --- Variables/Constants --- #
ERROR_MARKER = "\t!!!\t"

# --- Lists --- #
inbox = [] # Empty list to store emails

# --- Functions --- #
def input_check(input):
    """Checks if user input is convertable to int or float"""
    # First checks if input is int to prevent every int being assigned float
    if input.isnumeric():
        return int(input)
    elif input.replace(".","").isnumeric():
        return float(input)
    else:   # Returns input otherwise input would become NoneType
        return input


def populate_inbox():
    """Creates 3 sample emails and adds them to the Inbox list"""

    email_1 = Email("something@gmail.com", "Welcome", "Content of 1")
    inbox.append(email_1)
    email_2 = Email("someone@gmail.com", "Subject of 2", "Content of 2")
    inbox.append(email_2)
    email_3 = Email("address@hotmail.com", "Subject of 3", "Content of 3")
    inbox.append(email_3)


def list_emails():
    """Displays list of emails using their subjects with a number"""

    email_subjects = []
    for i in inbox:
        email_subjects.append(i.subject_line)
    email_subjects = enumerate(email_subjects)

    print("Inbox: ")
    for i in email_subjects:
        print(str(i).strip(punctuation).replace(",", " ->").replace("'", ""))


def read_email(index):
    """Displays an email and marks it as read"""

    # Error checking
    index = input_check(index)
    if type(index) != int:
        return print(f"{ERROR_MARKER}Please enter a number{ERROR_MARKER}")
    elif index > len(inbox):
        return print(f"{ERROR_MARKER}Please enter a number from the options listed{ERROR_MARKER}")
    
    print(f"""\nFrom {inbox[index].email_address}\t{inbox[index].subject_line}\n
{inbox[index].email_content}
""")
    # Marking email as read
    inbox[index].mark_as_read()
    print("\nEmail now marked as read\n")


# --- Email Program --- #
populate_inbox() # Ensures inbox never empty

while True:
    user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
    # Added additional error handling
    if user_choice.isnumeric():
        user_choice = int(user_choice)
    else:   # Error Message
        print(f"{ERROR_MARKER}Please enter a number corresponding to the options{ERROR_MARKER}")


    if user_choice == 1:
        list_emails()
        read_email(input("Select which email to read: "))
        
        
    elif user_choice == 2:
        unread_inbox = []
        for email in inbox:
            if email.has_been_read == False:
                unread_inbox.append(email)
        
        for e in unread_inbox:
                print(e.subject_line)

    elif user_choice == 3:
        exit("Closing Application")

    else:   # Error Message
        print(f"{ERROR_MARKER}Please enter a number corresponding to the options{ERROR_MARKER}")
