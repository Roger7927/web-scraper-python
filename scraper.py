import requests
from bs4 import BeautifulSoup

# URL da página que queremos raspar
url = 'http://books.toscrape.com/'

# Faz a requisição HTTP para a URL
response = requests.get(url)

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontra a tag h3 que contém o título do livro
livro = soup.find('h3')

# Encontra a tag a que contém o título do livro
titulo = livro.find('a').get('title')

# Imprime o título do livro no terminal
print(f'O título do primeiro livro é: {titulo}')