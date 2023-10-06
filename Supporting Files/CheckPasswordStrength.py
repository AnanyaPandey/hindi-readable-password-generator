# STRENGTH CHECK

import random
import string
import re
import requests

# List of common English words (you can extend this list)
common_words = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "guitar",
    "happiness", "internet", "jazz", "kangaroo", "lemon", "mango", "november",
    "ocean", "piano", "quilt", "rainbow", "sunshine", "tiger", "umbrella",
    "victory", "wonder", "xylophone", "yellow", "zebra"
]

# Function to generate a strong password from two random words
def generate_strong_password():
    word1 = random.choice(common_words)
    word2 = random.choice(common_words)
    
    # Generate a random digit and a random special character
    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)
    
    # Combine the words, digit, and special character to create the password
    password = f"{word1.capitalize()}{word2.capitalize()}{digit}{special_char}"
    
    return password

def check_password_strength(password):
    # Check if the password length is at least 8 characters
    if len(password) < 8:
        return "Weak: Password is too short (minimum length is 8 characters)."

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."

    # Check if the password contains at least one special character
    if not any(char in string.punctuation for char in password):
        return "Weak: Password must contain at least one special character."

    # Check if the password is not a common password or a dictionary word
    if is_common_password(password):
        return "Weak: Password is too common."

    # Password meets all complexity criteria
    return "Strong: Password is strong."

def is_common_password(password):
    # Check if the password is in a list of common passwords or dictionary words
    common_passwords_url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt"
    response = requests.get(common_passwords_url)
    common_passwords = response.text.splitlines()
    return password.lower() in common_passwords

# Example usage
password = generate_strong_password()
print(check_password_strength(password))
print("Generated strong password:", password)