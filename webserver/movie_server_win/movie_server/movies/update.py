import csv
import json
import re
from .models import Theaters
from .models import Movies
from django.http import JsonResponse
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
from datetime import datetime


def GetNaverMovieInfo(url):
    movieInfoPart = dict()
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read()

    bs = BeautifulSoup(html, 'html.parser')

    # Get movie name
    #movieNames = bs.find('h3', {'class':'h_movie'}).a
    #print(movieNames.text)

    infoSpec = bs.find('dl', {'class':'info_spec'})
    outline = infoSpec.find('dt', {'class':'step1'}).next_sibling.next_sibling
    genreRow = outline.find('span')
    genres = genreRow.findAll('a')
    genreStr = ""
    for genre in genres:
        genreStr += genre.text
    movieInfoPart["genre"] = genreStr

    nationRow = genreRow.next_sibling.next_sibling
    nation = nationRow.a
    nationStr = nation.text
    movieInfoPart["nation"] = nationStr

    duration  = nationRow.next_sibling.next_sibling
    durationStr = re.findall("\d+", duration.text)[0]
    movieInfoPart["duration"] = durationStr

    rating = infoSpec.find('dt', {'class':'step4'}).next_sibling.next_sibling
    movieRating = rating.a
    movieRatingStr = movieRating.text
    movieInfoPart["movieRating"] = movieRatingStr

    return movieInfoPart


def GetMovieInfo(movieName):
    client_id = "Ob9m_EHdGWkXlNLSWPjo"
    client_key = "tA5WWOMJHo"
    url = "https://openapi.naver.com/v1/search/movie.json"
    option = "&display=1&sort=count"
    query = "?query="+urllib.parse.quote(movieName)
    url_query = url + query + option
    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_key)
    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        response_body = response.read()
        movieInfo = response_body.decode('utf-8')
        # print(movieInfo)
        movieInfo = json.loads(movieInfo)
        link = movieInfo["items"][0]["link"]
        imgUrl = movieInfo["items"][0]["image"]
        actor = movieInfo["items"][0]["actor"]
        director = movieInfo["items"][0]["director"]
        userRating = movieInfo["items"][0]["userRating"]
        movieInfoPart2 = GetNaverMovieInfo(link)


        MoviesEle = Movies(movieName=movieName, director=director, \
                        actor=actor, movieRating=movieInfoPart2["movieRating"], \
                        duration=movieInfoPart2["duration"], genre=movieInfoPart2["genre"], \
                        userRating=userRating, imgUrl=imgUrl, nation=movieInfoPart2["nation"])
        MoviesEle.save()
        return MoviesEle
    else:
        print("Error code:"+rescode)

        



def UpdateMoive(request):
    print()

def UpdateTheater(request):
    #csvFileDir = r"C:\Users\student\works\bixby-kuchara\webserver\movie_server_win\movie_server\movies\theater_info.txt"
    csvFileDir = r"C:\Users\Lee\workspace\bixby-kuchara\webserver\movie_server_win\movie_server\movies\theater_info.txt"
    csvFile = open(csvFileDir, 'r', encoding='UTF-8')
    try:
        spamreader = csv.reader(csvFile)
        for row in spamreader:
            theaterName = row[0]
            theaterCode = row[1]
            regionCode = row[2]
            brand = row[3]
            latitude = row[4]
            longitude = row[5]
            oldTime = "20191010"
            convert_date = datetime.strptime(oldTime, "%Y%m%d").date()
            theaterEle = Theaters(theaterName=theaterName, regionCode=regionCode, theaterCode=theaterCode, \
                                longitude=longitude, latitude=latitude, brand=brand, updatedTime=convert_date)
            theaterEle.save()
 
    finally:
        csvFile.close()

    return JsonResponse({
        'message':'정상적으로 업데이트 되었습니다.',
        'items' : ['메가박스', 'CGV', '롯데시네마']
    })