# a = 1


# def fun():
#     global a
#     a = 2
#     print(a)


# a = 3
# fun()
# print(a)

# check if it triangle

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Enter the first side\'s length: '))
# b = float(input('Enter the second side\'s length: '))
# c = float(input('Enter the third side\'s length: '))

# if is_a_triangle(a, b, c):
#     print('Yes, it can be a triangle.')
# else:
#     print('No, it can\'t be a triangle.')


#area of a triangle

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def heron(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c)) ** 0.5


# def area_of_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return None
#     return heron(a, b, c)


# print(area_of_triangle(1., 1., 2. ** .5))


#factorial

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product


# for n in range(1, 6):  # testing
#     print(n, factorial_function(n))

# fibonacci

# def fib(n):
#     if n < 1:
#         return None
#     one
#     if n<3:
#         return 1
        
#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n+1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum
    
    
    
# for n in range(1, 10):
#     print(n, "->", fib(n))

# recursion- a function invokes itself

# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):
#     print(n, "->", fib(n))

# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)


# Recursive implementation of the factorial function.

# def factorial(n):
#     if n == 1:    # The base case (termination condition.)
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(4)) # 4 * 3 * 2 * 1 = 24


# tuples and dictionaries


# school_class = {}

# while True:
#     name = input("Enter the student's name: ")
#     if name == '':
#         break
    
#     score = int(input("Enter the student's score (0-10): "))
#     if score not in range(0, 11):
# 	    break
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
        
# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # outputs: 4

#combine dictionary

# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)

#convert list to tuple

# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)
# print(t)

#tuple to dictionary

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors)

# print(colors_dictionary)