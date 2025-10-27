# AadenGabrielAbarintos_ProgrammingExercise_CSV.py
# This program allows the user to input information of their students.
# The program allows the user to input their students' first names,
# last names, and three exam grades. The names are inputted as strings
# and the exam grades are inputted as integers.
# The program then reads the file and then displays the data
# in tabular format.

# Import the CSV module
import csv


# Define the get_name function.
def get_name(prompt):

    # Make sure the user does not input any integers
    # for a student's name.
    while True:
        name = input(prompt)
        if any (char.isdigit() for char in name):
            print("Name cannot contain numbers. Please try again.")
        else:

            # Return the student's name.
            return name


# Define the get_grade function.
def get_grade(prompt):

    # Make sure the user does not input any strings
    # for a student's exam scores.
    while True:
        score = input(prompt)
        if any (char.isalpha() for char in score):
            print("Score cannot contain strings. Please try again.")
        else:

            # Return the student's score.
            return int(score)


# Define the write_grades function
def write_grades():

    # Ask the user how many students' information
    #  they want to input.
    while True:
        try:
            num_students = int(input(
                "How many students' information "
                "do you want to input? "
            ))

            # Make sure the amount of students' information
            # the user wants to input is a positive integer.
            if num_students > 0:
                break
            else:
                print("Please enter a positive number" 
                " of students greater than 0."
                )
        
        # Raise a value error if they input anything
        # other than an integer.
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Create the CSV file.
    with open("grades.csv", mode = 'w', newline = "") as file:
        write = csv.writer(file)

        # Write the header row.
        write.writerow([
            "First Name", "Last Name", 
            "Exam 1", "Exam 2", "Exam 3"
            ])

        # Ask the user for their students' information.
        for x in range(num_students):
            first_name = get_name("Enter student's first name: ")
            last_name = get_name("Enter student's last name: ")
            exam1 = get_grade("Enter Exam 1 grade: ")
            exam2 = get_grade("Enter Exam 2 grade: ")
            exam3 = get_grade("Enter Exam 3 grade: ")

            # Write the data into the CSV file.
            write.writerow([first_name, last_name, exam1, exam2, exam3])

    # Tell the user the CSV file has been created.
    print("grades.csv has been created.")


# Define the read_grades function
def read_grades():

        # Open the CSV file.
    with open("grades.csv", mode = "r") as file:

        # Format the file.
        reader = csv.reader(file)
        print(
            f"{'First Name':<12} {'Last Name':<12} "
            f"{'Exam 1':<8} {'Exam 2':<8} {'Exam 3':<8}"
        )

        print("-" * 50)

        # Display the data.
        next(reader)
        for row in reader:
            print(
                f"{row[0]:<12} {row[1]:<12} "
                f"{row[2]:<8} {row[3]:<8} {row[4]:<8}"
            )


# Define the main function
def main():

    # Ask the user whether they would like to
    # read or write into the CSV file.
    while True:
        print("Choose an option:")
        print("1. Enter Student Grades")
        print("2. View Student Grades")
        print("3. Exit.")
        choice = input("Enter 1, 2, or 3: ")

        # Make sure the user inputs a correct choice
        if choice == "1":

            # The user will write into the CSV file.
            write_grades()

        elif choice == "2":

            # The user will read the CSV file.
            read_grades()

        elif choice == "3":
            
            # The user will exit the program.
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")
        print()


# Run the main function
main()
