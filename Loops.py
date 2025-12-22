#Loops are used to repeate task
# two types
# for and while loop
#while loop
#while condition:
    #some work
count = 1 
while count <= 5 :
    print("hello", count)
    count +=1
    
# print numbers 1 to 5
i = 1
while i <=5 :
    print(i)
    i +=1
print("loop ended")

#Print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i +=1
    
#print numbers from 1 to 100
x =1
while x <=100:
    print(x)
    x +=1
print("loop ended")

#print numbers from 100 to 1
v = 100
while v >=1:
    print(v)
    v -=1
    
# print the multiplication of a number n
b = 5
while b <=50:
    print(b)
    b *=5
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
im = 0
while im < len(nums):
    print(nums[im])
    im +=1
heroes = ["ironman", "superman", "batman"]
ib = 0
while ib < len(heroes):  #traverse
    print(heroes[ib])
    ib +=1    
    
    

num1 = [1, 34, 54, 35, 16, 98]
x = 35

ik = 0
while ik < len(num1):
    if(num1[ik] == x):
        print("Found at index", ik)
        break
    else:
        print("finding..")
    ik +=1
print("end of Loop")
    
ip =1
while ip <=10:
    print(ip)
    if(ip == 1):
        break
    ip +=1

    
# For loop is used for sequential traversseal for traversing list string tuples etc

list = [1, 2, 3, 4, 5, 6]
for el in list:
    print(el)


num2 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
o = 36
ind =0
for no in num2:
    if(no == o):
        print("Found at index", ind)
        break
    ind += 1
    
# range function returns a sequence of numbers starting from 0 by default and increments by 1(by default) and stops by specified number
#Range(start:stop:step)


for i in range(2, 10,2):
    print(i)
    
# Print numbers from 1 to 100
for i in range(1, 101, 1):
    print(i)
    
#print numbers from 100 to 1
for el in range(100, 0, -1):
    print(el)
    



#Pass statement
#pass is a null statement that does nothing it is used as a placeholder for future code
for i in range(5):
    pass
print("some usefull work5")


