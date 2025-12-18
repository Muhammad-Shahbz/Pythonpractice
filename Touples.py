### Touples in Python
#Touples are similar to list but they are immutable means we cannot change the values once touple is created .Touples are created using parenthesis (). 
# Touples are faster than list because of immutability.
# touples can store all types of data like list
#in Touples we can use duplicate values
#Touples support indexing and slicing like list
# Touples can be nested like list
# In touples we can do concatenation and repitation like list
# in touples we can use membership operator like list
#in touples we can use built in functions like list
# in touples we can convert list to touple and touple to list
# in touples we can unpack values like list
# in touples we can iterate using loops like list
#touples are used when we want to store data that should not be change throughout the programe
# in touples commas are used to separate vlaues
# the differece between touple and sting is that string is used to store squence of characters while touple is used to store sequence of any type of data.


# Normal Touple
t = (10,20,30,40,50)
print(t)

t = 10, 20, 30
print(t)  # without parenthesis also touple can be created
 #single element touple
t1 = (20,) #comma is necesary to create single element touple
print(t1)

# Touples with different data types
t2 = (10, "hello", 20.5, True)
print(t2)



