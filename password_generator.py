import secrets
import string

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure password.

    Args:
        length (int): The desired length of the password. Defaults to 12.
        use_lower (bool): Include lowercase letters. Defaults to True.
        use_upper (bool): Include uppercase letters. Defaults to True.
        use_digits (bool): Include digits. Defaults to True.
        use_symbols (bool): Include special symbols. Defaults to True.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the length is less than 1 or no character set is selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    character_sets = []
    if use_lower:
        character_sets.append(string.ascii_lowercase)
    if use_upper:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected")

    alphabet = ''.join(character_sets)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    """
    Main function to run the password generator and print the output.
    """
    print("Welcome to the Secure Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive integer. Please try again.")
                continue  # Go back to the beginning of the while loop
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")

    use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    use_symbols = input("Include special symbols? (yes/no): ").lower() == 'yes'

    try:
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print(f"\nYour generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
        print("Please ensure you select at least one character set (lowercase, uppercase, digits, or symbols).")

if __name__ == "__main__":
    main()
