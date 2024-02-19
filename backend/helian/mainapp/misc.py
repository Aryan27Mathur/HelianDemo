import requests
import csv
from models import Company

def populate_companies_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            company = Company.objects.create(
                symbol=row['Symbol'],
                name=row['Name'],
                sector=row['Sector']
            )
            company.save()

if __name__ == '__main__':
    csv_file_path = 'constituents.csv'
    populate_companies_from_csv(csv_file_path)

def testEmails():
    url = 'http://localhost:8000/newuser/'
    data = {'name': 'John Doe', 'email': 'john@example.com'}
    response = requests.post(url, json=data)

    print(response.json())  # Output: {'message': 'User created successfully'}


