#task 3
import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: No character types selected."

    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(lower))  # Ensure at least one lowercase

    # Fill the rest of the password
    remaining_length = length - len(password)
    password += random.choices(all_chars, k=remaining_length)

    # Shuffle the list to randomize positions
    random.shuffle(password)

    return ''.join(password)

def password_generator_app():
    print("🔐 Welcome to the Password Generator!")

    try:
        length = int(input("Enter desired password length (e.g. 8, 12, 16): "))
        if length < 4:
            print("Password length should be at least 4.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print("\nYour generated password is:")
    print(f"👉 {password}")

# Run the apprr
password_generator_app()
