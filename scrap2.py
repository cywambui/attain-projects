import requests
from bs4 import BeautifulSoup

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

print(title_text)
print(h1_text)
print(p_text)
print(span_text)
print(span_text)




