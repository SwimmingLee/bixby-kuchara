import urllib.request

client_id = "Ob9m_EHdGWkXlNLSWPjo"
client_key = "2b38350590ac6619079672fb9ec1b029"

url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
option = ""
query = "?key={}&movieNm={}".format(client_key, urllib.parse.quote(input("질의:")))
url_query = url + query + option
#Open API 검색 요청 개체 설정
request = urllib.request.Request(url_query)

#request.add_header("X-Naver-Client-Id",client_id)
#request.add_header("X-Naver-Client-Secret",client_secret)
#검색 요청 및 처리
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode == 200):
   response_body = response.read()
   print(response_body.decode('utf-8'))
else:
   print("Error code:"+rescode)
#제목: 네이버 검색 API 활용하기
