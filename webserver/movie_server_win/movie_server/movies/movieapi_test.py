from .crawling import MegaBoxCrawl
from .crawling import CGVCrawl
from .crawling import LotteCinemaCrawl
from .getdistance import get_euclidean_distance
from .models import Movies
from .models import Theaters
from .models import MovieSchedules
from django.http import JsonResponse, HttpResponse
import json




def SearchMegaboxMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='megabox')
    for reqtheater in allTheater:
        MegaBoxCrawl(reqtheater)

    movieJson = {
        "megabox searching":"success"
    }
    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")



def SearchLottecinemaMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='lottecinema')
    movieJson = []
    for reqtheater in allTheater:
        movieList = LotteCinemaCrawl(reqtheater)
        movieJson.append(movieList)

    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")



def SearchCGVMovie(request):
    allTheater = Theaters.objects.filter(brand__exact='cgv')
    movieJson = []
    for reqtheater in allTheater:
        movieList = CGVCrawl(reqtheater)
        movieJson.append(movieList)

    movieJson = json.dumps(movieJson, ensure_ascii=False)
    return HttpResponse(movieJson, content_type="text/json-comment-filtered")



    
def Test(request):

    #GetMovieInfo("조커")
    return JsonResponse({
        'message':'안녕 파이썬 장고',
        'items' : ['python', 'django']
    })
