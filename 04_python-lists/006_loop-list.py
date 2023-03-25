thislist = ["apple", "banana", "cherry"]
for x in thislist:
# print(x)
    print(x,end=" ")    #apple banana cherry
print("\n")


#range() and len()
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i],end=" ")    #pple banana cherry
print("\n")


#while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i],end=" ")    #pple banana cherry
  i = i + 1
print("\n")


#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x,end=" ") for x in thislist]    #pple banana cherry
print("\n")
