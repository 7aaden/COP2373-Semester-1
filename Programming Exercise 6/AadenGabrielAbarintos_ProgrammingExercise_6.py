# AadenGabrielAbarintos_ProgrammingExercise_6
# This program writes an application that validates data,
# specifically phone numbers, social security numbers,
# and zip codes using regular expressions.

# Import the regular expression module
import re

# Validate the phone number
def validate_phone(phone):

    phone_pattern = re.compile()


# Validate the Social Security Number
def validate_ssn(ssn):

    ssn_pattern = re.compile()


# Validate the ZIP code
def validate_zip(zip_code):

    zip_code_pattern = re.compile()


# Initialize the main function
def main():

    # Ask the user for their credentials
    print("Credential Validation Test: ")
    phone = input("Enter your phone number: ")
    ssn = input ("Enter your Social Security Number: ")
    zip_code = input("Enter your ZIP code: ")

    # Display the data
    print("Validity Test Results: ")
    print()
    print(f"Phone Number: {validate_phone(phone)}")
    print(f"SSN: {validate_ssn(ssn)}")
    print(f"ZIP Code: {validate_zip(zip_code)}")


# Run the main function
main()