"""
PYTHON DICTIONARIES - COMPLETE GUIDE FOR BEGINNERS
Dictionary = collection of key-value pairs
"""

print("=" * 50)
print("DICTIONARIES BASICS")
print("=" * 50)

# 1. CREATING DICTIONARIES
# ========================

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Simple dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}
print("\nStudent dictionary:", student)

# Dictionary with different data types
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science", "English"],
    "gpa": 3.8
}
print("\nPerson dictionary:", person)

# 2. ACCESSING VALUES
# ===================

print("\nACCESSING VALUES:")

# Access by key
print("Student name:", student["name"])
print("Student age:", student["age"])

# Safe access with get() (no error if key doesn't exist)
print("Student grade (get):", student.get("grade"))
print("Student city (get):", student.get("city"))  # Returns None
print("Student city (get with default):", student.get("city", "Not specified"))

# 3. ADDING & CHANGING VALUES
# ===========================

print("\nADDING & CHANGING VALUES:")

# Create dictionary
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print("Original car:", car)

# Add new key-value
car["color"] = "Blue"
print("After adding color:", car)

# Change existing value
car["year"] = 2021
print("After changing year:", car)

# 4. REMOVING ITEMS
# =================

print("\nREMOVING ITEMS:")

# Remove specific key
car.pop("color")
print("After removing color:", car)

# Remove using del
del car["model"]
print("After deleting model:", car)

# Remove all items
car.clear()
print("After clear:", car)

# 5. DICTIONARY OPERATIONS
# ========================

print("\nDICTIONARY OPERATIONS:")

# Create new dictionary
book = {
    "title": "Python Guide",
    "author": "John Doe",
    "pages": 300,
    "price": 29.99
}

# Check if key exists
print("Has title?", "title" in book)
print("Has publisher?", "publisher" in book)

# Get all keys
print("Keys:", book.keys())

# Get all values
print("Values:", book.values())

# Get all items (key-value pairs)
print("Items:", book.items())

# Length of dictionary
print("Number of items:", len(book))

# 6. LOOPING THROUGH DICTIONARIES
# ===============================

print("\nLOOPING THROUGH DICTIONARIES:")

# Loop through keys
print("Loop through keys:")
for key in book:
    print(f"  Key: {key}")

# Loop through values
print("\nLoop through values:")
for value in book.values():
    print(f"  Value: {value}")

# Loop through items (key-value pairs)
print("\nLoop through items:")
for key, value in book.items():
    print(f"  {key}: {value}")

# 7. NESTED DICTIONARIES
# ======================

print("\n" + "=" * 50)
print("NESTED DICTIONARIES")
print("=" * 50)

# Dictionary inside dictionary
school = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 88]
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": [78, 85, 92]
    }
}

print("Nested dictionary:")
print("Student 1 name:", school["student1"]["name"])
print("Student 2 age:", school["student2"]["age"])
print("Student 1 grades:", school["student1"]["grades"])

# 8. PRACTICAL EXAMPLES
# =====================

print("\nPRACTICAL EXAMPLES:")

# Example 1: Phone book
phone_book = {
    "John": "555-1234",
    "Sarah": "555-5678",
    "Mike": "555-9012"
}
print("Phone Book:")
for name, number in phone_book.items():
    print(f"  {name}: {number}")

# Example 2: Word counter
def count_words(text):
    """Count how many times each word appears"""
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

text = "hello world hello python world python hello"
result = count_words(text)
print("\nWord count:", result)

# Example 3: Student grades system
grades = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "History": 88
}

# Calculate average
average = sum(grades.values()) / len(grades)
print(f"\nGrades: {grades}")
print(f"Average grade: {average:.2f}")

# Find highest grade
highest_subject = max(grades, key=grades.get)
print(f"Highest grade: {highest_subject} ({grades[highest_subject]})")

# 9. COMMON DICTIONARY METHODS
# ============================

print("\nCOMMON DICTIONARY METHODS:")

# copy() - create a copy
original = {"a": 1, "b": 2, "c": 3}
copy_dict = original.copy()
copy_dict["d"] = 4
print("Original:", original)
print("Copy:", copy_dict)

# update() - merge dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print("\nAfter update:", dict1)

# setdefault() - get value or set default
fruit_prices = {"apple": 1.0, "banana": 0.5}
print("\nApple price:", fruit_prices.setdefault("apple", 1.2))
print("Orange price (default):", fruit_prices.setdefault("orange", 0.8))
print("Updated prices:", fruit_prices)

# 10. PRACTICE PROBLEMS
# =====================

print("\n" + "=" * 50)
print("PRACTICE PROBLEMS")
print("=" * 50)

print("""
Problem 1: Create a dictionary of 5 countries and their capitals

Problem 2: Write a function that counts letter frequency in a string

Problem 3: Create a shopping cart dictionary with items and prices

Problem 4: Merge two dictionaries

Problem 5: Find the most frequent word in a string
""")

# Solutions
print("\nSOLUTIONS:")

# Problem 1
countries = {
    "USA": "Washington DC",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Brazil": "Brasilia"
}
print("1. Countries and capitals:")
for country, capital in countries.items():
    print(f"  {country}: {capital}")

# Problem 2
def letter_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():  # Only count letters
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

text = "hello world"
print(f"\n2. Letter frequency in '{text}':")
freq = letter_frequency(text)
for letter, count in sorted(freq.items()):
    print(f"  {letter}: {count}")

# Problem 3
cart = {
    "apple": 1.20,
    "banana": 0.50,
    "milk": 2.50,
    "bread": 1.80
}
print("\n3. Shopping cart:")
total = 0
for item, price in cart.items():
    print(f"  {item}: ${price}")
    total += price
print(f"  Total: ${total:.2f}")

# Problem 4
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
merged = {**dict_a, **dict_b}
print("\n4. Merged dictionaries:", merged)

# Problem 5
def most_frequent_word(text):
    words = text.lower().split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    # Find word with max frequency
    most_freq = max(freq, key=freq.get)
    return most_freq, freq[most_freq]

text = "the quick brown fox jumps over the lazy dog the fox"
word, count = most_frequent_word(text)
print(f"\n5. Most frequent word: '{word}' (appears {count} times)")