import requests
from bs4 import BeautifulSoup
import sqlite3

html_doc="""
<html>
<head>
<title>my first request</title>
</head>
<body>
<h1>hello world</>
<p>hello world i just started coding welcome to my world of coding</p>
<span>i literally need money right now like lots of them</span>
</body>
</html>
"""

soup=BeautifulSoup(html_doc,"html.parser")

# accessing elements
title=soup.title
h1=soup.h1
p=soup.p
span=soup.span

# extracting elements
title_text=title.text
h1_text=h1.text
p_text=p.text
span_text=span.text



conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS website_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        p TEXT,
        name TEXT 
    )
''')

# Insert the extracted data into the database
cursor.execute('INSERT INTO website_data (title, p) VALUES (?, ?)', (title, p))
# Commit the changes and close the connection
conn.commit()

conn.close()

