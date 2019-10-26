console = require('console')

module.exports.function = function makeDetailFromTheaterOrderedSchedule (theaterOrderedSchedule, duration) {
  console.log(theaterOrderedSchedule.movie.movieName)
  let movieScheduleDetail = {
    'movieName': "조커",
    "duration": 130,
    "movieRating": "15세관람가",
    "director": '스티븐 스필버그',
    "actors": '히스레저, 조셉 고든 래빗',
    "genre": '액션, 드라마',
    "imgUrl":"https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167635_P27_100146.jpg",
    "userRating":0.0,
    'nation': 'korea',

    'brand' : "cgv",
    "theaterName": "영통",
    'longitude' : 123.123,
    'latitude' : 123.123,
    "theaterCode": 1533,
    "regionCode": 25,
    'iconUri':"/images/brand/theater/1x/cgv.png",

    'startTime': '18:00',
    'endTime': '19:50',
    "totalSeat": 234,             // 총 좌석수
    "availableSeat": 123,             // 빈 좌석수
    "subtitle": true,               // 자막여부
    "dubbing": true,
    "room": '7관',
    "roomProperty": "/images/roomProperty/padding_1px.png"
  }
  return movieScheduleDetail;
}




// let theater = {
//     "theaterName": theaterName,
//     "theaterCode": -1,
//     "regionCode": -1,
//     "brand": brand,
//     "theaterFlag": {
//       "namedPointStructure": {
//         'name': '',
//         'point':{
//           "latitude": -1,
//           "longitude": -1,
//         },
//       }, 
//     },
//   }