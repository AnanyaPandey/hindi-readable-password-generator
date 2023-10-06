import random
import string

# List of transliterated Hindi words
hindi_words = ["kamal", "sundar", "masti", "khushi", "dhoom", "anand", "pyaar", "jhoom"]

# Randomly select two different words
word1, word2 = random.sample(hindi_words, 2)

# Randomly select a capital letter, a number, and a special character
capital_letter = random.choice(string.ascii_uppercase)
number = random.choice(string.digits)
special_char = random.choice(string.punctuation)

# Replace 's' with '$' and 'o' with '0' in the selected words
word1 = word1.replace('s', '$').replace('o', '0')
word2 = word2.replace('s', '$').replace('o', '0')

# Combine the words, capital letter, number, and special character to create the password
password = f"{word1}{word2}{capital_letter}{number}{special_char}"

# Shuffle the characters in the password
password = ''.join(random.sample(password, len(password)))

# Print the generated password
print("Generated Password:", password)