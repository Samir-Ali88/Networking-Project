"""
BeautifulSoup practice script.
Run with: python scrape.py
Requires: pip install beautifulsoup4 lxml --break-system-packages
"""
 
from bs4 import BeautifulSoup

# 1. Load the HTML (from a local file here; for real scraping you'd use
#    requests.get(url).text instead of open(...).read())
with open("web_scrapping/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 2. Create the soup object — this parses the HTML into a navigable tree
soup = BeautifulSoup(html, "lxml")  # or "html.parser" if lxml isn't installed

# 3. find() — grabs the FIRST matching element
title = soup.find("title")
print("Title:", title.text)

# 4. find_all() — grabs ALL matching elements, returns a list
courses = soup.find_all("div", class_="course")
print(f"\nFound {len(courses)} courses:\n")

for course in courses:
    name = course.find("h2", class_="course-name").text
    instructor = course.find("p", class_="instructor").text
    code = course["data-code"]  # reading an HTML attribute
    print(f"- [{code}] {name} | {instructor}")

# 5. select() — use CSS selectors instead (very handy)
links = soup.select("#links a")
print("\nLinks found via CSS selector:")
for link in links:
    print(f"- {link.text} -> {link['href']}")

# 6. Getting just text, no tags, from the whole page
# print(soup.get_text(separator=" ", strip=True))