import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    char_sets = ""
    if use_letters:
        char_sets += string.ascii_letters
    if use_numbers:
        char_sets += string.digits
    if use_symbols:
        char_sets += string.punctuation
    if not char_sets:
        char_sets = string.ascii_letters

    password = ''.join(random.choice(char_sets) for _ in range(length))
    
    return password

def main():
 
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"Your generated password is: {password}")

if __name__ == "__main__":
    main()