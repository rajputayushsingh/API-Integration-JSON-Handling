# API Integration & JSON Handling
# This program fetches user data from a public API,
# parses JSON, allows searching by name,
# and handles possible errors.

import requests

# Public API URL
API_URL = "https://jsonplaceholder.typicode.com/users"

try:
    # Send GET request
    response = requests.get(API_URL, timeout=10)

    # Raise an exception if request failed
    response.raise_for_status()

    # Convert JSON response into Python list
    users = response.json()

    print("=== User List ===")
    for user in users:
        print(f"{user['id']}. {user['name']} - {user['email']}")

    # Search functionality
    search = input("\nEnter a user name to search: ").lower()

    print("\n=== Search Result ===")
    found = False

    for user in users:
        if search in user["name"].lower():
            print(f"Name   : {user['name']}")
            print(f"Email  : {user['email']}")
            print(f"City   : {user['address']['city']}")
            print(f"Company: {user['company']['name']}")
            print("-" * 30)
            found = True

    if not found:
        print("No matching user found.")

except requests.exceptions.HTTPError:
    print("HTTP Error! Unable to fetch data.")

except requests.exceptions.ConnectionError:
    print("Connection Error! Check your internet.")

except requests.exceptions.Timeout:
    print("Request Timed Out!")

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)