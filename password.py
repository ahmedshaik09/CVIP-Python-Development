import random
import string

def get_password_length():
    while True:
        try:
            password_length = int(input("Enter password length: "))
            if password_length < 8:
                print("Password length must be at least 8.")
            else:
                return password_length
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_password_character_types():
    print("\nSelect character types:")
    print("1. Lowercase")
    print("2. Uppercase")
    print("3. Numbers")
    print("4. Special characters")

    character_types = []
    while True:
        try:
            selection = int(input("Enter your selection (1-4): "))
            if selection == 1:
                character_types.append(string.ascii_lowercase)
            elif selection == 2:
                character_types.append(string.ascii_uppercase)
            elif selection == 3:
                character_types.append(string.digits)
            elif selection == 4:
                character_types.append(string.punctuation)
            else:
                print("Invalid selection. Please enter a number between 1 and 4.")
            return character_types
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(password_length, character_types):
    all_characters = "".join(character_types)
    password = []
    for i in range(password_length):
        password.append(random.choice(all_characters))
    return "".join(password)

def main():
    password_length = get_password_length()
    character_types = get_password_character_types()
    password = generate_password(password_length, character_types)
    print("\nGenerated password: ", password)

if __name__ == "__main__":
    main()