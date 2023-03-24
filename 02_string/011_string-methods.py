## String Methods

# capitalize(): Converts the first character the string to Capital Letter
challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'


# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 2`


# endswith(): Checks if a string ends with a specified ending
challenge = 'thirty days of python'
print(challenge.endswith('on'))  # True
print(challenge.endswith('tion'))  # False


# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'


# find(): Returns the index of first occurrence of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0


# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0


# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False


# isalpha(): Checks if all characters are alphabets
challenge = 'thirty days of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())  # False


# isdecimal(): Checks Decimal Characters
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0


# isdigit(): Checks Digit Characters
challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.digit())  # True


# isdecimal():Checks decimal characters
num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True


# isnumeric():Checks numeric characters
num = '10'
print(num.isnumeric())  # True
print('ten'.isnumeric())  # False


# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'


# strip(): Removes both leading and trailing characters
challenge = ' thirty days of python '
print(challenge.strip('y'))  # 5


# title(): Returns a Title Cased String
challenge = 'thirty days of python'
print(challenge.title())  # Thirty Days Of Python


# swapcase(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON


# startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))  # True
challenge = '30 days of python'
print(challenge.startswith('thirty'))  # False