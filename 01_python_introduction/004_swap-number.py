# Swap two variables
x = 6
y = 9
print('The value of x before swapping: {}'.format(x))
print('The value of y before swapping: {}'.format(y))
print("\n")
# To take inputs from the user
#x = input('Enter value of x: )
#y = input('Enter value of y: )

# x = x + y
# y = x - y
# x = x - y

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))