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
