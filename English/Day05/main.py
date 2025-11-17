import string
import random

print("\n*** Password Generator ***\n")

numbers = string.digits
symbols = string.punctuation
letters = string.ascii_letters

num_letters = int(input("How many letters do you want in your password? "))
num_numbers = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

password = []

for _ in range(num_letters):
    password.append(random.choice(letters))

for _ in range(num_numbers):
    password.append(random.choice(numbers))

for _ in range(num_symbols): 
    password.append(random.choice(symbols))
    
random.shuffle(password)

final_password = "".join(password)
print(f"Your password is: {final_password}")