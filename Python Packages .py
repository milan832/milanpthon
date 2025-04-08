import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "TvEQDs0S8GmSm3eGgxHIuxzWs3QJIePovI9RQHpaAABj7"

headers = {
    "Authorization": "Bearer " + api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
print(response.text)

#web scrping
import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())


#Browser Automation 
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

#working with pdf 
from pypdf import PdfReader, PdfWriter

reader = PdfReader("1234.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)
writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)
