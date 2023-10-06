import random
import string

# List of Hindi words transliterated to English (you can extend this list)
hindi_words_transliterated = [
    "pyaar", "khushi", "dil", "duniya", "zindagi", "sapna", "rishta",
    "dharti", "aasmaan", "sooraj", "chaand", "mausam", "mohabbat", "khuda",
    "pyaas", "raah", "manzil", "safar", "yaad", "khwaab", "dhadkan",
    "aankhein", "musafir", "parchhai", "hawaa", "humsafar"
]

# Function to replace characters in a word
def replace_characters(word):
    # Replace 's' with '$', 'o' with '0'
    word = word.replace('s', '$')
    word = word.replace('o', '0')
    return word

# Function to generate a strong password
def generate_strong_password(password_length):
    if password_length <= 7:
        return "Password length is too short (minimum length is 8 characters)."

    # Select two random transliterated Hindi words
    word1 = random.choice(hindi_words_transliterated)
    word2 = random.choice(hindi_words_transliterated)

    # Replace characters and capitalize the first letter of each word
    word1 = replace_characters(word1).capitalize()
    word2 = replace_characters(word2).capitalize()

    # Generate a random digit
    digit = random.choice(string.digits)

    # Generate a random special character
    special_char = random.choice(string.punctuation)

    # Combine the words, digit, and special character to create the password
    password = word1 + word2 + digit + special_char

    # If the password length is greater than the required length, truncate it
    if len(password) > password_length:
        password = password[:password_length]

    return password

# Get the desired password length from the user
try:
    password_length = int(input("Enter the desired password length: "))
    password = generate_strong_password(password_length)
    print("Generated strong password:", password)
except ValueError:
    print("Invalid input. Please enter a valid integer for the password length.")