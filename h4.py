import getpass
import hashlib

# Sample security questions
SECURITY_QUESTIONS = {
    "What is your pet's name?": "pet_name",
    "What is your mother's maiden name?": "maiden_name",
    "What is your favorite color?": "color"
}

# Simple database to store user credentials
USER_DATABASE = {}

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    """Register a new user with a textual password, graphical password, and security questions."""
    username = input("Enter a username: ")

    if username in USER_DATABASE:
        print("Username already exists!")
        return

    # Level 1: Textual Password
    password = getpass.getpass("Enter a password: ")
    hashed_password = hash_password(password)

    # Level 2: Graphical Password (Simulated with text choices)
    print("\nSelect a graphical password (sequence of choices):")
    graphical_choices = ["Red", "Blue", "Green"]  # Replace images with text choices
    graphical_password = []
    for i, choice in enumerate(graphical_choices):
        user_choice = input(f"Do you want to select {choice}? (y/n): ")
        if user_choice.lower() == 'y':
            graphical_password.append(choice)

    # Level 3: Security Questions
    security_answers = {}
    for question, key in SECURITY_QUESTIONS.items():
        answer = input(f"{question} ")
        security_answers[key] = hash_password(answer)

    USER_DATABASE[username] = {
        "password": hashed_password,
        "graphical_password": graphical_password,
        "security_answers": security_answers
    }

    print("\nRegistration successful!\n")

def authenticate_user():
    """Authenticate a user based on the three levels of security."""
    username = input("Enter your username: ")

    if username not in USER_DATABASE:
        print("Username not found!")
        return False

    # Level 1: Textual Password
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)
    if USER_DATABASE[username]["password"] != hashed_password:
        print("Incorrect password!")
        return False

    # Level 2: Graphical Password (Simulated with text choices)
    print("\nEnter your graphical password (sequence of choices):")
    graphical_choices = USER_DATABASE[username]["graphical_password"]
    for i, choice in enumerate(graphical_choices):
        user_choice = input(f"Did you select {choice} during registration? (y/n): ")
        if user_choice.lower() != 'y':
            print("Incorrect graphical password!")
            return False

    # Level 3: Security Questions
    print("\nAnswer the security questions:")
    for question, key in SECURITY_QUESTIONS.items():
        answer = input(f"{question} ")
        hashed_answer = hash_password(answer)
        if USER_DATABASE[username]["security_answers"][key] != hashed_answer:
            print("Incorrect answer to security question!")
            return False

    print("\nAuthentication successful!\n")
    return True

def main():
    while True:
        choice = input("1. Register\n2. Login\n3. Exit\nEnter your choice: ")
        if choice == '1':
            register_user()
        elif choice == '2':
            authenticate_user()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()