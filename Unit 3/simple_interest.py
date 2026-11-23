def simple_interest(principal, time, rate=5):
    si = (principal * time * rate) / 100
    return si

# Using default rate
result1 = simple_interest(1000, 2)
print("Simple Interest (Default Rate):", result1)

# Using explicit rate
result2 = simple_interest(1000, 2, 10)
print("Simple Interest (Explicit Rate):", result2)
