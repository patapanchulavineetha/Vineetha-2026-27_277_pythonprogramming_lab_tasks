def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# Call the function
student_details(name="Krishna", Maths=90, Science=85, English=95)
