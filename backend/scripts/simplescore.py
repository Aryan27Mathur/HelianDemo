import requests
from bs4 import BeautifulSoup
import re

total_score_pattern = r"Total ESG Risk Score\s+(\d+\.\d+)"
environmental_score_pattern = r"Environmental Risk Score\s+(\d+\.\d+)"
social_score_pattern = r"Social Risk Score\s+(\d+\.\d+)"
governance_score_pattern = r"Governance Risk Score\s+(\d+\.\d+)"

def send_post_request(symbol, t_score, e_score, s_score, g_score):
    url = 'http://localhost:8000/update_esg_score/'
    data = {
        'symbol': symbol,
        'total_score': t_score,
        'e_score':e_score,
        's_score':s_score,
        'g_score':g_score,
        'etf' :'no'
    }
    response = requests.post(url, json=data)
    return response

symbols = requests.get('http://localhost:8000/get_all_company_symbols/').text.split(",")
badSymbols = []
for i, s in enumerate(symbols):

    url = f"https://finance.yahoo.com/quote/{s}/sustainability"

    payload = {}
    headers = {
    'authority': 'finance.yahoo.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'tbla_id=9f802803-ba78-444d-bf70-cfcbf17b235d-tuctb5adc2f; GUC=AQEBCAFl4TBmEEIh6ASz&s=AQAAAFXgcIBb&g=Zd_klw; A1=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; A3=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; A1S=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; gpp=DBAA; gpp_sid=-1; axids=gam=y-YCMxlUZE2uIn60MfPvZEPrC8mjHynQJG~A&dv360=eS1hTzVNNVBwRTJ1Ri4wNFYxN3ZYa3JueVFFOTBBQll6MX5B&ydsp=y-t6ncRHJE2uKTUDBHCi15_NnyXt1OSXM4~A&tbla=y-ItM0A4lE2uLqwErmpLm9Bq1JD7tCgS2m~A; PRF=t%3DABBV%252BVOO%252BAAPL%252BTSLA; __gpi=UID=00000dce2ae28563:T=1709238035:RT=1709238035:S=ALNI_MbZDQersrGcJUREkMK-c8WJfPlWqw; __eoi=ID=349b00eb6adaa151:T=1709238035:RT=1709238035:S=AA-AfjaAPIkzIW8hIRagyJkUS4SZ; cmp=t=1709242037&j=0&u=1YNN',
    'referer': f'https://finance.yahoo.com/quote/{s}',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload, proxies={"http":"27.79.140.50:4004","https":"27.79.140.50:4004"})

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the section with class="svelte-1dspbuk"
    section = soup.find('section', class_='svelte-1dspbuk')

    if section:
        # Access the content of the section
        content = section.get_text()
        #print(content)
    else:
        badSymbols.append(s)
        print(f"{s} not working")
        continue


    # Extract numerical values using regular expressions
    t_score_match = re.search(total_score_pattern, content)
    e_score_match = re.search(environmental_score_pattern, content)
    s_score_match = re.search(social_score_pattern, content)
    g_score_match = re.search(governance_score_pattern, content)

    # Assign the matched numerical values to variables
    if t_score_match:
        t_score = float(t_score_match.group(1))
    else:
        t_score = None

    if e_score_match:
        e_score = float(e_score_match.group(1))
    else:
        e_score = None

    if s_score_match:
        s_score = float(s_score_match.group(1))
    else:
        s_score = None

    if g_score_match:
        g_score = float(g_score_match.group(1))
    else:
        g_score = None

    send_post_request(s, t_score, e_score, s_score, g_score)

    if(i%10==0):
        print(f"company {i} updated")

print(badSymbols)
