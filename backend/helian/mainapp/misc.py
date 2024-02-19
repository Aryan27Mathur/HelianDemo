import requests
import csv
#from models import Company
import json

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



def testEmails():
    url = 'http://localhost:8000/newuser/'
    data = {'name': 'John Doe', 'email': 'john@example.com'}
    response = requests.post(url, json=data)

    print(response.json())  # Output: {'message': 'User created successfully'}

def testAddReport():
    # Replace with your Django development server URL
    url = 'http://localhost:8000/add_esg_report/'
    # Sample payload with company symbol and esg_report link
    data = {
        'symbol': 'AAPL',
        'esg_report': 'https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2023.pdf'
    }

    # Send a POST request to the endpoint
    response = requests.post(url, json=data)
    # Print the response
    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    # csv_file_path = 'constituents.csv'
    # populate_companies_from_csv(csv_file_path)
    testAddReport()


