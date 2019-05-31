# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits
# or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.


import re


def validate_pin(pin):
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    return False


# Some regex explanation:
#
# This character "\d" matches only digits.
# The number in curly brackets that follows it shows exactly how many of the preceding token
# ("\d" in our case) we want to match.
# This "|" acts like an OR, telling that we can either match 4 digits, or 6 digits.
# fullmatch will only return a match object if the entire string matches the pattern.
# But since we don't have that function in the earlier versions,
# this behaviour can be simulated by adding a "$" at the end of our pattern.
# It shows that we want this pattern to only match the end of the string and match function matches the characters from the beginning only.
# So combining these properties, we get a pattern that will only match the entire string
