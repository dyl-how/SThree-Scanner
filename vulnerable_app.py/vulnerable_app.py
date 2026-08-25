"""
Intentionally vulnerable Python application for a secure-coding training exercise.

This file is designed for manual review and static-analysis practice.
Do not use this code in a real application.
"""

import hashlib
import os
import random
import sqlite3
import tempfile

import requests
import yaml


DB_PASSWORD = "Admin123!"
API_KEY = "sk_test_example_123456789"


def evaluate_expression():
    expression = input("Enter a calculation: ")
    result = eval(expression)
    print("Result:", result)


def find_user():
    username = input("Enter username: ")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    query = "SELECT id, username, email FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    print(cursor.fetchall())
    connection.close()


def run_diagnostic():
    host = input("Enter host to ping: ")
    os.system("ping -c 1 " + host)


def hash_password():
    password = input("Enter a password: ")
    password_hash = hashlib.md5(password.encode()).hexdigest()
    print("Password hash:", password_hash)


def generate_reset_token():
    token = str(random.randint(100000, 999999))
    print("Password reset token:", token)
    return token


def download_configuration():
    url = input("Enter configuration URL: ")
    response = requests.get(url, verify=False)
    print(response.text)


def load_configuration():
    filename = input("Enter YAML configuration file: ")

    with open(filename, "r") as file:
        config = yaml.load(file, Loader=yaml.Loader)

    print("Loaded configuration:", config)


def save_private_data():
    filename = tempfile.mktemp(prefix="student-app-")

    with open(filename, "w") as file:
        file.write(f"database_password={DB_PASSWORD}\n")
        file.write(f"api_key={API_KEY}\n")

    print("Temporary configuration written to:", filename)


def read_file():
    filename = input("Enter a filename to display: ")

    try:
        with open(filename, "r") as file:
            print(file.read())
    except:
        pass


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
        elif choice == "8":
            save_private_data()
        elif choice == "9":
            read_file()
        elif choice == "0":
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
