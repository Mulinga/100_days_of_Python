import random
import string

def generate_password():
    # Ask user for counts
    num_letters = int(input("How many letters would you like in your password? "))
    num_symbols = int(input("How many symbols would you like? "))
    num_numbers = int(input("How many numbers would you like? "))

    # Define character sets
    letters = string.ascii_letters  # includes both uppercase and lowercase
    symbols = "!@#$%^&*()-_=+[]{};:,.<>/?"
    numbers = string.digits

    # Pick random characters from each category
    password_chars = []
    password_chars += random.choices(letters, k=num_letters)
    password_chars += random.choices(symbols, k=num_symbols)
    password_chars += random.choices(numbers, k=num_numbers)

    # Shuffle the characters so password is in random order
    random.shuffle(password_chars)

    # Join list into a string
    password = "".join(password_chars)

    print(f"Your generated password is: {password}")

generate_password()
