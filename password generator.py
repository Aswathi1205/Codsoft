import secrets
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Example usage
password_length = 12
print("Generated password:", generate_password(password_length))

