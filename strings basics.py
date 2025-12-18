
# A string is a squence of characters enclosed within single quotes


print("hello world") # this is a basic print statment showing how to print in python
a= "hello" #this is a string variable

#multiple line string
b = """im learning python from basic to advance level 
as a key to become artificial intelligence engineer""" #this is multiline strings
print(a)
print(b)

#String indexing and slicing

s = "Optometrist"

print(s[0])
print(s[-1])
print(s[:-1]) #print all except last character
print(s[2:]) #print from index 2 to end
print(s[::3]) #print every third character
print(s[::-1]) # print string in reverse order

# strings are immutable you can not change character directly

ab = "hellp"
#a[0]="H" # this will give errror

#to change string we can do like this
ab = "o" + a[-1]
print(a)

# String length

r = "Optometry"
print(len(r))

# String Concatenation
# In string concatenation we can join two strings together
ar="hello"
br="world"
cr = ar + " " +br
print(cr)

#String Repetition is done by multiplying string with integer

print("Hi " * 3)

print("Hi " *1 +"Shahbaz")
print("welcome " *2 + "to " *2 + "Python")
print("welcome\n " *2 + "to\n " *2 + "Python\n") # \n is used for new line

# Membership operator in python in strings is used to check if a value exists in a string or not

str1 = "Artificaial intelligence"
print("intelligence" in str1) #it will return true
print("machine" not in str1) # it will return true
print("Art" in str1) # it will return true 
print("art" in str1) # it will return false becauase its case sensitive 
print("intelligence" not in str1) # it will return falsse becausse intelligence is pressent

# check substring in stsring
str2 = "Python is powerfull language"
print("powerfull" in str2) #it will return true
print("java" in str2) # it will return false

str3 = "python programming"
print("z" in str3) # it will return false
print("g" in str3) # it will return true

#built in string functions

a = "PYTHON"
print(a.lower()) # converts string to lowercase

vb = "nice to meet you"
print(vb.upper()) # converts string to uppercase

"python language is easy".capitalize()
"python language".title()