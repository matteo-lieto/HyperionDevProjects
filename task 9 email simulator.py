### --- OOP Email Simulator --- ###

# --- Email Class --- #
class Email:
    # Class variable to indicate if the email has been read; default is False for all instances
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        # Initialise the instance variables for emails
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        # Method to change 'has_been_read' from False to True
        Email.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects
inbox = []

# --- Functions --- #
def populate_inbox():
    # Create 3 sample emails and add them to the Inbox list
    inbox.append(Email("sender1@example.com", "Welcome to our service!", "Thank you for joining us."))
    inbox.append(Email("sender2@example.com", "Check out our new features!", "We have updated our service."))
    inbox.append(Email("sender3@example.com", "Your account details", "Please update your account information."))

def list_emails():
    # Function which prints each email’s subject_line, along with a corresponding number
    for index, email in enumerate(inbox):
        read_status = "(Read)" if email.has_been_read else "(Unread)"
        print(f"{index} {email.subject_line} {read_status}")

def read_email(index):
    # Function which displays a selected email and marks it as read
    if index < len(inbox) and index >= 0:
        email = inbox[index]
        email.mark_as_read()
        print(f"\nEmail from {email.email_address}:")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}\n")
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("Invalid email index.")

# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program
populate_inbox()

# Fill in the logic for the various menu operations
while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application
    Enter selection: '''))
    
    if user_choice == 1:
        # Logic to read an email by displaying it and marking it as read
        list_emails()
        email_index = int(input("Enter the email index to read: "))
        read_email(email_index)
       
    elif user_choice == 2:
        # Logic to view unread emails
        print("\nListing all unread emails:")
        for email in inbox:
            if not email.has_been_read:
                print(f"Subject: {email.subject_line} - Unread")

    elif user_choice == 3:
        # Logic to quit the application
        print("Quitting application.")
        break

    else:
        # Handle incorrect input
        print("Invalid input, please enter a valid option.")
