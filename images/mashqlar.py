import sys
import math

# =========================   Question_1: ===========================================
# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# Consider use range(#begin, #end) method


numbers = range(2000, 3201)
sorted_numbers = []

for i in numbers:
    if i % 7 == 0 and i % 5 != 0:
        sorted_numbers.append(i)
print(sorted_numbers)




# =========================   Question_2: ===========================================

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
#
# Hints:
# In case of input data being supplied to the question, it should be assumed
# to be a console input.

def fact_1(x):
    b = 1
    for a in range(1, x+1):
        b *= a
    return b
print("Exercise_2: Solution_1(input like 8 or 9)")
# x = int(input())
# print(fact_1(x))


# Solution 2:
def fact_2(x):
    if x == 0:
        return 1
    return x * fact_2(x - 1)

print("Exercise_2: Solution_2(input like 8 or 9)")
# x=int(input())
# print (fact_2(x))


# =========================   Question_3: ===========================================
# Question:
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a
# console input.
# Consider use dict()

def prog_1(x):
    dict_ = dict()
    for a in range(1, x+1):
        dict_[a] = a*a
    print(dict_.__str__())
print("Exercise_3: input like 8, 7 or 9")
# prog_1(int(input()))

# =========================   Question_4: ===========================================
# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be assumed to be a
# console input.
# tuple() method can convert list to tuple

print("Exercise:4 (input like 30,23,24,345)")
def prog_2():
    x = input()
    l = []
    for a in x.split(","):
        l.append(a)
        print(x)
    t = tuple(l)
    print(l)
    print(t)
# prog_2()


# =========================   Question_5: ===========================================
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters

class Class_1:
    def __init__(self, str_):
        self.str_ = str_

    def getString(self):
        print("Enter string:")
        self.str_ = input()
        return
    def printString(self):
        return print(self.str_)

x = Class_1("Salom, Doston")
x.printString()


# =========================   Question_6: ===========================================
# Write a program which takes 2 digits, X,Y as input and generates
# a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


def two_dimens_arr(x, y):
    l1 = []
    for a in range(x):
        l1.append([])
        for b in range(y):
            d = a * b
            l1[a].append(a*b)
    print(l1)
    return
two_dimens_arr(4, 4)


# =========================   Question_7: ===========================================
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def prog_3():
    x = input()
    list_ = []

    for a in x.split(","):
        list_.append(a)
    list_.sort()
    str_ = ",".join(list_)
    print(list_)
    return



# =========================   Question_8: ===========================================
# Write a program that accepts a sequence of whitespace separated words as input and prints the words
# after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

def prog_4():
    x = input()
    set_ = set((x.split()))
    list_ = [x for x in set_]
    list_.sort()
    print(" ".join(x for x in list_))
# prog_4()


# =========================   Question_9: ===========================================
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are
# to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.


def prog_5():
    x = input().split(",")
    print(x)
    list_ = []
    for a in x:
        list_.append(int(a))
    list_2 = [a for a in list_ if a % 5 == 0]
    print(list_2)
# prog_5()

# =========================   Question_10: ===========================================
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.

def prog_6():
    n_ = []
    str_num_ = ""
    for a in range(1000, 3001):
        str_num_ = str(a)
        indicator_ = 0
        for i in str_num_:
            if int(i)%2 == 0:
                indicator_ += 1
        if indicator_ == 4:
            n_.append(a)
    print(n_)
    return
prog_6()


# =========================   Question_11: ===========================================
# Write a Python program to get the Python version you are using

str_ = str(sys.version_info[0]) + "." + str(sys.version_info[1]) + "." + str(sys.version_info[2])
print("Python version: " + str_)
# or simple
print(sys.version_info)

# =========================   Question_12: ===========================================
# Write a Python program which accepts the radius of a circle from the user and compute the area.

def prog_7():
    radius  = int(input())
    print("Area for radius: " + str(radius) + " is " + str(math.pi * math.pow(radius, 2)))
# prog_7()


# =========================   Question_13: ===========================================
# Write a Python program which accepts a string and return as reverse order:

str_ = "Doston"
print("----- Reversing string using FOR loop -------")
s = ""
for x in str_:
    s = x + s
print("Orginal: " + str_)
print("reversed: " + s)

print("----- Reversing string using a function_ 1 -------")
def reverse_1(string):
    string = string[::-1]
    return string
print("Orginal: " + str_)
print("reversed: " + reverse_1(str_))

print("----- Reversing string using RECERSED function -------")
def reverse_2(string):
    string = "".join(reversed(string))
    return string
print("Orginal: " + str_)
print("reversed: " + reverse_2(str_))


# =========================   Question_13: ===========================================
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate
# a list and a tuple with those numbers.

def prog_8():
    x = input()
    list_ = list(x.split(","))
    tuple_ = tuple(x.split(","))
    print(list_)
    print(tuple_)
# prog_8()

# =========================   Question_13: ===========================================
# Write a Python program to display the first and last colors from the following list
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[len(color_list)-1])
print("=============================================")


# =========================   Question_14: ===========================================
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def prog_9():
    # x = input()
    x = "add230"
    int_n = 0
    str_n = 0

    for a in x:
        if a.isalpha():
            str_n +=1
        else:
            int_n +=1
    print("LETTERS: " + str(str_n))
    print("DIGITS: " + str(int_n))
    return
prog_9()