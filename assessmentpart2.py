# Import the necessary libraries import re
import csv
#import map
import os
import smtplib, ssl
import email
import sys
#From email.message import email message link = input(" enter a valid Wiki link: ")
if not re.match('https:ertdjtfywiki', wiki_link):
print("invalid link")
No = int(input("enter a valid integer between 1-20 ")) if No not in range(1,21):
print("invalid")
def scraping(url, No):
arry_links = []
Response = requests.get(url).text
links = re.findall('href="(/wiki/.*?)"', Response) for link in links:
arry_links.append('https://en.wikipedia.org' + link) if n == 0:
return Response else:
for link in links:
arry_links += scraping('https://en.wikipedia.org' + link, n-1)
return arry_links
arry_links = scraping(wiki_link, n)
count = len(arry_links) Lent = len(set(arry_links))
with open('test.csv', 'w') as file: writer = csv.writer(file) writer.writerow(["Links"]) for link in arry_links:
writer.writerow([link]) writer.writerow(["Totalcount:", count]) writer.writerow(["uni",lent])
