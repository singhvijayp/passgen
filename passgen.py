import string
import random

def generate_password(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

def get_password_difficulty():
    print("Select password difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please select a valid option (1, 2, or 3).")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

def main():
    difficulty = get_password_difficulty()
    
    if difficulty == 1:
        length = 8
        chars = string.ascii_lowercase
    elif difficulty == 2:
        length = 12
        chars = string.ascii_letters + string.digits
    elif difficulty == 3:
        length = 16
        chars = string.ascii_letters + string.digits + string.punctuation
    
    password = generate_password(length, chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
