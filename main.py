import useful_tools
from math import *
'''
characture_name = "John"
characture_age = "35"
print("Hello " + characture_name)
print(characture_name + " is " + characture_age + " years old.")

# string
phrase = "Giraffe Academy"
print(phrase.lower())
print(phrase.upper())
print(phrase.lower().islower())
print(len(phrase))
print(phrase[0])
print(phrase.index("G"))
print(phrase.replace("Giraffe", "Elephant"))

# numbers
my_num = -5.6
print(my_num)
print(abs(my_num))
print(str(my_num))
print(pow(my_num, 2))
print(max(my_num, 9))
print(min(my_num, 9))
print(round(my_num))
print(floor(my_num))
print(ceil(my_num))
print(sqrt(5))

# input from user
name = input("enter your name:")
age = input("enter your age:")
print("Hello " + name + "! you are " + age + " years old!")

# calculator
num1 = input("Enter a number:")
num2 = input("Enter another number:")
result = float(num1) + float(num2)
print(result)

# Mad libs Game
color = input("Enter a color:")
plural_noun = input("Enter a plural noun:")
celebrity = input("Enter a celebrity:")
print("roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# lists
friends = ["Mike", "Mary", "Emi", "Emi", "Nick", "Theo"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[2:4])
print(friends[2:])
friends[1] = "Jim"
print(friends[1])

# lists functions
lucky_numbers = [28, 98, 1, 8, 7, 29]
friends.extend(lucky_numbers)
print(friends)
friends.append("Emi")
print(friends)
friends.insert(1, "Kave")
print(friends)
friends.remove("Nick")
print(friends)
friends.pop()
print(friends)
print(friends.index("Emi"))
print(friends.count("Emi"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
friends2 = friends.copy()
print(friends2)
friends2.clear()
print(friends2)

# tuples
coordinates = (4, 5)
print(coordinates[0])


# function

def say_hi(user_name):
    print("Hello " + user_name + "!")


say_hi("Mary")


# return statement

def cube(num):
    return pow(num, 3)


cube_result = cube(2)
print(cube_result)

# if statement
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not is_tall:
    print("You are a male and not tall")
elif not is_male and is_tall:
    print("You are not male and tall")
else:
    print("You are not male and not tall")


# if statement and comparison
def max_num(num11, num12, num13):
    if num11 >= num12 and num11 >= num13:
        return num11
    elif num12 >= num11 and num12 >= num13:
        return num12
    else:
        return num13


print(max_num(3, 4, 6))

# better calculator
num21 = float(input("Enter first number:"))
op = input("Enter operator:")
num22 = float(input("Enter second number:"))

if op == "+":
    print(num21 + num22)
elif op == "-":
    print(num21 - num22)
elif op == "*":
    print(num21 * num22)
elif op == "/":
    print(num21 / num22)
else:
    print("Invalid operator")

# dictionary
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv", "Invalid key"))

# while loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

# Guessing Game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose!")
else:
    print("You Win!")

# For loop
for letter in "Giraffe Academy":
    print(letter)
for friend in friends:
    print(friend)
for index in range(10):
    print(index)
for index2 in range(3, 10):
    print(index2)
for index3 in range(len(friends)):
    print(friends[index3])
for index4 in range(5):
    if index4 == 0:
        print("first iteration")
    else:
        print("not first iteration")


# exponent function
def raise_to_power(base_num, pow_num):
    result2 = 1
    for index5 in range(pow_num):
        result2 = result2 * base_num
    return result2


print(raise_to_power(2, 3))

# 2D lists and nested loops
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][1])

for row in number_grid:
    for col in row:
        print(col)

# build a translator


def translate(phrase2):
    translation = ""
    for letters in phrase2:
        #if letters in "AEIOUaeiou":
        if letters.lower() in "aeiou":
            if letters.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letters
    return translation


print(translate(input("Enter a phrase: ")))

# try exception
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid value!")

# reading file
employees_file = open("employees.txt", "r")
#print(employees_file.readable())
#print(employees_file.read())
#print(employees_file.readline())
#print(employees_file.readline())
#print(employees_file.readlines())
#print(employees_file.readlines()[0])

for employee in employees_file.readlines():
    print(employee)

employees_file.close()

# writing file
employee_file = open("employees.txt", "a")
employee_file.write("Toby - Human Resource")
employee_file.write("\nKate - Customer Service")

employee_file.close()

html_file = open("index.html", "w")
html_file.write("<p>This is HTML</p>")


# modales and pip
print(useful_tools.roll_dice(10))

# classes & objects
from Student import Student

student1 = Student("Jim", "IT", 3.9, False)
student2 = Student("Kim", "Art", 2.5, True)
print(student1.gpa)
print(student1.on_honor_roll())

# multiple choose quiz
from Question import Question
question_prompt = [
    "what color is apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "what color is bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "what color is strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]
questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")


run_test(questions)
'''
# inheritance
from Chef import Chef
from ChineseChef import ChineseChef

my_chef = Chef()
my_chef.make_chicken()
my_ChineseChef = ChineseChef()
my_ChineseChef.make_special_meal()
