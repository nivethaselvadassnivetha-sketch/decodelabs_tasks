import random
import string
length=int(input("Enter the length of Password:"))
characters=string.ascii_letters+string.digits+"!@#$%^&*"
password=""
for i in range(length):
    password=password+random.choice(characters)
print("Generated Password:",password)