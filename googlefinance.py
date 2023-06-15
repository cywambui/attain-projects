from bs4 import BeautifulSoup
import requests

def getData(symbol):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    url= f'https://www.google.com/finance/quote'
    results = requests.get(url, headers=headers)

    soup = BeautifulSoup(results.text, 'html.parser')
    stock={
    'symbol' :symbol,   
    'price' : soup.find('div',{'class': 'YMlKec fxKbKc'}).text,
    'inflation' : soup.find('div',{'class':'JwB6zf'}).text,
    }
    return stock

print(getData('TSLA:NASDAQ'))
