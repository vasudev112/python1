# 1.Define a function called `greet` that takes a name as an argument and prints a greeting message like: "Hello, [name]!

def greet(name):
  print("Hello, "+name+" !")
greet("praveen")

# 2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by passing different numbers

def add_numbers(a, b):
    return a + b
print("Sum add numbers :",add_numbers(5,8)) 

# 3.Create a function `is_even` that takes a number as an argument and returns `True` if the number is even, and `False` otherwise.
def is_even(x):
 if x%2==0:
    return True
 else:
    return False
 
print("the given even number is :",is_even(4))
print("the given even number is :",is_even(7))
print("the given even number is :",is_even(0)) 

# 4.Write a function `factorial` that takes a positive integer as input and returns the factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result
print("factorial of 5 :",factorial(5))
print("factorial of 4 :",factorial(4))
print("factorial of 3 :",factorial(3))
print("factorial of 2 :",factorial(2))
print("factorial of 1 :",factorial(1))

print(".........")
# 5.Define a function `find_max` that takes three numbers as input and returns the largest of the three. Test the function with various sets of numbers.
def find_max(a, b, c):
    return max(a, b, c)
print("findmax and return large of three inputs :",find_max(3,5,7))

# 6.Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
print("count vowels :",count_vowels("helloworld"))

# 7.Create a function `is_prime` that takes a number as input and returns `True` if the number is prime, and `False` otherwise.
def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
        return True
print("check 9 is a prime number :",test_prime(9))
print("check 7 is a prime number:",test_prime(7))

# 8.Write a recursive function `recursive_sum` that takes a positive integer `n` and returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)` should return \(1 + 2 + 3 + 4 + 5 = 15\).
def recursive_sum(n):
    if n == 1 :
        return 1
    else :
        return n + recursive_sum(n-1)

print(recursive_sum(5))

# 9.Write a function `calculator` that takes three parameters: two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`). The function should perform the operation on the two numbers and return the result.
def calculator(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":       
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
            
print("calculator using + operator :",calculator(5, 3, "+"))
print("calculator using - operator :",calculator(5, 3, "-"))
print("calculator using * operator :",calculator(5, 3, "*"))
print("calculator using % operator :",calculator(5, 3, "/"))

# 10.Write a function `find_common_elements` that takes two lists as input and returns a list of elements that are present in both lists.
def find_common_elements(list1,list2):
    common_elements = [elements for elements in list1 if elements in list2]
    return common_elements
list1 =[1,3,5,75]
list2 = [3,4,6,5]
print(list1,list2)
print("finding common elements in ;list",find_common_elements(list1,list2))

# 11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
def reverse_string(e):
   return e[::-1]
print("reverseing the string :",reverse_string("hello"))

# 12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a list of tuples sorted by the dictionary values in ascending order.
data = {'student1': ('bhanu', 10), 'student4': ('uma', 12),
		'student3': ('suma', 11), 'student2': ('ravi', 11),
		'student5': ('gayatri', 9)}
for i in sorted(data.items()):
	print(i, end=" ")
print()
for i in sorted(data.values()):
	print(i, end=" ")
print()
for i in sorted(data.keys()):
	print(i, end=" ")
