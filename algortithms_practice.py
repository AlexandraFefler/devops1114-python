# nums = [1,2,3,4,5]
# squares = []
# for i in range(0,len(nums)):
#     squares.append(nums[i]**2)
# print (squares)



# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# counter = 0
# for i in range(0,len(fruits)):
#     if "apple" == fruits[i]:
#         counter += 1
# print (f"There are {counter} apples in the list")



# colors = ['red', 'blue', 'green', 'yellow', 'blue']
# def is_there_green(list):
#     for i in range(0,len(list)):
#         if list[i] == 'green':
#             return i
#     return 0

# print (is_there_green(colors))



# list1 = [1,2,3]
# list2 = [4,5,6]
# list1.extend(list2)
# print(list1)

########################last my version
# def remove_all(lst, value):
#     result_lst = lst
#     for i in range(0,len(lst)):
#         if lst[i] == value:
#             result_lst.remove(result_lst[i])
#     return result_lst

# def remove_all(lst,value):
#     i = 0
#     while value in lst:
#         if lst[i] == value:
#             lst.remove(lst[i])
#         i += 1
#     return lst

######### ex. 20
# def remove_all(lst,value):
#     lst_of_places = []
#     for i in range(0,len(lst)):
#         if lst[i] 


##############Yeb tvoyu mat' za nogu sukaaaaaaaaaaaaaaaaa blyaaaaaaaaaaaaaaaaaat' yobaniy v rot nahuy 
# def remove_all(lst, value):
#     while value in lst:
#         lst.remove(value)
#     return lst



# numbers1 = [1,2,2,3,4,2]
# print(remove_all(numbers1,2))

# def sortAsc(nums):
#     for i in range(0,len(nums)):
#         if i > 0:
#             for j in range(0,i):
#                 if nums[j] >= nums[i]:
#                     nums.insert(j,nums[i])
#                     # nums.pop(nums[i+1])
#                     del nums[i+1]  #pushed all eyvarim to their position + 1, so the nums[i] i found to be out of order here, has moved +1 too
#     return nums

# nums = [33,55,1,2,3,78,130,3,0,-2,-90]
# print (sortAsc(nums))






#######  Iterables ex., the second pdf ##############
# 1
# my_tuple = (1,2,3)
# print(my_tuple[1])
# my_tuple[0] = 0 # won't work, only option is to cast the tuple to a list, change the list and cast it again into the tuple
# print(my_tuple)

# 2
# person = ("shasha","84","Kibini-bottom")
# (name, age, city) = person
# print(name)
# print(age)
# print(city)

# #tuple_3
# nested_tuple = ((1,2,3), (4,5,6))
# second_tuple = nested_tuple[1]
# print(second_tuple[1])

# #tuple_4
# numbers = (1, 2, 3, 2, 4, 2)
# countedNum = numbers.count(2)
# print(countedNum)
# hamburger = numbers.index(3)
# print(hamburger)

# #dict_1
# student = {"name": "yuval", "age": "24", "grade": "c"}
# print(student["name"])
# student["school"] = "ben-zvi"
# print(student)

# #dict_2
# student["age"] = "25"
# student["grade"] = "amazing"
# print(student)
# if "grade" in student:
#   print('Grade exist')
# else:
#   print('Does not exist')

# #dict_3
# capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
# for i in capitals.values():
#   print(i)



# #dict_4
# print(student.values())
# print(student.keys())
# grade = student.get("grade")
# print(grade)
# school = student.get("school")
# print(school)

# #dict_5
# def count_number(text):
#   number_count = {}
#   for char in text:
#     if char in number_count:
#       number_count[char] += 1
#     else:
#       number_count[char] = 1
#   return number_count
# text = "hello"
# result = count_number(text)
# print(result)

# #sets_1
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# # my_set.add(3)
# my_set.remove(2) #return 
# print(my_set)

# #sets_2
# set_a = {1, 2, 3, 4}
# set_b = {1, 5, 6, 7, 8}
# union_set = set_a.union(set_b)
# print(union_set) #return a union set 

# intersection_set = set_a.intersection(set_b)
# print(intersection_set) #returns a new set with elements common to both sets.
# difference_set = set_a.difference(set_b)
# print(difference_set) #returns the numbers that arent match
# symmetric_diff = set_a.symmetric_difference(set_b)
# print(symmetric_diff) #return a new set with elements that are in either of the sets, but not in both

# #sets_3
# numbers = [1, 2, 2, 3, 4, 4, 5]
# new_numbers = set(numbers)
# print(new_numbers)

# #sets_4
# if 3 in set_a:
#   print('3 is in set_a')
# else:
#   print("3 is not in set_a")  

# if 6 not in set_b:
#     print('6 is not in set_b')
# else:
#     print('6 is in set_b')
# print("lololololololololo")
# #sets_5
# last_set = {1, 2, 3, 4, 5}
# last_set.add(6)
# print(last_set)
# last_set.remove(6)
# print(last_set)
# last_set.discard(2)
# print(last_set) #discard won’t cause an error if the element isn’t present, whereas remove will











###########loops exercise ###############
#22
# def calculaotor(a, b, operation):
#     if operation == "+":
#         return a+b
#     elif operation == "-":
#         return a-b
#     elif operation == "*":
#         return a*b
#     elif operation == "/":
#         if b == 0:
#             return "Cannot divide by zero"
#         else:
#             if (a % b == 0):
#                 return a//b # // return an int (a whole number)
#             else:
#                 return a/b # / returns a float result (esroni)
#     else:
#         return "invalid operation entered (third argument), enter only +, -, /, or *"

# while True: # while loop just to not press "play" every time I check
#     a = int(input("Enter a: "))
#     b = int(input("Enter b: "))
#     op = input("Enter operation(+,-,*,/): ")
#     print("The result is: "+str(calculaotor(a,b,op)))



#21
# def is_prime(number):
#     return_value = True 
#     for i in range(2,number): # checks every number from 2 to number-1
#         if number % i == 0: # if number mithalek be ehad a misparim - 
#             print("The number is not prime, it is divided by " + str(i))
#             return_value = False # - siman she hu lo rishoni (prime) so we poslim it
#     return return_value # if no number is found, then it's a rishoni

# print(is_prime(24))

#20
# def sum_list(lst):
#     return sum(lst)

# ### or ###
# def sum_list2(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum

# print(sum_list2([10,20,30,40]))

#19
# def is_palindrome(word):
#     return word == word[::-1]

# print(is_palindrome("level"))

#18
# def celsius_to_fahrenheit(celsius):
#     return (celsius*1.8+32)

# print(celsius_to_fahrenheit(0))
# print(celsius_to_fahrenheit(20))
# print(celsius_to_fahrenheit(-200))

#17
# def find_max(lst):
#     max = lst[0]
#     for i in lst:
#         if i > max:
#             max = i
#     return max
# print("max is: "+str(find_max([1,5,6,3,0])))

#16
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i 
#     return result
# print(factorial(5))

# 5! = 1*2*3*4*5

#15
# def square(number):
#     return str(number)*4
# print(square(5))

#14
# def greet(name):
#     print("Hello "+name+"!")
# greet("shasha")

#13
# def greet():
#     print("Hello, brand new world")

# #12
# num = int(input("Enter a number, to stop entering numbers enter a negative number: "))
# sum = 0
# while num >= 0:
#     sum += num
#     num = int(input("Enter a number, to stop entering numbers enter a negative number: "))
# print(f"The sum of all this stuff is {sum}")

#11
# from random import randint

# randomNum = randint(1,101)
# guess = int(input("Guess a number between 1 and 100 :) :"))
# while guess != randomNum:
#     if guess > randomNum:
#         print("A lil lower")
#     else:
#         print("A lil higher")
#     guess = int(input("Guess a number between 1 and 100 :)"))
# print("Congrats! You guessed correctly - the num's "+str(randomNum))

## or ###
#10
# from time import sleep

# countdown = 10
# while countdown >= 1:
#     print(str(countdown))
#     countdown -= 1
#     sleep(0.5)
# print("Kaboom!")
# sleep(0.5)

#9
# colors = ['red','green','blue','yellow']
# for color in colors:
#     print(color)

#8 
# num = int(input("Enter number: "))
# for i in range(1,num+1):
#     for j in range(1,num+1):
#         print(i*j, end = "|")
#     print("\n")

#7 
# sum = 0
# for i in range(1,101):
#     sum += i
# print(str(sum))

#6
# for num in range(1,11):
#     print(str(num))
# ### modified ver ###
# for num in range(1,11):
#     if num % 2 == 0:
#         print(str(num))
# ### or ###
# for num in range(1,11,2):
#     print(str(num))

#5 
# age = int(input("What's your age punk? "))
# is_student = input("Are you a student? (yes/no): ")
# if age < 18 or is_student == "yes":
#     print("Congrats you got a discount")
# else:
#     print("You're gonna pay the full price, you're a working adult kapara")

#4
# num = int(input("Enter a number: "))
# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("The number is 0")

#3
# from time import sleep

# score = int(input("Enter your grade: "))
# if score >= 90 and score <= 100:
#     print("You got an A :)")
# elif score <= 89 and score >= 80:
#     print("You got a B :)")
# elif score <= 79 and score >= 70:
#     print("You got a C :)")
# elif score <= 69 and score >= 60:
#     print("You got a D :)")
# else:
#     print("You got an F, but life goes on :)")
#     sleep(2)
#     print("Without you.")

#2
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# 1
# age = int(input("What's your age? "))
# if age >= 18:
#     print("You're good to go")
# elif age == 16 or age == 17:
#     print("You're almost there!")
# else:
#     print("Sorry kid, you're too young")

#_______________side checks for fileOps.py_______________#
# import datetime
# str1 = "ooga booga"
# print("["+(datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")+"] "+str1)

# import os
# print(os.getcwd())

# f = open("journal.txt", "rt")
# print(f.read())

# # Get the current working directory
# current_directory = os.getcwd()
# print(current_directory)

# # List all files and folders in the current directory
# entries = os.listdir(current_directory)
# print(entries) # Returns ['my_data, 'airbnb_data.csv'] 

# open('journal.txt', 'w').close()

#_______________side checks for speedTest.py_______________#
# open('internet_speed.csv', 'w').close()
# import speedTest
# print(measure_speed())



# print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))
# print(list(map(lambda x: x % 2 == 0, [1,2,3,4,5,6,7,8,9,10])))

# class A:
#     count = 0
#     def __init__(self):
#         A.count += 1
# obj1 = A()
# obj2 = A()
# print(A.count)


# def func(ns):
#     s = 0
#     for k in range(1,len(ns)):
#         s += ns[k]
#     return s
# qs = [1,2,3,4,5]
# print(func(qs))