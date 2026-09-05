import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# ⬇️ Yahan apni marzi se koi bhi website ka link daalo
URL = "http://books.toscrape.com/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
# Website ka HTML mangwao
response = requests.get(URL, headers=headers)
# Check karo request kamyaab hui ya nahi
print("Status Code:", response.status_code)
# ager kamyab hote tu hain 202 ay ga weran 404 ka wrtie aye ga means no acces 
soap = BeautifulSoup(response.text, 'lxml')
# print(soap.prettify())
#.prettify()html ky har tag ko nayi line aur proper indentation ke saath dikhata hai (jaise VS Code mein code formatted hota hai)
# suppse <html>
#  <head>
#   <title>
#    Test
#   </title>
#  </head>
#  <body>
#   <p>
#    Hello
#   </p>
#  </body>
# </html>
# print("Length of response:", len(response.text))
# print(response.text[:500])
# html_h1 = soap.find_all('p')
# html my dehkhna kitny paragraph hain 
# print(html_h1)
# print(len(html_h1))

# html_class_target = soap.find_all('p', class_='price_color')
# print(html_class_target)

# kise be class ko targer kerny ky liya asy kerty ..kise be website per inspect kerrna or check kerna class name kya dya woh class name idehr paset kerna 
for i in soap.find_all('h3'):
    print(i).text
    # .strip() yeah i.text.strip() leg stka iske lagany ke wjha jeb be html bnta tu space chori jate \n kerky to woh remove kerny ky liya yeah suse hota taky tate line wise aye space agy pichy na ho