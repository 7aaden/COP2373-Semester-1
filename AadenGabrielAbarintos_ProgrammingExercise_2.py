# AadenGabrielAbarintos_ProgrammingExercise_2.py
# This program creates a list of 30 words and phrases commonly used and found 
# in spam messages. This program accepts an input of an email message,
# and analyzes it for the 30 words or phrases. The program then displays the 
# liklihood that the email is spam, the spam score of the email, and
# the amount of phrases that increased the email's risk.


# Define the scan_message function.
def scan_message(message, keywords):
    
    # Convert the message to lowercase
    # to prevent case sensitivity.
    msg_lower = message.lower()

    # Split the message into individual words.
    words = msg_lower.split()

    # Create an empty dictionary to store matched spam words
    matches = {}

    # Initialize the accumulator variable to keep count of
    # the spam score.
    score = 0

    # Create a for loop to look through each
    # keyword in the list and finds it in the email.
    for kw in keywords:
        kw_lower= kw.lower()
        
        # Create an if statement to check if the keyword/phrase
        # is more than one word.
        if " " in kw_lower:

            # Count how many times the keyword appears.
            count = msg_lower.count(kw_lower)

        else:
            # Count how many times a singular key word
            # appears.
            count = words.count(kw_lower)

        # If found, store matched key words and add point(s)
        # to the score.
        if count > 0:
            matches[kw] = count
            score += count
    
    # Return the spam score of the email and the
    # number of matched keywords.
    return score, matches


# Define the rate_score function.
def rate_score(score):

    # Rate each score range.
    if score == 0:
        return "Very unlikely that this email is spam."
    elif 1 <= score <= 2:
        return "Low likelihood that this email is spam."
    elif 3 <= score <= 5:
        return "Likely that this email is spam."
    elif 6 <= score <= 9:
        return "High likelihood that this email is spam."
    else:
        return "Most definitely spam. PROCEED WITH CAUTION!"


# Define the main function.
def main():

    # Create the list of keywords that are common in spam messages.
    spam_keywords = [
        "free", "click here", "act now", "limited time", "deal",
        "bonus", "cash", "congratulations", "urgent", "winner",
        "financial freedom", "debt", "exclusive", "click to remove",
        "investment opportunity", "earn money", "make money", "$$$",
        "order now", "unsubscribe", "subscribe now", "free gift",
        "get paid", "guaranteed", "giveaway", "promise", "miracle",
        "special promotion", "once in a lifetime", "risk-free"
    ]

    # Ask the user for the suspicious email.
    message = input("Please paste the suspicious " 
                "email as one line: "
                ).strip()
    
    # If the user did not input a message stop the program.
    if not message:
        print("No message entered. Exiting.")
        return

    # Call the scan_message function within the main function.
    score, matches = scan_message(message, spam_keywords)

    # Call the rate_score function within the main function
    category = rate_score(score)

    # Display the data results
    print(f"Spam score: {score}")
    print(f"Spam likelihood: {category}")

    # Displays which specific key words appeared
    # and how many times they appeared.
    if matches:
        print("\nMatched keywords/phrases and counts:")
        for kw, cnt in matches.items():
            print(f" {kw} : {cnt}")
    else:
        print("\nNo keywords or phrases detected.")


# Run the main function
main()