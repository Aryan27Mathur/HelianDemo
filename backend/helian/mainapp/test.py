import requests

url = 'http://localhost:8000/newuser/'
data = {'name': 'John Doe', 'email': 'john@example.com'}
response = requests.post(url, json=data)

print(response.json())  # Output: {'message': 'User created successfully'}
