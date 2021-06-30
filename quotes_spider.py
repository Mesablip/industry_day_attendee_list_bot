from scrapy import Selector
import time
from selenium import webdriver
from urllib.request import urlopen, Request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#Test
agency = input("Please enter the agency you are searching for (ex: DOD MDA): ")
agency = ["\"" + x + "\"" for x in agency.split(" ")]
attendee_list_names = ' "Industry Day*" ("attendee* list" OR "contractor* list" OR "interested parties" OR "registration list" OR "participant* list" OR "interested companies" OR "bidder* list" OR "procurement list")'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
driver = webdriver.Chrome(executable_path="C:\\Users\\Dylan Newman\\Documents\\chromedriver.exe")
url = "https://www.google.com/search?q=" + " ".join(agency) + attendee_list_names + " filetype:pdf"
driver.get(url)
time.sleep(3)
sel = Selector(text=driver.page_source)
x = sel.xpath("//div[@class='yuRUbf']/a/@href").extract()
y = 1
for link in x:
    req = Request(url=link, headers=headers)
    html = urlopen(req).read()
    with open("C:\\Users\\Dylan Newman\\Documents\\Files\\file" + str(y) + ".pdf", "wb") as file:
        file.write(html)
    y += 1
print("hey")
