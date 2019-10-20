import urllib.request
client_id = "Ob9m_EHdGWkXlNLSWPjo"
client_secret = "tA5WWOMJHo"
url = "https://openapi.naver.com/v1/search/movie.json"
option = "&display=3&sort=count"
query = "?query="+urllib.parse.quote(input("질의:"))
url_query = url + query + option
#Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
   response_body = response.read()
   print(response_body.decode('utf-8'))
else:
   print("Error code:"+rescode)
#제목: 네이버 검색 API 활용하기
#import
import urllib.request
#애플리케이션 클라이언트 id 및 secret
client_id = "[자신의 client id]"
client_secret = "[자신의 client secret]"
#도서검색 url
#디폴트(json) https://openapi.naver.com/v1/search/book?query=python&display=3&sort=count
#json 방식 https://openapi.naver.com/v1/search/book.json?query=python&display=3&sort=count
#xml 방식  https://openapi.naver.com/v1/search/book.xml?query=python&display=3&sort=count
url = "https://openapi.naver.com/v1/search/book.json"
option = "&display=3&sort=count"
query = "?query="+urllib.parse.quote(input("질의:"))
url_query = url + query + option
#Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
   response_body = response.read()
   print(response_body.decode('utf-8'))
else:
   print("Error code:"+rescode)
