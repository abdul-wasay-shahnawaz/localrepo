# 1. Greeting function
def greetings(name):
    print(f"Welcome to SMIT training center, {name}")

greetings("Ahsan")
# 2. Positive / Negative / Zero checker
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))
# 3. Larger between two numbers
def larger_two(a, b):
    return a if a > b else b

print(larger_two(10, 25))
# 4. Largest among three numbers
def largest_three(a, b, c):
    return max(a, b, c)

print(largest_three(10, 25, 15))
# 5. Age category
def check_age(age):
    if age < 18:
        return "Minor"
    elif age <= 60:
        return "Adult"
    else:
        return "Senior Citizen"

print(check_age(45))
# 6. Even or Odd
def even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print(even_odd(7))
# 7. Square of a number
def square(num):
    return num ** 2

print(square(6))
# 8. Circle Area & Circumference
import math

def circle(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference
# 9. Pass or Fail
def check_result(score):
    return "Pass" if score > 60 else "Fail"

print(check_result(75))
# 10. Factorial (Recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
# 1. Student Info List
student = ["Ahsan", 20, "AI and Data Science", True]
for item in student:
    print(item)
print(circle(7))
# 2. Separate data types
data = ["Apple", 44, 74, True, "Data Science", False]
strings = []
numbers = []
booleans = []

for item in data:
    if isinstance(item, str):
        strings.append(item)
    elif isinstance(item, int):
        numbers.append(item)
    elif isinstance(item, bool):
        booleans.append(item)

print("Strings:", strings)
print("Numbers:", numbers)
print("Booleans:", booleans)
# 3. Fruits List Tasks
fruits = ["apple", "raspberry", "pineapple", "cherry"]

# a. Check presence
print("apple" in fruits)

# b. Replace raspberry and pineapple with orange
fruits[1] = "orange"
fruits[2] = "orange"

# c. Insert apricot at index 2
fruits.insert(2, "apricot")
# 4. Extend List
items = ["apple", "banana"]
items.extend(["car", "bike", "aeroplane"])
print(items)
# 5. Best Scores
scores = [400, 89, 90, 95, 23, 50]
scores.sort(reverse=True)
print("First Best:", scores[0])
print("Second Best:", scores[1])
# 6. Sorting & Average
numbers = [32, 54, 6, 12, 71, 10, 9]

# Remove numbers less than 20
numbers = [n for n in numbers if n >= 20]

# Sort ascending & descending
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))

# Average
avg = sum(numbers) / len(numbers)
print("Average:", avg)
# 7. Gadgets List
gadgets = ["Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

strings = [g for g in gadgets if isinstance(g, str)]
numbers = [g for g in gadgets if isinstance(g, (int, float))]

print("Strings Asc:", sorted(strings))
print("Strings Desc:", sorted(strings, reverse=True))
print("Numbers Asc:", sorted(numbers))
print("Numbers Desc:", sorted(numbers, reverse=True))


print(fruits)

             
