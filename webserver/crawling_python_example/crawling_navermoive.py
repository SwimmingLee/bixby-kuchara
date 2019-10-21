from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://movie.naver.com/movie/bi/mi/basic.nhn?code=167613')
res = urlopen(req)
html = res.read()

bs = BeautifulSoup(html, 'html.parser')

title = bs.find('title')
print(title.text)

movieNames = bs.findAll('h3', {'class':'h_movie'})
for movieName in movieNames:
    print(movieName.text)

