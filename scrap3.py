import requests
from bs4 import BeautifulSoup
import sqlite3

respond = requests.get("https://www.google.com/finance/quote/VIX:INDEXCBOE")
html_content= respond.text

soup= BeautifulSoup(html_content, "html.parser")

title= soup.title.text 



conn= sqlite3.connect('example.db')
cursor= conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS web_data(
    id INTERGER PRIMARY KEY,
    title TEXT
    )
    ''')
cursor.execute('INSERT INTO web_data(title )VALUES (?)', (title,))
conn.commit()
conn.close()