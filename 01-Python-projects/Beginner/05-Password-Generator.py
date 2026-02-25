import random
import string

chars = list(string.ascii_letters)
numbers = list(string.digits)
spcl_chars = list(string.punctuation)
password = []

print("Welcome to the PyPassword Generator!")
num_of_letters=int(input("How many letters would you like in your password?"))
num_of_numbers=int(input("How many numbers would you like?"))
num_of_spclChars=int(input("How many symbols would you like?"))

for i in range(num_of_letters):
    password.append(random.choice(chars))
for i in range(num_of_numbers):
    password.append(random.choice(numbers))
for i in range(num_of_spclChars):
    password.append(random.choice(spcl_chars))
random.shuffle(password)

result= ""
for i in password:
    result += i
print(result)


