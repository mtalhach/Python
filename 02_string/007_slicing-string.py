# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

b="Hello world"
print(b[:4])

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto) # pto