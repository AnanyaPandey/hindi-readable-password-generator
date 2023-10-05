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
    "Tez", "Teekha", "Udta", "Langda", "Jhagdalu", "Budbak", "Gaddar", "Bhutiya"
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
    "Khidki", "Darwaza", "Mahal", "Gulaab"
]


def replace_characters(word):
    # Replace 's' with '$', 'o' with '0'
    word = word.replace('s', '$')
    word = word.replace('o', '0')
    return word


def generate_strong_password(password_length):
    if password_length < 6:
        return "Password length is too short (minimum length is 6 characters)."

    while True:
        word1 = random.choice(hindi_words_transliterated)
        word2 = random.choice(hindi_words_transliterated2)
        if word1 != word2:
            break

    word1 = replace_characters(word1).capitalize()
    word2 = replace_characters(word2).capitalize()

    digit = random.choice(string.digits)
    special_char = random.choice(string.punctuation)

    password = [word1, word2, digit, special_char]

    indicestoshuffle = [0, 2, 3]
    shuffled_elements = random.sample([password[i] for i in indicestoshuffle], len(indicestoshuffle))
    random.shuffle(shuffled_elements)
    for i, index in enumerate(indicestoshuffle):
        password[index] = shuffled_elements[i]

    password = ''.join(map(str, password))
    readable = f"{word1} {word2}"

    return password, readable


def generate_passwords():
    password_length = 11
    p1, p1_r = generate_strong_password(password_length)
    p2, p2_r = generate_strong_password(password_length)
    p3, p3_r = generate_strong_password(password_length)
    p4, p4_r = generate_strong_password(password_length)
    password = [p1, p2, p3, p4]
    readables = [p1_r, p2_r, p3_r, p4_r]

    for i, each in enumerate(password):
        print(f"Generated Strong Password: {i + 1}. {readables[i]} - {each}")

    return password


def main():
    try:
        while True:
            passwords = generate_passwords()
            choice = int(input("Press Number to Copy or 11 to Regenerate: "))
            if choice != 11:
                if 1 <= choice <= len(passwords):
                    pyperclip.copy(passwords[choice - 1])
                    copied_text = pyperclip.paste()
                    if copied_text == passwords[choice - 1]:
                        print("Password copied to clipboard successfully!")
                        save_choice = input("What app or account do you want to save this with: ")
                        row = [passwords[choice - 1], save_choice]
                        print(row)
                        time.sleep(3)
                    else:
                        print("Copying to clipboard failed.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
            elif choice == 11:
                pass
    except ValueError:
        print('Exiting')


if __name__ == "__main__":
    main()
