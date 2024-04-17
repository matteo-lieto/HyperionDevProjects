# Function to register students for an exam
def register_students():
    # Ask the user for the number of students to register
    num_students = int(input("How many students are registering? "))

    # Open or create reg_form.txt in write mode
    with open("reg_form.txt", "w") as file:
        for _ in range(num_students):
            # Prompt for each student's ID number
            student_id = input("Enter the next student ID number: ") + ("." * 30)

            # Write the student ID to the file
            file.write(f"{student_id}\n")
            
            # Write a series of dots (simulated dotted line) for signing
            file.write("." * 30 + "\n")  # Ensure this line is executed

    print("Registration complete. IDs have been saved to reg_form.txt.")

# Directly calling the main function
register_students()
