from bs4 import BeautifulSoup # Extração de dados HTML e XML
import requests # Enviar solicitações HTTP

# Objeto site recebendo o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content

# Objeto soup baixando do site o html
# Transforma html em string e o print vai exibir o html
soup = BeautifulSoup(site, "html.parser")
#print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

#print(temperatura.string)

print(soup.title)
print(soup.title.string)

print(soup.find('admin'))