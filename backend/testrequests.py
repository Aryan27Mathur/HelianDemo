import requests

# URL of the Flask app
base_url = 'http://127.0.0.1:5000'

# Example POST request to add an email
def add_email(email):
    endpoint = '/email'
    url = base_url + endpoint
    data = {'email': email}
    response = requests.post(url, json=data)
    return response.json()

# Example GET request to retrieve all emails
def get_emails():
    endpoint = '/getEmails'
    url = base_url + endpoint
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    # Example usage
    email = 'aryan@example.com'

    # Add an email
    #print(add_email(email))

    # Retrieve all emails
    print(get_emails())
