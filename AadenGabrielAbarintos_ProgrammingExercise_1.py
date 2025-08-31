# AadenGabrielAbarintos_ProgrammingExercise_1.py
# This program writes a hypothetical application in which
# a cinema sells tickets. Four out of twenty tickets can be sold at a time.
# This program counts how many tickets are sold and the amount of buyers.
# The program ends once all tickets are sold and displays the data.

# Initialize constants (global variables).
TOTAL_TICKETS = 20
MAX_TICKETS_PER_BUYER = 4


# Define the sell_tickets function to handle sales.
def sell_tickets():


    # Initialize tickets_remaining variable to track remaining tickets.
    tickets_remaining = TOTAL_TICKETS

    # Initialize the accumulator variable to count the number of buyers.
    buyers = 0

    # Initialize a while loop to repeatedly ask a customer for
    # how many tickets they want to purchase.
    while tickets_remaining > 0:
        
        # Display how many tickets are available for purchase.
        print(f"\nThere are {tickets_remaining} tickets remaining.")

        # Ask the user how many tickets they would like to purchase.
        try:
            tickets_bought = int(input(
            "How many tickets would you like to buy? "
            "(4 maximum per person): "
            ))
        
        # Raise a value error if the user does not input an integer.
        except ValueError:
            print("Invalid input. Please enter a whole number of tickets.")
            continue

        # Create an if statement to validate whether the purchase is valid.
        if tickets_bought < 1:

            # Check if the user bought at least one ticket.
            print("You must buy at least one ticket. Please try again.")
        
        # Check if the user bought more than the maximum amount per user.
        elif tickets_bought > MAX_TICKETS_PER_BUYER:
            print("The maximum number of tickets per person "
                "available for purchase is 4. Please try again."
            )

        # Check if the user bought more tickets than there are available.
        elif tickets_bought > tickets_remaining:
            print(f"Sorry, there are only {tickets_remaining} "
                "tickets left. Please try again."
            )
        
        # If the purchase is valid count the buyer and 
        # count how many tickets are remaining.
        else:
            tickets_remaining -= tickets_bought
            buyers += 1
            print("Thank you for your purchase. You have bought: " 
                f"{tickets_bought} ticket(s)."
            )
    
    # Return how much people bought tickets and
    # how many tickets are remaining.
    return buyers, TOTAL_TICKETS - tickets_remaining


# Define the main function
def main():
    

    # Call the sell_tickets function within the main function
    total_buyers, tickets_sold = sell_tickets()
    
    # Display the data results
    print()
    print("All tickets have been sold!")
    print(f"Total tickets sold: {tickets_sold}")
    print(f"Total number of buyers: {total_buyers}")


# Run the main function
main()