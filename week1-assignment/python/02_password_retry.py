"""
Assignment 02 — Password Retry

Simple login with three attempts; locks on failure (default password in `correct_password`).
"""

def login_system() -> None:
    correct_password = "openAI123"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password = get_password_input()
        if password == correct_password:
            print("Login successful!")
            break
        else:
            attempts += 1
            print(f"Incorrect password. You have {max_attempts - attempts} attempts left.")

    if attempts == max_attempts:
        print("Account locked due to too many failed attempts.")    

def get_password_input() -> str:
    return input("Enter your password: ")


if __name__ == "__main__":
    login_system()    
