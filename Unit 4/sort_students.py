students = [
    {"name": "Vineetha", "marks": 90},
    {"name": "Anusha", "marks": 85},
    {"name": "Krishna", "marks": 95}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
print(ascending)

print("Descending Order:")
print(descending)
