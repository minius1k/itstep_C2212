import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

response = requests.get(url)
response.encoding = 'utf-8'

if response.status_code == 200:
  soup = BeautifulSoup(response.text, 'html.parser')
  books = soup.find_all('article', class_='product_pod')

  for i, book in enumerate(books, 1):
    title = book.find('h3').find('a')['title']
    price = book.find('p', class_='price_color').text
    print(f'{i}. Назва: {title} | Ціна: {price}')
else:
  print('Помилка:', response.status_code)