"""
This Python script manipulates a string by repeating it and printing a substring.

It assigns the string "Holberton School" to the variable 'str', then it prints 'str' repeated three times with spaces in between, and also prints the first 9 characters of 'str'.
"""

str = "Holberton School"

print(" ".join([str] * 3))
print(str[:9])
