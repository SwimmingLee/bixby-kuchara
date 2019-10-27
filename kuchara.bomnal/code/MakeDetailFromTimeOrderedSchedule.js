let console = require('console')
let dates = require('dates');

module.exports.function = function makeDetailFromTimeOrderedSchedule (timeSchedule, movie) {
  console.log(movie.movieName)
  // console.log(movie.duration)
  console.log(movie.movieRating)
  console.log(movie.director)
  console.log(movie.actors)
  console.log(movie.genre)
  console.log(movie.imgUrl)
  console.log(movie.userRating)
  console.log(movie.nation)

  console.log(theaterInfo.brand)
  console.log(theaterInfo.theaterName)
  console.log(theaterInfo.longitude)
  console.log(theaterInfo.latitude)
  console.log(theaterInfo.regionCode)
  console.log(theaterInfo.theaterCode)
  console.log(theaterInfo.iconUri)

  console.log(theaterSchedule.startTime)
  console.log(theaterSchedule.endTime)
  console.log(theaterSchedule.totalSeat)
  console.log(theaterSchedule.availableSeat)
  console.log(theaterSchedule.subtitle)
  console.log(theaterSchedule.dubbing)
  console.log(theaterSchedule.room)
  console.log(theaterSchedule.roomProperty)

  let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')

  let dateObj = {
    'dateTime': zonedDateTime.getDateTime(),
  }


  let movieScheduleDetail = {
    'movieName': movie.movieName,
    // "duration": movie.duration,
    "movieRating": movie.movieRating,
    "director": movie.director,
    "actors": movie.actors,
    "genre": movie.genre,
    "imgUrl": movie.imgUrl,
    "userRating": movie.userRating,
    'nation': movie.nation,

    'brand' : theaterInfo.brand,
    "theaterName": theaterInfo.theaterName,
    'longitude' : theaterInfo.longitude,
    'latitude' : theaterInfo.latitude,
    "theaterCode": theaterInfo.theaterCode,
    "regionCode": theaterInfo.regionCode,
    "distance": theaterInfo.distance,
    //'iconUri': theaterInfo.iconUri,

    'startTime': theaterSchedule.startTime,
    'endTime': theaterSchedule.endTime,
    "totalSeat": theaterSchedule.totalSeat,             // 총 좌석수
    "availableSeat": theaterSchedule.availableSeat,             // 빈 좌석수
    "subtitle": theaterSchedule.subtitle,               // 자막여부
    "dubbing": theaterSchedule.dubbing,
    "room": theaterSchedule.room,
    "roomProperty": theaterSchedule.roomProperty,

    "myDateExpression": dateObj.dateTime.date.year + "." + dateObj.dateTime.date.month + "." + dateObj.dateTime.date.day,
  }
  return movieScheduleDetail;
}
