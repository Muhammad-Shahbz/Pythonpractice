# A dictionary is a built in Python data type to store data in key-value pairs
# In python dictionary curly braces {} are used
# keys and values are separated by:
# multiple items are separated by commas

Person = {"name": "Sara", "age": 25}
print(Person)
print(Person["name"])
print(Person["age"])
print(Person.get("age"))
print(Person.get("name"))

#adding new key
d1 = {"city": "islamabad", "population": 250000}
print(d1["city"])
d1["country"]="Pakistan"
print(d1)

#update existing key
d1.update({"city": "lahore"})
print(d1)

#Removing items
d1.pop("population")
print(d1)
del d1["city"]
print(d1)

d1.update({"cityy": "Multan", "population": 30000000})
print(d1.keys()) # return all keys
print(d1.values()) #return all values
print(d1.items()) # returns key value pairs
print(d1.copy())
