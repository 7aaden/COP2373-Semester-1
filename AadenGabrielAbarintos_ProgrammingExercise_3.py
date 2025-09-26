# AadenGabrielAbarintos_ProgrammingExercise_2.py
# This program asks the user for a list of their monthly
# expenses as well as the type of expense, and the total amount
# of the expense. The program then analyzes the list and displays
# the total expense, highest expense, and the lowest expense.

# Import the functools module
import functools

# Define the main function.
def main():

    # Create an empty dictionary of expenses
    expenses = []

    # Ask the user for their list of their monthly expenses.
    print("Please list your monthly expenses below.")

    # Create a While loop to ask the user for their
    # until they type "done".
    while True:

        # Ask the user for one of their expenses.
        expense_type = input("Enter the type of expense here "
        "(type done when finished listing your expenses): "
        )

        # If the user inputs done, end the while loop.
        if expense_type.lower() == "done":
            break
        
        # Ask the user for the amount of their specific expense.
        try:
            expense_amount = float(input(
                f"Enter the amount for {expense_type} here: $"
            ))

            # Add the data to the dictionary
            expenses.append(expense_type, expense_amount)

        # Raise a value error if they do not input a number.
        except ValueError:
            print("Invalid input. Please input a number.")
    
    # If the user did not enter any expenses then return.
    if not expenses:
        print("No expenses entered.")
        return
    
# Calculate the total expense

# Calculate the highest expense

# Calculate the lowest expense

    # Display the results
    print ("Expense Report: ")
    print()
    print("Total Expenses: ")
    print("Highest Expense: ")
    print("Lowest Expense: ")


# Run the main function
main()





