from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import requests
import time
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()


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

driver.get("https://finance.yahoo.com/quote/WAB/sustainability")
esg_cards = driver.find_element(By.CLASS_NAME, "svelte-1dspbuk")
data = esg_cards.text.split("\n")

t_score = float(data[2])
e_score = float(data[6])
s_score = float(data[8])
g_score = float(data[10])


driver.quit()

send_post_request('WAB', t_score, e_score, s_score, g_score)

# text_box = driver.find_element(by=By.CSS_SELECTOR, value='[data-testid="TOTAL_ESG_SCORE"]')

# print(text_box.text)
