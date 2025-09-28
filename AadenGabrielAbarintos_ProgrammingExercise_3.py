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
            expenses.append({"type": expense_type, "amount": expense_amount})

        # Raise a value error if they do not input a number.
        except ValueError:
            print("Invalid input. Please input a number.")
    
    # If the user did not enter any expenses then return.
    if not expenses:
        print("No expenses entered.")
        return
    
    # Calculate the total expense
    total_expenses = functools.reduce(
        lambda acc, x: acc + x["amount"], expenses, 0
        )

    # Calculate the highest expense
    highest_expense = functools.reduce(
        lambda acc, x: x if x["amount"] > acc["amount"] else acc, expenses
        )

    # Calculate the lowest expense
    lowest_expense = functools.reduce(
        lambda acc, x: x if x["amount"] < acc["amount"] else acc, expenses
        )

    # Display the results
    print ("Expense Report: ")
    print()

    # Print the total expenses
    print(f"Total Expenses: ${total_expenses:.2f}")
    
    # Print the highest expense
    print("Highest Expense: "
        f"{highest_expense['type']}, ${highest_expense['amount']:.2f}"
    )

    # Print the lowest expense
    print("Lowest Expense: "
        f"{lowest_expense['type']}, ${lowest_expense['amount']:.2f}"
    )

# Run the main function
main()





