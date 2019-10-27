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

  console.log(timeSchedule.theaterInfo.brand)
  console.log(timeSchedule.theaterInfo.theaterName)
  console.log(timeSchedule.theaterInfo.longitude)
  console.log(timeSchedule.theaterInfo.latitude)
  console.log(timeSchedule.theaterInfo.regionCode)
  console.log(timeSchedule.theaterInfo.theaterCode)
  // console.log(timeSchedule.theaterInfo.iconUri)

  console.log(timeSchedule.startTime)
  console.log(timeSchedule.endTime)
  console.log(timeSchedule.totalSeat)
  console.log(timeSchedule.availableSeat)
  console.log(timeSchedule.subtitle)
  console.log(timeSchedule.dubbing)
  console.log(timeSchedule.room)
  console.log(timeSchedule.roomProperty)

  let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')
  let dateObj = { 'dateTime': zonedDateTime.getDateTime(), }

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

    'brand' : timeSchedule.theaterInfo.brand,
    "theaterName": timeSchedule.theaterInfo.theaterName,
    'longitude' : timeSchedule.theaterInfo.longitude,
    'latitude' : timeSchedule.theaterInfo.latitude,
    "theaterCode": timeSchedule.theaterInfo.theaterCode,
    "regionCode": timeSchedule.theaterInfo.regionCode,
    "distance": timeSchedule.theaterInfo.distance,
    "address": timeSchedule.theaterInfo.address,
    //'iconUri': timeSchedule.theaterInfo.iconUri,

    'startTime': timeSchedule.startTime,
    'endTime': timeSchedule.endTime,
    "totalSeat": timeSchedule.totalSeat,             // 총 좌석수
    "availableSeat": timeSchedule.availableSeat,     // 빈 좌석수
    "subtitle": timeSchedule.subtitle,               // 자막여부
    "dubbing": timeSchedule.dubbing,
    "room": timeSchedule.room,
    "roomProperty": timeSchedule.roomProperty,
    "roomPropertyUriList": timeSchedule.roomPropertyUriList,
    

    "myDateExpression": dateObj.dateTime.date.year + "." + dateObj.dateTime.date.month + "." + dateObj.dateTime.date.day,
  }
  return movieScheduleDetail;
}
