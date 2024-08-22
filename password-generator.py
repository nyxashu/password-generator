import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a secure password based on user-defined criteria."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")
    
    # Define possible characters
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length (minimum 1): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
