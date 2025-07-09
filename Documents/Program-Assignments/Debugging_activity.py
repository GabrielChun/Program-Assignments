# Debugging activity - Gabriel Chun

# Code snippet 1
x = 10
y = 2
result = x / y # Zero division error, fix by changing y value to anything besides 0
print("Result:", result)

# Code snippet 2
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)): # Indexing starts from 0
   print(numbers[i]) # i + 1 when numbers = 5 is out of range

# Code snippet 3
def calculate_area(radius): # Missing colon when defining a func
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# Code snippet 4
def is_even(number):
   if number % 2 == 0: # Missing colon when calling if statement
       return True
   else: # Missing colon when calling else statement
       return False
 
print(is_even(4))
print(is_even(7))

#  Code snippet 5
for i in range(5): # Missing colon when calling a loop
   print(i)

# Code snippet 6
def greet(name):
   return "Hello, " + name # Forgot the + to join the strings together
 
print(greet("Alice"))

# Code snippet 7
numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number # Missing indentation for it to be called in the for loop
print("Sum of numbers:", sum)

# Code snippet 8
def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1) # Constantly calling the function since the number is going up, never reaching n == 0
 
print(factorial(5))

# Code snippet 9
name = input("Enter your name: ")
if name == "Alice" or name == "Bob": # Missing name ==, python needs to be hyperspecific
   print("Hello, " + name)
else:
   print("Hello, stranger!")

# Code snippet 10
def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2 # Division by 0, Change number to anything besides 0
print(divide_numbers(num1, num2))