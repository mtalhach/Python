# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


fname="talha"
lname="SHAFIQ"
print(fname.upper())
print(lname.lower())


# The strip() method removes any whitespace from the beginning or the end:
challenge = ' thirty days of python '
print(challenge.strip())


# replace(): Replaces substring inside
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'


challenge = 'thirty days of python'
print(challenge.replace('y', '*')) # 'thirty days of coding'


# split():Splits String from Left
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']