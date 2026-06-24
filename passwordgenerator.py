import random
import string 
class PasswordError(Exception):
   pass

def generate_password(length=12):
    all_characters=string.ascii_letters+string.digits+string.punctuation
    password= "".join(random.choice(all_characters)
    for _ in range(length))
    return password

user_password=input("Enter password")
try:
    if len (user_password)<8:
        raise PasswordError("Password is too short,It must contain more than 8 words")
    if not any(cahr.isdigit() for char in user_password):
        raise PasswordError("Your password must coontain numeric value")

    print("Valid Password")
except PasswordError as error:
    print(f"Rejected:{error}")


