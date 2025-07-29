import random
import string

def generate_password(length, include_digits=True, include_symbols=True):
    characters = string.ascii_letters  # a-z + A-Z

    if include_digits:
        characters += string.digits     # 0-9

    if include_symbols:
        characters += string.punctuation  # !@#$%^&*()

    if length < 4:
        print("⚠️ Password should be at least 4 characters.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Welcome to Dhanya's Password Generator!\n")

    try:
        length = int(input("👉 Enter the desired password length: "))
    except ValueError:
        print("❌ Please enter a valid number!")
        return

    use_digits = input("🔢 Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("✨ Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_digits, use_symbols)

    if password:
        print("\n✅ Your generated password is:")
        print("🔑", password)

if __name__ == "__main__":
    main()