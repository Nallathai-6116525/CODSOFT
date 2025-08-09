import random
import string

def generate_strong_password(length):
    """
    Generates a random password of a specified length.

    The password is created using a combination of lowercase letters,
    uppercase letters, digits, and punctuation marks.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: The generated random password.
    """
   
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    """
    Main function to run the password generator application.
    """
    try:
       
        length = int(input("Enter the desired password length: "))

        if length <= 0:
            print("Password length must be a positive number.")
            return

        password = generate_strong_password(length)

       
        print(f"\nYour generated password is: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")


if __name__ == "__main__":
    main()
