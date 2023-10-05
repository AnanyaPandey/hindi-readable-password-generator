import random

# List of common English words (you can extend this list)
common_words = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "guitar",
    "happiness", "internet", "jazz", "kangaroo", "lemon", "mango", "november",
    "ocean", "piano", "quilt", "rainbow", "sunshine", "tiger", "umbrella",
    "victory", "wonder", "xylophone", "yellow", "zebra"
]

# Function to generate a password from random words
def generate_password(num_words=3):
    if num_words < 1:
        return "Invalid input"

    password = ""
    for _ in range(num_words):
        word = random.choice(common_words)
        password += word.capitalize()  # Capitalize the first letter of each word
        password += str(random.randint(1, 9))  # Add a random digit
        password += random.choice("!@#$%^&*")  # Add a random special character
    return password

# Example usage
num_words = 3  # You can change this to generate passwords with more words
password = generate_password(num_words)
print("Generated password:", password)