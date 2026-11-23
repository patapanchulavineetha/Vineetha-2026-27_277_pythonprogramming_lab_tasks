
def convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Call the function
c = 25

result = convert(c)

print("Temperature in Celsius:", c)
print("Temperature in Fahrenheit:", result)
