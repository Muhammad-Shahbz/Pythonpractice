
# A string is a squence of characters enclosed within single quotes
print("hello world") # this is a basic print statment showing how to print in python
a= "hello" #this is a string variable

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
cr = ar + " " + br
print(cr)

