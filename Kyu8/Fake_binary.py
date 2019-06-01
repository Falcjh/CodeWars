# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'.
# Return the resulting string.

return ''.join('0' if int(c) < 5 else '1' for c in s)