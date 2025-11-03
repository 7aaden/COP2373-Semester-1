# AadenGabrielAbarintos_ProgrammingExercise_9.py
# This program creates a class that contains the name,
# account number, amount, and interest rate of an account.
# The class then supports methods for adjustng the interst rate,
# for withdrawing, depositing, and for giving a balance.


# Create the BankAcct Class.
class BankAcct:


    # Initialize all account attributes.
    def __init__(self, name, acct_number, amount, interest_rate):
        self.name = name
        self.acct_number = acct_number
        self.amount = amount
        self.interest_rate = interest_rate
        self.last_interest_calc = 0.0


    # Create the method to change the interest rate.
    def adjust_interest_rate(self, new_rate):

        # Make sure the new interest rate is greater than 0.
        if new_rate < 0:
            print("Interest rate cannot be negative.")
            return

        # Display the new interest rate.
        self.interest_rate = new_rate
        print(f"Interest rate updated to {new_rate * 100:.2f}%.")


    # Create the method to deposit money into the account.
    def deposit(self, amount):

        # Make sure the deposit amount is positive.
        if amount <= 0:
            print("The deposit amount must be positive.")
            return

        # Update the balance of the account.
        self.amount += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.amount:.2f}")


    # Create the method to withdraw money from the account.
    def withdraw(self, amount):

        # Make sure the withdrawal is more than 0.
        if amount <= 0:
            print("Withdrawal must be positive.")
            return

        # Make sure the withdrawal is less
        # than the total account value.
        if amount > self.amount:
            print("Insufficient funds. Please try again.")
            return

        # Update the balance of the account.
        self.amount -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.amount:.2f}")


    # Create the method to display the balance of the account.
    def bal(self):

        # Return the balance of the account.
        return self.amount


    # Create the method to calculate the interest of the account.
    def calc_interest(self, days):

        # Caculate the interest.
        interest = self.amount * (self.interest_rate / 365) * days
        self.last_interest_calc = interest

        # Return the interest amount.
        return interest


    # Create the method to format all details into strings.
    def __str__(self):

        # Display account data.
        result = (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.acct_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate * 100:.2f}%"
        )

        # Update the interest rate.
        if self.last_interest_calc > 0:
            result += f"\nLast Calculated Interest: ${self.last_interest_calc:.2f}"

        # Return the account data.
        return result



# Create the test function to verify the methods.
def test():

    print("Testing BankAcct Class")

    # Create a sample bank account.
    acct = BankAcct("Aaden A", "123456789", 1000.00, 0.03)

    # Display the account details.
    print(acct)
    print()

    # Deposit money into the account.
    acct.deposit(500)

    # Display the new details.
    print(acct)
    print()

    # Withdraw money from the account.
    acct.withdraw(200)

    # Display the new details.
    print(acct)
    print()


    # Adjust the interest rate of the account.
    acct.adjust_interest_rate(0.04)

    # Display the new details.
    print(acct)
    print()

    # Test the calcuated interest for 30 days
    days = 30
    acct.calc_interest(days)

    # Display the new details.
    print(acct)

    # End the program.
    print("End of test")



# Run the test function
test()

