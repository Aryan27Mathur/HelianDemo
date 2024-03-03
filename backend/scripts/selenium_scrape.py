from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import requests
import time
chromedriver_autoinstaller.install()

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


driver = webdriver.Chrome()
symbols = requests.get('http://localhost:8000/get_all_company_symbols/').text.split(",")

for s in symbols:

    driver.get(f"https://finance.yahoo.com/quote/{s}/sustainability")
    time.sleep(2)
    esg_cards = driver.find_element(By.CLASS_NAME, "svelte-1dspbuk")
    data = esg_cards.text.split("\n")p

    t_score = float(data[2])
    e_score = float(data[6])
    s_score = float(data[8])
    g_score = float(data[10])
    send_post_request(s, t_score, e_score, s_score, g_score)
    print(f"{s} updated")

driver.quit()

# text_box = driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="TOTAL_ESG_SCORE"]')

# print(text_box.text)
