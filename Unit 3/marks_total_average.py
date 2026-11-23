def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average

# Call the function
a = 85
b = 90
c = 95

total, average = calculate(a, b, c)

print("Total marks:", total)
print("Average marks:", average)
