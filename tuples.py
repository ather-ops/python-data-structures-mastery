"""
PYTHON TUPLES - COMPLETE GUIDE FOR BEGINNERS
Tuple = ordered collection of items that CANNOT be changed
"""

print("=" * 50)
print("TUPLES BASICS")
print("=" * 50)

# 1. CREATING TUPLES
# ==================

# Tuple with parentheses
t1 = (1, 2, 3, 4, 5)
print("Tuple 1:", t1)

# Tuple without parentheses (comma is what matters)
t2 = 10, 20, 30
print("Tuple 2:", t2)

# Single element tuple (needs comma)
t3 = (5,)  # This is a tuple
t4 = (5)   # This is just number 5
print("Single element tuple:", t3, type(t3))
print("Without comma:", t4, type(t4))

# Mixed tuple
person = ("John", 25, "New York", True)
print("Person tuple:", person)

# 2. ACCESSING TUPLE ELEMENTS
# ===========================

print("\nACCESSING ELEMENTS:")

colors = ("red", "green", "blue", "yellow", "purple")
print("All colors:", colors)
print("First color:", colors[0])
print("Last color:", colors[-1])
print("Colors 2-4:", colors[1:4])

# 3. WHY TUPLES CAN'T BE CHANGED
# ===============================

print("\nTUPLES ARE IMMUTABLE:")

# This works with lists
my_list = [1, 2, 3]
my_list[0] = 100  # OK
print("List changed:", my_list)

# This DOESN'T work with tuples
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # ERROR! Cannot change tuple
print("Tuple unchanged:", my_tuple)

# 4. TUPLE OPERATIONS
# ===================

print("\nTUPLE OPERATIONS:")

# Concatenation (joining tuples)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Combined tuples:", combined)

# Repetition
repeated = tuple1 * 3
print("Repeated tuple:", repeated)

# Length
print("Length of tuple:", len(tuple1))

# Check if item exists
print("Is 2 in tuple?", 2 in tuple1)
print("Is 10 in tuple?", 10 in tuple1)

# 5. UNPACKING TUPLES
# ===================

print("\nUNPACKING TUPLES:")

# Packing values into tuple
student = ("Alice", 20, "Computer Science")
print("Student tuple:", student)

# Unpacking tuple into variables
name, age, major = student
print("Unpacked:")
print("  Name:", name)
print("  Age:", age)
print("  Major:", major)

# Multiple assignment (tuple unpacking)
x, y, z = 10, 20, 30
print(f"\nx={x}, y={y}, z={z}")

# Swap values easily
a, b = 5, 10
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a  # Swap using tuple unpacking
print(f"After swap: a={a}, b={b}")

# 6. WHEN TO USE TUPLES
# =====================

print("\n" + "=" * 50)
print("WHEN TO USE TUPLES VS LISTS")
print("=" * 50)

print("""
USE TUPLES WHEN:
1. Data should not change (days of week, months)
2. Using as dictionary keys (tuples can, lists cannot)
3. Function returns multiple values
4. You need better performance

USE LISTS WHEN:
1. Data needs to change (shopping cart, to-do list)
2. Need to add/remove items
3. Need to sort or reorder
4. Building dynamic collections

EXAMPLE USE CASES:
Tuples: coordinates (x,y), RGB colors, database records
Lists: user inputs, game scores, file contents
""")

# 7. PRACTICAL EXAMPLES
# =====================

print("\nPRACTICAL EXAMPLES:")

# Example 1: RGB Color codes
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
print("RGB Colors:")
print("  Red:", red)
print("  Green:", green)
print("  Blue:", blue)

# Example 2: Coordinate points
point1 = (10, 20)
point2 = (30, 40)
print("\nCoordinates:")
print("  Point 1:", point1)
print("  Point 2:", point2)

# Example 3: Function returning multiple values
def get_min_max(numbers):
    """Return both minimum and maximum"""
    return min(numbers), max(numbers)

result = get_min_max([5, 2, 8, 1, 9])
print("\nMin and Max:", result)
min_val, max_val = result  # Unpack
print(f"Min: {min_val}, Max: {max_val}")

# 8. CONVERTING BETWEEN LISTS AND TUPLES
# =======================================

print("\nCONVERTING LISTS ↔ TUPLES:")

# List to tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)
print("List to tuple:", my_list, "→", my_tuple)

# Tuple to list
my_tuple = (5, 6, 7, 8)
my_list = list(my_tuple)
print("Tuple to list:", my_tuple, "→", my_list)

# 9. PRACTICE PROBLEMS
# ====================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

print("""
Problem 1: Create a tuple of weekdays

Problem 2: Write a function that accepts (x,y) coordinates
           and returns distance from origin (0,0)

Problem 3: Create a student record tuple and unpack it

Problem 4: Count vowels in a tuple of letters

Problem 5: Check if a tuple is a palindrome
           (reads same forwards and backwards)
""")

# Solutions
print("\nSOLUTIONS:")

# Problem 1
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print("1. Weekdays:", weekdays)

# Problem 2
def distance_from_origin(point):
    x, y = point
    return (x**2 + y**2) ** 0.5
print("2. Distance of (3,4) from origin:", distance_from_origin((3,4)))

# Problem 3
student = ("Bob", 22, "Physics")
name, age, subject = student
print(f"3. Student: Name={name}, Age={age}, Subject={subject}")

# Problem 4
def count_vowels(letters):
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for letter in letters:
        if letter.lower() in vowels:
            count += 1
    return count
letters_tuple = ('a', 'b', 'e', 'd', 'i', 'o', 'u')
print("4. Vowels in tuple:", count_vowels(letters_tuple))

# Problem 5
def is_palindrome(t):
    return t == t[::-1]
print("5. Is (1,2,3,2,1) palindrome?", is_palindrome((1,2,3,2,1)))
print("   Is (1,2,3) palindrome?", is_palindrome((1,2,3)))