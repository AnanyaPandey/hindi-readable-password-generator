import random
import string
import pyperclip
import time

# List of Hindi words transliterated to English (you can extend this list)
hindi_words_transliterated = [
 "Sundar", "Sukha", "Pyaara", "Chhota", "Mota", "Bura", "Khoobsurat", 
    "Swasth", "Garib", "Ameer", "Shant", "Jhulta", "Majedar", "Garam", 
    "Thanda", "Naya", "Purana", "Lal", "Hara", "Neela", "Safed", "Kala", 
    "Sukhi", "Dhaniya", "Lamba", "Samridh", "Sachcha", "Jhoota", "Sharif",
    "Tez","Teekha","Udta","Langda","Jhagdalu","Budbak","Gaddar","Bhutiya"
]

hindi_words_transliterated2 = [
    "Kanya",  # Love (Noun)
    "Talwar",  # Happiness (Noun)
    "Teer",  # Journey (Noun)
    "Tyagi",  # Heart (Noun)
    "Chhatri",  # Weather (Noun)
    "Maal",  # Life (Noun)
    "Rasta",  # Roads (Noun)
    "Mazdur",  # World (Noun)
    "kitab",  # Book (Noun)
    "kaagaz",  # Paper (Noun)
    "kursi",  # Chair (Noun)
    "botal",  # Bottle (Noun)
    "raja",  # King (Gangster Name)
    "don",  # Don (Gangster Name)
    "bhai",  # Brother (Gangster Name)
    "Shakeel",  # The Biggest (Gangster Name)
    "gunda",  # Goon (Gangster Name)
    "Aurat",  # Lioness (Gangster Name)
    "Panchi",  # God (Gangster Name)
    "Khidki","Darwaza","Mahal","Gulaab"
]

# Function to replace characters in a word
def replace_characters(word):
    # Replace 's' with '$', 'o' with '0'
    word = word.replace('s', '$')
    word = word.replace('o', '0')
    return word

# Function to generate a strong password
def generate_strong_password(password_length):
    if password_length < 6:
        return "Password length is too short (minimum length is 6 characters)."

    # Select two random transliterated Hindi words with different lengths
    while True:
        word1 = random.choice(hindi_words_transliterated)
        word2 = random.choice(hindi_words_transliterated2)
        if word1 != word2:
            break

    # Replace characters and capitalize the first letter of each word
    word1 = replace_characters(word1).capitalize()
    word2 = replace_characters(word2).capitalize()

    # Generate a random digit
    digit = random.choice(string.digits)

    # Generate a random special character
    special_char = random.choice(string.punctuation)

    # Combine the words, digit, and special character to create the password
    
    #password = word1 + word2 + digit + special_char
    password = [word1,word2,digit,special_char]

    indicestoshuffle=[0,2,3]
    shuffled_elements = random.sample([password[i] for i in indicestoshuffle], len(indicestoshuffle))
    random.shuffle(shuffled_elements)
    for i, index in enumerate(indicestoshuffle):
        password[index] = shuffled_elements[i]
    
    password = ''.join(map(str, password))
    readable = f"{word1} {word2}"
    # If the password length is greater than the required length, truncate it
    # if len(password) > password_length:
    #    password = password[:password_length]

    return password,readable

# Get the desired password length from the user
def generatePasswords():
    password_length = 11
    p1,p1_r = generate_strong_password(password_length)
    p2,p2_r = generate_strong_password(password_length)
    p3,p3_r = generate_strong_password(password_length)
    p4,p4_r = generate_strong_password(password_length)
    password=[p1,p2,p3,p4]
    readables=[p1_r,p2_r,p3_r,p4_r]

    # Printing the Passwords
    for i,each in enumerate(password):
        print(f"Generated Strong Password: {i+1}. {readables[i]} - {each}")

    return password
try: 
    while True:
        password=generatePasswords()
        # Asking User if we should Copy the password to clipboard
        choice = int(input("Press Number to Copy or 11 to Regenerate"))
        if choice != 11:        
            pyperclip.copy(password[choice-1])
            copied_text = pyperclip.paste()
            # Checking if passworf copied to clipboard
            if copied_text == password[choice-1]:
                print("Variable copied to clipboard successfully!")
                savechoice = input("What app or account do you want to save this with: ")
                row = [password[choice-1],savechoice]
                print(row)
                time.sleep(3)
            else:
                print("Copying to clipboard failed.")
            break
        elif choice == 11:
            pass
except ValueError:
    print('Exiting')



