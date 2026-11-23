balance = 1000

def deposit(amount):
    global balance
    balance += amount
    print("After deposit:", balance)

def local_deposit(amount):
    balance = 500
    balance += amount
    print("Local balance:", balance)

print("Initial balance:", balance)

deposit(500)

local_deposit(200)

print("Final account balance:", balance)
