# Question 1
print("Question 1")

string = str(input("Enter string to be reversed : "))
length_string = len(string)
print(string[length_string::-1])

print("----------------------------------------------------")

# Question 2

print("Question 2")

input_range = int(input("Enter Range : "))
num = int(input("Enter number : "))

for i in range(input_range):
    if (i % num == 0):
        print(i)
    else:
        continue

print("----------------------------------------------------")

# Question 3

print("Question 3")

import math
s1= int(input("Enter the first side: "))
s2= int(input("Enter the second side: "))
s3= int(input("Enter the third side: "))
if s1+s2<s3 or s2+s3<s1 or s3+s1<s2:
    print("Triangle is not possible")
else:
    S= (s1+s2+s3)/2
    area= math.sqrt(S*(S-s1)*(S-s2)*(S-s3))
    print(area)

# Question 4

print("Question 4")
print(" ")

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=' ')
    print()

for i in range(5, 1, -1):
    for j in range(1, i):
        print("*", end=' ')
    print()

print(" ")
print("----------------------------------------------------")

# Question 5

print("Question 5")

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
             "V", "W", "X", "Y", "Z"]
rows = int(input("Enter number of rows : "))
k = 0
for i in range(rows):
    for j in range(i):
        if k > 25:
            k = 0
        print(alphabets[k], end=' ')
        k += 1
    print()

print("----------------------------------------------------")

# Question 6

print("Question 6")

user_range = int(input("Enter Range : "))
for n in range(user_range + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i == 0):
                break
        else:
            print(n)

print("----------------------------------------------------")

# Question 7

print("Question 7")

for i in range(500):
    if i % 7 == 0:
        if i % 11 == 0:
            print(i)
        else:
            continue

print("----------------------------------------------------")

# Question 8

print("Question 8")

newlist = []
positive_nums = []
negative_nums = []
even_nums = []
odd_nums = []
for i in range(10):
    user_input = int(input("Enter Integer Value : "))
    newlist.append(user_input)
set_newlist = set(newlist)
for num in set_newlist:
    if num > 0:
        positive_nums.append(num)
    if num < 0:
        negative_nums.append(num)

for num in set_newlist:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
print("Positive numbers : ", positive_nums)
print("Negative numbers : ", negative_nums)
print("Even numbers : ", even_nums)
print("Odd numbers : ", odd_nums)

for num in set_newlist:
    print(num, " appears ", newlist.count(num), " times.")

print("----------------------------------------------------")

# Question 9

print("Question 9")

user_list = []
list_len = int(input("Enter length of list you wish to enter : "))
for i in range(list_len):
    c = str(input("Enter word : "))
    user_list.append(c)
set_userlist = set(user_list)

for element in set_userlist:
    print(element, " occurs ", user_list.count(element), " times.")