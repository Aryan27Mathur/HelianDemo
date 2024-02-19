import requests
from exa_py import Exa
import csv
# Initialize Exa instance
exa = Exa("d520a7ba-2dc4-4109-8b9a-702c14eb3327")

# Function to get ESG report URL for a symbol
def get_esg_report_url(symbol):
    response = exa.search(
        f"{symbol} ESG Report 2023",
        num_results=1,
        use_autoprompt=True,
        type="keyword",
    )
    results = response.results
    if results:
        return results[0].url
    return None

# Function to send POST request to Django endpoint
def send_post_request(symbol, esg_report_url):
    url = 'https://helian-backend.onrender.com/add_esg_report/'
    data = {
        'symbol': symbol,
        'esg_report': esg_report_url
    }
    response = requests.post(url, json=data)
    return response

# List of symbols (you can replace this with your symbols from the CSV file)

# Loop through symbols and send POST requests
with open(r"C:\Users\aryan\OneDrive\Documents\Helian\HelianDemo\backend\scripts\constituents.csv", 'r') as file:

    reader = csv.DictReader(file)

    counter = 0
    for row in reader:

        if counter >= 50:
            break
        symbol = row['Symbol']
        esg_report_url = get_esg_report_url(symbol)
        if esg_report_url:
            response = send_post_request(symbol, esg_report_url)
            print(f"Symbol: {symbol}, Status Code: {response.status_code}")
        else:
            print(f"ESG report URL not found for symbol: {symbol}")



