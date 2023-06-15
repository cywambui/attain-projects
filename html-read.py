from bs4 import BeautifulSoup

with open("index.html","r") as f:
    text=BeautifulSoup(f,"html.parser")

#a specific tag
tag = text.span

#reads the specific string in the tag
print(tag.string)

