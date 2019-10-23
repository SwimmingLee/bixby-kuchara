// let timeOrderedSchedule = require('./sample/newStructure2.js');

module.exports.function = function restructureTheaterViewToTimeView (theaterOrderedSchedule) {

  let timeOrderedSchedule = {
    'movie':{
      "movieName": theaterOrderedSchedule.movie.movieName,
      "duration": theaterOrderedSchedule.movie.duration,
      "movieRating": theaterOrderedSchedule.movie.movieRating,
      "director": theaterOrderedSchedule.movie.director,
      "actors": theaterOrderedSchedule.movie.actors,
      "genre": theaterOrderedSchedule.movie.genre,
      "imgUrl": theaterOrderedSchedule.movie.imgUrl,
      "userRating": theaterOrderedSchedule.movie.userRating,
      "nation": theaterOrderedSchedule.movie.nation,
    },
    
    'timeSchedule': []
    }

  theaterOrderedSchedule.theater.forEach(function(theaterElement){
    let newBrand = theaterElement.theaterInfo.brand;
    let newTheaterName = theaterElement.theaterInfo.theaterName;
    let newLongitude = theaterElement.theaterInfo.longitude;
    let newLatitude = theaterElement.theaterInfo.latitude;
    let newTheaterCode = theaterElement.theaterInfo.theaterCode;
    let newRegionCode = theaterElement.theaterInfo.regionCode;
    let newIconUri = theaterElement.theaterInfo.iconUri;

    theaterElement.theaterSchedulePack.forEach(function(schedulePackElement){
      schedulePackElement.theaterSchedule.forEach(function(scheduleElement){
        timeOrderedSchedule.timeSchedule.push({
          'startTime': scheduleElement.startTime,
          'endTime': scheduleElement.endTime,
          'totalSeat': scheduleElement.totalSeat,
          'availableSeat': scheduleElement.availableSeat,
          "subtitle": scheduleElement.subtitle,               // 자막여부
          "dubbing": scheduleElement.dubbing,
          "room": scheduleElement.room,
          "roomProperty": scheduleElement.roomProperty,

          "theaterInfo": {
            "theaterName": newTheaterName,
            "theaterCode": newTheaterCode,
            "regionCode": newRegionCode,
            "brand": newBrand,
            'latitude':newLatitude,
            'longitude':newLongitude,
            'iconUri': newIconUri
          }
        })
      })
    })
  })

  return timeOrderedSchedule
}
