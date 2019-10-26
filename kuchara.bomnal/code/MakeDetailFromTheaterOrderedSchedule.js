console = require('console')

module.exports.function = function makeDetailFromTheaterOrderedSchedule (movie, theaterInfo, theaterSchedule) {
  console.log(movie.movieName)
  console.log(movie.duration)
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

  let movieScheduleDetail = {
    'movieName': movie.movieName,
    "duration": movie.duration,
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
    'iconUri': theaterInfo.iconUri,

    'startTime': theaterSchedule.startTime,
    'endTime': theaterSchedule.endTime,
    "totalSeat": theaterSchedule.totalSeat,             // 총 좌석수
    "availableSeat": theaterSchedule.availableSeat,             // 빈 좌석수
    "subtitle": theaterSchedule.subtitle,               // 자막여부
    "dubbing": theaterSchedule.dubbing,
    "room": theaterSchedule.room,
    "roomProperty": theaterSchedule.roomProperty
  }
  return movieScheduleDetail;
}

// let movieScheduleDetail = {
//     'movieName': movie.movieName,
//     "duration": movie.duration,
//     "movieRating": movie.movieRating,
//     "director": movie.director,
//     "actors": movie.actors,
//     "genre": '액션, 드라마',
//     "imgUrl":"https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167635_P27_100146.jpg",
//     "userRating":0.0,
//     'nation': 'korea',

//     'brand' : "cgv",
//     "theaterName": "영통",
//     'longitude' : 123.123,
//     'latitude' : 123.123,
//     "theaterCode": 1533,
//     "regionCode": 25,
//     'iconUri':"/images/brand/theater/1x/cgv.png",

//     'startTime': '18:00',
//     'endTime': '19:50',
//     "totalSeat": 234,             // 총 좌석수
//     "availableSeat": 123,             // 빈 좌석수
//     "subtitle": true,               // 자막여부
//     "dubbing": true,
//     "room": '7관',
//     "roomProperty": "/images/roomProperty/padding_1px.png"
//   }