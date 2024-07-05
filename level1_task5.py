import re
def is_palindrome(s):
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()

    # Check if the cleaned string reads the same backward as forward
    return cleaned == cleaned[::-1]


# Input string to check
string = input("Enter a string to check if it's a palindrome: ")

# Check if the string is a palindrome
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
