import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# {{{{{{{{{{{{{{{{{{yeah one page ko data fetch kya hian }}}}}}}}}}}}}}}}}}

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
products = soap.find_all('article', class_='product_pod')
data = []
for i in products:
     title = i.find('h3').text
    #  print(title)
     price = i.find('p',class_='price_color').text
    #  print(price)
     rating = i.find('p',class_='instock availability').text.strip()
    #  print(rating)
     data.append({'Title': title, 'Price': price,  'rating': rating})

df=pd.DataFrame(data)
print(df)
    # .strip() yeah i.text.strip() leg stka iske lagany ke wjha jeb be html bnta tu space chori jate \n kerky to woh remove kerny ky liya yeah suse hota taky tate line wise aye space agy pichy na ho



# {{{{{{{{{{{{{{{{{{yeah one to 50 teq data fetch kya page ka web }}}}}}}}}}}}}}}}}}

# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
# }

# data = []   # sab pages ka data isi list mein jama hoga

# for page in range(1, 51):   # page 1 se 50 tak
#     URL = f"http://books.toscrape.com/catalogue/page-{page}.html"
    
#     response = requests.get(URL, headers=headers)
#     print(f"Page {page} -> Status Code: {response.status_code}")
    
#     if response.status_code != 200:
#         break   # agar page exist na kare to loop rok do
    
#     soap = BeautifulSoup(response.text, 'lxml')
#     products = soap.find_all('article', class_='product_pod')
    
#     for i in products:
#         title = i.find('h3').find('a').get('title')
#         price = i.find('p', class_='price_color').text
#         rating = i.find('p', class_='instock availability').text.strip()
        
#         data.append({'Title': title, 'Price': price, 'Rating': rating})

# # Sab pages ka data ek DataFrame mein
# df = pd.DataFrame(data)
# print(df.shape)   # kitni total rows (books) mile
# print(df)