
# Python Data Structures Assignment

# 1. List: Create, update, search, and display
students = ["Akshay", "Rahul", "Priya"]
print("Original List:", students)

students.append("Amit")
students[0] = "Akshay Kumar"

if "Priya" in students:
    print("Priya found in the list")

print("Updated List:", students)

# 2. Tuple: Store and display fixed data
subjects = ("Python", "Java", "SQL")
print("\nSubjects Tuple:", subjects)
print("First Subject:", subjects[0])

if "Python" in subjects:
    print("Python found in the tuple")

# 3. Set: Store unique values and update
numbers = {10, 20, 30, 20}
print("\nOriginal Set:", numbers)

numbers.add(40)
numbers.discard(10)

if 20 in numbers:
    print("20 found in the set")

print("Updated Set:", numbers)

# 4. Dictionary: Create, update, search, and display
student = {
    "name": "Akshay",
    "age": 22,
    "course": "Python"
}
print("\nOriginal Dictionary:", student)

student["age"] = 23
student["city"] = "Mumbai"

if "name" in student:
    print("Student Name:", student["name"])

print("Updated Dictionary:", student)

# 5. Loop and condition
print("\nStudent Names:")
for name in students:
    if name:
        print(name)

print("\nAssignment completed successfully!")
