
import requests
from bs4 import BeautifulSoup
import re

context_text = """
Environment, Social and Governance (ESG) Risk RatingsTotal ESG Risk score1718th percentileLowLowEnvironment Risk Score0.5Social Risk Score7.4Governance Risk Score9.4Controversy LevelAAPLPeersCategory Average3Significant Controversy level4NoneSevereESG data provided by Sustainalytics, Inc.Last updated on 9/2023
"""

# Define regular expressions for matching the scores
total_score_regex = re.compile(r'Total ESG Risk score(\d+)')
environment_score_regex = re.compile(r'Environment Risk Score([\d.]+)')
social_score_regex = re.compile(r'Social Risk Score([\d.]+)')
governance_score_regex = re.compile(r'Governance Risk Score([\d.]+)')

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
    'cookie': 'A3=d=AQABBAwr3WUCENYm5ILfiYjgnxwY8AjZQggFEgEBAQF83mXnZdxI0iMA_eMAAA&S=AQAAArxAggYstqThsbzX9jPkJPI; A1=d=AQABBAwr3WUCENYm5ILfiYjgnxwY8AjZQggFEgEBAQF83mXnZdxI0iMA_eMAAA&S=AQAAArxAggYstqThsbzX9jPkJPI; A1S=d=AQABBAwr3WUCENYm5ILfiYjgnxwY8AjZQggFEgEBAQF83mXnZdxI0iMA_eMAAA&S=AQAAArxAggYstqThsbzX9jPkJPI; cmp=t=1709502620&j=0&u=1YNN; gpp=DBAA; gpp_sid=-1; PRF=t%3DAAPL; axids=gam=y-xNBECB9E2uKjE.K5u4vMrE6HDEVz5PDO~A&dv360=eS1qdTh6RmoxRTJ1RVhyeFB5MTd6dmRzYWo0cllxRm15X35B&ydsp=y-8Sr_9gNE2uInJ.MyZ_6JtTIFio7NMfDb~A&tbla=y-VXewiTtE2uLPPydBjWNq8OomtMUPUpGL~A; tbla_id=5b8e9d3c-2934-496e-8ca4-1b72ff00a424-tuctcd6ad0e; __gpi=UID=00000dcefd458825:T=1709502620:RT=1709502620:S=ALNI_MaSytEN8awtB4FcNIdGpq5WLePJ4g; __eoi=ID=b824e1dc14fb5abd:T=1709502620:RT=1709502620:S=AA-AfjYIwFXXmNJsVaKbK8h-TSM2',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.text, 'html.parser')

        # Find the section with class="svelte-1dspbuk"
    try:
        maindiv = soup.find("div", {"id": "Main"})
        esgdata = maindiv.get_text("|").split("|")
        
        t_score = float(esgdata[esgdata.index('Total ESG Risk score') + 1])
        e_score = float(esgdata[esgdata.index('Environment Risk Score') + 1])
        s_score = float(esgdata[esgdata.index('Social Risk Score') + 1])
        g_score = float(esgdata[esgdata.index('Governance Risk Score') + 1])
        send_post_request(s, t_score, e_score, s_score, g_score)
        print(s)
    except:
        badSymbols.append(s)
        print(f"{s} not working")
        send_post_request(s, -1, -1, -1, -1)
        continue
 
    if(i%10==0):
        print(f"company {i} updated")

print(badSymbols)



