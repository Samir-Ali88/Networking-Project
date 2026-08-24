from bs4 import BeautifulSoup

with open("web_scrapping/hw.html","r") as f:
    html=f.read()

soup = BeautifulSoup(html,"lxml")

title = soup.find("h1")    
print("h1 is: ", title.text)

footer = soup.find("footer", id="footer")
footer_links = footer.find_all("a")
print("footer is: ", footer.text.strip())

books = soup.find_all("div", class_="book-container")
print("total books are: ", len(books))

for b in books:
    name = b.find("h2", class_="title")
    i = b.get("data-id")
    print(f"the name of book: {name.text}! the id of book {i}")
    
    tag = b.find("ul", class_="tags")
    lists = tag.find_all("li")
    
   
    tags = [li.text for li in lists] 
    
    
    print(f"{name.text} tags: {tags}") 

for link in footer_links:
    print(f"{link.text} and {link.get('href')}")