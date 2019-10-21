import csv
import json
from .models import Theaters
from django.http import JsonResponse

def UpdateTheater(request):
    csvFileDir = r"C:\Users\student\works\bixby-kuchara\webserver\movie_server_win\movie_server\movies\theater_info.txt"
    # csvFileDir = r"C:\Users\Lee\workspace\bixby-kuchara\webserver\apitest\theater_info.txt"
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
            theaterEle = Theaters(theaterName=theaterName, regionCode=regionCode, theaterCode=theaterCode, longitude=longitude, latitude=latitude, brand=brand)
            theaterEle.save()
 #           
 # print("theatherName:{}, theaterCode:{}, regionCode:{}, brand:{}, latitude:{}, longitude:{}".format(row[0], row[1], row[2], row[3], row[4], row[5]))
    finally:
        csvFile.close()

    return JsonResponse({
        'message':'정상적으로 업데이트 되었습니다.',
        'items' : ['메가박스', 'CGV', '롯데시네마']
    })