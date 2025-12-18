
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

#Python swacase() function is used capitalize the first letter of each word and lower case the other letters that are in upper case

str4 = "hello WORLD"
print(str4.swapcase())

# Searching in strings
ap = 'python'
print(ap.find('t')) # it will return index of character 't' which is 2


#index() is similar to find() but it raises an error  if the substring is not found
str5 = "artificial intelligence"
print(str5.index('i')) # it will return index of first 'i' which is 3

# rindex() function gives the index of last occurence of substring like this
str6 = 'programming in python'
print(str6.rindex('r'))

# count() function counts the number of occurrence of substring in string
str7 = "data science is getting disappear and take over by artifiical intelligence"
print(str7.count('is')) # it will return 2 becausse 'is' occurs 2 times in string

# checking boolean methods
str8 = "HELLO"
print(str8.isupper()) # it will return true because all characters are in uppercase

'hello'.islower() # it will return true because all characters are in lowercase

# isalnum() function checks if all character in string are alphanumeric

str9 = "hello124"
print(str9.isalnum()) # it will return true because all characters are alphanumeric
str10 = "hello@12"
print(str10.isalnum()) # it will return false because '@' is not alphanumeric
print("hello")
# isspace() function checks if all characters in string are with space or not 
print(" ".isspace()) # it will retrun true
print("hellowoeld".isspace())

# istitle() functions checks if string is in title case or not
str11 = "Hello World"
print(str11.istitle()) # it will return true because both words start with uppercasse

# white space removal functions
str12 = " hello world"
print(str12.strip())# it will remove leading and tailing white spaces


# Isstrip() funnction removes leading white spaces
str13 = "   hello world"
print(str13.lstrip()) 

#rstrip() function removes tailing white spaces
str14 = "hello world "
print(str14.rstrip())

# replace() function replace substring with another substring

"I like java".replace("java", "python")
# Split() function splits string into list of substrings based on values provided
str15 = "python is easy to learn"
print(str15.split()) # it will split string at space and return list of words

# rsplit() function splilts string from right side based on value provided 
str16 = "apple, bannana, orange"
print(str16.rsplit(", ")) # it will split string at ',' and return list of fruits

#join() function joins elements of iterable to end of string
str17 = ("-".join(["2025", "12", "18"]))
print(str17)

str18 = "@".join(["optmetry", "ai", "com"])
print(str18)

# startswith() function checks if string starts with specified substring
str19 = "artificial intelligence"
print(str19.startswith("art")) # it will return true
print(str19.startswith("int")) # it will return false

#center() function center the string within specified width
str20 = "hello python"
print(str20.center(100)) # it will center the string within 100 characters width

# ljust() function left justifies the string within specified width
str21 = "hello ai engineer "
print(str21.ljust(50))

# Formate() functiion is used to formate string by placing values in placehlders
name = "Yasir"
age = 25
intro = "My name is {} and i am {} years old".format(name, age)
print(intro)

print(f"Name: {name}, Age: {age}") # f string formating

price = 99.099990
print(f"Price: %.2f" % price)
