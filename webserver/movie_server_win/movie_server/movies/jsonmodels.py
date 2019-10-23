import json



def GetTheaterInfo(theaterInfo):
    theaterInfoDict = dict()
    theaterInfoDict['theaterName'] = theaterInfo.theaterName
    theaterInfoDict['theaterCode'] = theaterInfo.theaterCode
    theaterInfoDict['regionCode'] = theaterInfo.regionCode
    theaterInfoDict['longitude'] = theaterInfo.longitude
    theaterInfoDict['latitude'] = theaterInfo.latitude
    theaterInfoDict['brand'] = theaterInfo.brand
    return theaterInfoDict

def GetMovie(movie):
    movieDict = dict()
    movieDict['movieName'] = movie.movieName
    movieDict['movieRating'] = movie.movieRating
    movieDict['userRating'] = movie.userRating
    movieDict['duration'] = movie.movieRating
    movieDict['director'] = movie.movieRating
    movieDict['actor'] = movie.actor
    movieDict['genre'] = movie.genre
    movieDict['imgUrl'] = movie.imgUrl
    movieDict['nation'] = movie.nation
    return movieDict

class TheaterOrderedSchedule:
    def __init__(self, movie, theater):
        self.movie = movie
        self.theater = theater
    
    def movieUpdate(self, movie):
        self.movie = movie

    def theaterUpdate(self, theater):
        self.theater = theater


    def GetJson(self):
        movieDict = GetMovie(self.movie)
        
        theaterList = []
        for theater in self.theater:
            theaterInfo = theater['theaterInfo']
            theaterEle = {
                'theaterInfo':GetTheaterInfo(theaterInfo),
                'theaterSchedule':theater['theaterSchedule']
            }
            theaterList.append(theaterEle)
        
        TOSJson = {
            'movie':movieDict,
            'theater':theaterList
        }

        return TOSJson
        

    
