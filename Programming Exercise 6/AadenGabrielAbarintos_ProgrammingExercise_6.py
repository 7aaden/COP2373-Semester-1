# AadenGabrielAbarintos_ProgrammingExercise_6
# This program writes an application that validates data,
# specifically phone numbers, social security numbers,
# and zip codes using regular expressions.


# Import the regular expression module
import re

# Validate the phone number
def validate_phone(phone):

    # Create the pattern to match the user's phone number to.
    phone_pattern = re.compile(r'^\(?\d{3}\)?[\s-]?\d{3}-?\d{4}$')

    # Return t/f depending on if the number matches the pattern.
    return bool(re.match(phone_pattern, phone))


# Validate the Social Security Number
def validate_ssn(ssn):

    # Create the pattern to match the user's SSN to.
    ssn_pattern = re.compile(r'^\d{3}-?\d{2}-?\d{4}$')

    # Return t/f depending on if the ssn matches the pattern.
    return bool(re.match(ssn_pattern, ssn))


# Validate the ZIP code
def validate_zip(zip_code):

    # Create the pattern to match the user's ZIP Code to.
    zip_code_pattern = re.compile(r'^\d{5}(-\d{4})?$')

    # Return t/f depending on if the zip code matches the pattern.
    return bool(re.match(zip_code_pattern, zip_code))


# Initialize the main function
def main():

    # Ask the user for their credentials
    print("Credential Validation Test: ")
    phone = input(
        "Enter your phone number (XXX-XXX-XXXX),"
        "((XXX) XXX-XXXX), or (XXXXXXXXXX): "
    )

    ssn = input ("Enter your Social Security Number (XXX-XX-XXXX) or (XXXXXXXXX): ")
    zip_code = input("Enter your ZIP code (XXXXX) or (XXXXX-XXXX): ")

    # Display the data
    print("Validity Test Results: ")
    print()
    print(f"Phone Number: {validate_phone(phone)}")
    print(f"SSN: {validate_ssn(ssn)}")
    print(f"ZIP Code: {validate_zip(zip_code)}")
    print(
        "'True' denotes that your information matches the correct format. " 
        "'False' means that your information is input incorrectly."
        )


# Run the main function
main()