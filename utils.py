import random
import requests
from openai import OpenAI
from bs4 import BeautifulSoup

def random_number():
    return str(sorted(random.sample(range(1, 46), 6)))


def kospi():
    KOSPI_URL = 'https://finance.naver.com/sise/'

    res = requests.get(KOSPI_URL)

    res_text = res.text

    selector = '#KOSPI_now'
    
    soup = BeautifulSoup(res_text, 'html.parser')
    kospi = soup.select_one(selector).text

    return kospi


def openai(api_key, user_input):
    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role': 'system', 'content': '너는 지장보살이야'},
            {'role': 'user', 'content': user_input},
        ]
    )

    return completion.choices[0].message.content



