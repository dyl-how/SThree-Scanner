''' Made as a 'safe' copy of the vulnerable_app.py, returns one low
risk issue being the importing of the subprocess module, but other than that is clean
showing that program does only flag actual issues
'''

# still flags some errors, mainly subprocess.run() and the blind except
# these are included due to contraints (catch wide errors, cant use alternative to subprocess)

import hashlib
import sqlite3
import ast
import subprocess
import secrets
import requests
import yaml

def evaluate_expression():
    expression = input("Enter a calculation: ")
    result = ast.literal_eval(expression)
    print("Result:", result)


def find_user():
    username = input("Enter username: ")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT ... WHERE username = ?", (username,)
    cursor.execute(query)

    print(cursor.fetchall())
    connection.close()


def run_diagnostic():
    host = input("Enter host to ping: ")
    subprocess.run(["ping", "-c", "1", host])


def hash_password():
    password = input("Enter a password: ")
    password_hash = hashlib.sha256(password.encode())
    print("Password hash:", password_hash)


def generate_reset_token():
    token = str(secrets.randbelow(900000) + 100000)
    print("Password reset token:", token)
    return token


def download_configuration():
    url = input("Enter configuration URL: ")
    response = requests.get(url, verify=True, timeout=5)
    print(response.text)


def load_configuration():
    filename = input("Enter YAML configuration file: ")

    with open(filename, "r") as file:
        config = yaml.safe_load(file)

    print("Loaded configuration:", config)


def read_file():
    filename = input("Enter a filename to display: ")

    try:
        with open(filename, "r") as file:
            print(file.read())
    except Exception as e: 
        print(f"Error: {e}")


def main():
    while True:
        print("\nSecurity Training Application")
        print("1. Evaluate expression")
        print("2. Find user")
        print("3. Run diagnostic")
        print("4. Hash password")
        print("5. Generate reset token")
        print("6. Download configuration")
        print("7. Load YAML configuration")
        print("8. Save private data")
        print("9. Read file")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            evaluate_expression()
        elif choice == "2":
            find_user()
        elif choice == "3":
            run_diagnostic()
        elif choice == "4":
            hash_password()
        elif choice == "5":
            generate_reset_token()
        elif choice == "6":
            download_configuration()
        elif choice == "7":
            load_configuration()
        elif choice == "9":
            read_file()
        elif choice == "0":
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
