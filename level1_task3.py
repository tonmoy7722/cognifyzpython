import re
def is_valid_email(email):
    # Define the regular expression for validating an email address
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the provided email matches the regular expression
    if re.match(regex, email):
        return True
    else:
        return False
# Input email to check
email = input("Enter an email address to validate: ")
# Validate the email
if is_valid_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is not a valid email address.")
