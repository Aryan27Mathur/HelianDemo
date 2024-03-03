import requests
import queue
import threading

q = queue.Queue()
valid_proxies=[]

with open("backend\scripts\proxies.txt", "r") as f:
    proxies = f.read().split('\n')
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while(not q.empty()):
        proxy = q.get()
        try: 
            url = f"https://finance.yahoo.com/quote/AAPL/sustainability"

            payload = {}
            headers = {
            'authority': 'finance.yahoo.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'tbla_id=9f802803-ba78-444d-bf70-cfcbf17b235d-tuctb5adc2f; GUC=AQEBCAFl4TBmEEIh6ASz&s=AQAAAFXgcIBb&g=Zd_klw; A1=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; A3=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; A1S=d=AQABBK1WYWQCEMN-cmnKfaC0ONTMz3lWQd0FEgEBCAEw4WUQZtxI0iMA_eMBAAcIrVZhZHlWQd0&S=AQAAAn-WSpzyNf4uM3yOXnL67T4; gpp=DBAA; gpp_sid=-1; axids=gam=y-YCMxlUZE2uIn60MfPvZEPrC8mjHynQJG~A&dv360=eS1hTzVNNVBwRTJ1Ri4wNFYxN3ZYa3JueVFFOTBBQll6MX5B&ydsp=y-t6ncRHJE2uKTUDBHCi15_NnyXt1OSXM4~A&tbla=y-ItM0A4lE2uLqwErmpLm9Bq1JD7tCgS2m~A; PRF=t%3DABBV%252BVOO%252BAAPL%252BTSLA; __gpi=UID=00000dce2ae28563:T=1709238035:RT=1709238035:S=ALNI_MbZDQersrGcJUREkMK-c8WJfPlWqw; __eoi=ID=349b00eb6adaa151:T=1709238035:RT=1709238035:S=AA-AfjaAPIkzIW8hIRagyJkUS4SZ; cmp=t=1709242037&j=0&u=1YNN',
            'referer': f'https://finance.yahoo.com/quote/AAPL',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
            }

            response = requests.request("GET", url, headers=headers, data=payload, proxies={"http":proxy,"https":proxy})
        except:
            #print(f"{proxy} broke")
            continue
        if(response.status_code == 200):
            print(proxy)

for _ in range(20):
    threading.Thread(target=check_proxies).start()