s = "Python"
print(len(s)) # length of string
print(s[0])     #first character
print(s[-1])    #last character
print(s[1:4])   #substring from index 1 to 3 slies

print(s[::-1])  #reverse the string # reversing a string using sliceing

print(s[::2])

print(s.upper()) # convert to uppercase
print(s.lower()) # convert to lowercase 
print(s.replace("P", "J")) # replace cahracters
print(s.title())
print(s.count("o"))

print(s.isalpha())
print(s.isdigit())
print(s.isupper())
sentence = "Python is easy to learn"
words = sentence.split()
print(words)
joined = "-".join(words)
print(joined)

name = "ali"
age = 27
print(f"My name is {name} and i am {age} years old.")

ali =int(input("Ali"))
karim =int(input("Karim"))
print(f"Ali", {ali+1})
print(f"Karim", {karim-1})           
