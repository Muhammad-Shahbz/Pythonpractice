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
t2 = (10, "hello", 20.5, True) # any type of data can be stored in touple
print(t2)

#Touple wiith duplicate values
t3 = (10,10,20,20, 30, 30)
print(t3)

# INDEXING AND Slicing in touples
t4 = (10,20,30,40,50,60,50,70,80,90)
print(t4[3]) # indexing
print(t4[-1]) # negative indexing
print(t4[:3]) # slicing
print(t4[::2]) #slicing with steps


#Nested Touples and accessing values
t5 = (20, "hello", (45,56,67,78), "world")
print(t5[::-1])
print(t5[2:-1])

#concotanation and repitation in touples
t6 =("a","b","c",4, 5 ,6)
t7 = ("d", "e","f",7,8,9,10)
print(t6 + t7) # concotanation
print(t6 * 2) # repitation

#membership operator in touples
t8 = (45,90,89,90,67)
print(90 in t8) #it will return true becuase 90 is in touple
print((100 in t8)) # it will return false because 100 is not in touple

# built in functions in touples
t9 = (90,30,50,60,20,10)
print(len(t9)) # length of touple
print(max(t9)) # maximum value in touple
print(min(t9)) # minimum value in touple
print(sum(t9)) # sum of all valuses in touple
print(sorted(t9)) # sorted touple meaning touple in ascending order
print(reversed(t9)) # reversed touple
print(tuple(range(1,11))) # touple with range of values 1 to 10
print(t9.count(90)) #count specific values in touple
print(t9.index(50)) # index of specific value in touple
#converting list to touple and touple to list
list1 = [10,10,90,80,70]
touple1 = tuple(list1) # llist to touple conversion 
print(touple1)

touple2 = (23,"hello", 45,78)
list2 = list(touple2) # touple to list conversion
print(list2)

#unpacking values in touples 
t5 =(10,2,34,45)
a, b, c,d =t5 
print(a)
print(b) # it will print 2
print(c) # it will print 34
print(d) # it will print 45

t = (1, [2,3])
t[1][0]=99
print(t) # touple is immutable but if it contains mutable eleneb=nts like list then we can change the value in the mutable element

#for loop in touples 
# touples can contain multiple vlaues and loops helps us to
# read each value one by one
#perform calculations
#search data
#Dsisplay values one by one

#for loop syntax
# for variable in touple-name:
#     statement
d
t10 =(10,20,30,40)
for x in t10:
    print(x)  # it will print all values in touple one by one
    # x will take each value of touple one by one and print it
    # loop will continue until all values are printed

t12 = ("Python", "java", "c")
for lang in t12:
    print("I love", lang) 

t13 = (5,10,40)
for i in range(len(t13)):
    print("index", i,"value", t13[i]) # it will print index and value of each element
    
#loop with condition
t14 = (10,20,3,40,5000)
for value in t14:
    if value > 40:
        print("Large value:", value)

t = (78,900),(45,43),(54,50)
for a, b in t:
    print("a:", a, "b:", b)
    #it will print a and b values from each nested touple

#While Loop in touples
#what is iteration? iteration is the process of repeating a set of instructions
# while loop basic syntax
#index = 0 
#hile index < len(index)
  #statement
  # statement +=1
  
# basic while loop with a touple
t = (20,30,40,50,60,70)
i = 0
while i < len(t):
    print(t[i])
    i +=1 
    
    
t = ("apple", "banana", "cherry")
i = 0
while i < len(t):
    print(i, "->", t[i]) 
    
    i +=1

 #0 -> apple
 #1 -> banana
 #2 -> cherry
 
 
 
 

    
    
        

   