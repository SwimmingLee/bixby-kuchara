from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=167613'
url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=187787'
req = Request(url)
res = urlopen(req)
html = res.read()

bs = BeautifulSoup(html, 'html.parser')

title = bs.find('title')
print(title.text)

movieNames = bs.find('h3', {'class':'h_movie'}).a
print(movieNames.text)

infoSpec = bs.find('dl', {'class':'info_spec'})
outline = infoSpec.find('dt', {'class':'step1'}).next_sibling.next_sibling
genreRow = outline.find('span')
genres = genreRow.findAll('a')
for genre in genres:
    print(genre.text)
nationRow = genreRow.next_sibling.next_sibling
nation = nationRow.a
print(nation.text)
duration  = nationRow.next_sibling.next_sibling
print(duration.text)
rating = infoSpec.find('dt', {'class':'step4'}).next_sibling.next_sibling
movieRating = rating.a
print(movieRating.text)


