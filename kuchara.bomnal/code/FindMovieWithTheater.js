let console = require('console');
var config = require('config')

module.exports.function = function findMovieWithTheater (locationalKeyword, brand) {
  if(locationalKeyword){
    console.log("no locational keyword")
  } else {
    console.log(locationalKeyword)
  }

  let response = [
    {
      "movie": {
        "movieName": "조커",
        "duration": 130,
        "movieRating": "15세관람가",
        "director": '스티븐 스필버그',
        "actors": ['히스레저', '조셉 고든 래빗'],
        "genre": ['액션', '드라마'],
      },
      // startTime: dates.ZonedDateTime.now(),
      // endTime: dates.ZonedDateTime.now(),
      "totalSeat": 234,             // 총 좌석수
      "availableSeat": 123,             // 빈 좌석수
      "theater": {
        "theaterName": "영통 메가박스",
        "theaterCode": 1533,
        "regionCode": 25,
        // "pos": {
        //   "xpos": 27.483674,
        //   "ypos": 57.123734,
        // },
        "brand": "megabox",
        "theaterFlag": {
          "locationalKeyword": ['영통', '수원', '경희대']
        },
      },
      "movieScheduleFlag": {
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "digitalized": true,            // 디지털 / 필름
        "lateNight": false,              // 심야 여부
        "morning": false,   
      },
      "room": "1관",                 // 상영관
      "movieCode": 123123,  
    },
    {
      "movie": {
        "movieName": "인셉션",
        "duration": 140,
        "movieRating": "15세관람가",
        "director": '토드 스필버그',
        "actors": ['조셉 고든 래빗', '호아킨 피닉스'],
        "genre": ['액션', '드라마'],
      },
      // startTime: dates.ZonedDateTime.now(),
      // endTime: dates.ZonedDateTime.now(),
      "totalSeat": 234,             // 총 좌석수
      "availableSeat": 123,             // 빈 좌석수
      "theater": {
        "theaterName": "왕십리 CGV",
        "theaterCode": 1533,
        "regionCode": 25,
        // "pos": {
        //   "xpos": 27.483674,
        //   "ypos": 57.123734,
        // },
        "brand": "cgv",
        "theaterFlag": {
          "locationalKeyword": ['왕십리', '한양대', '성동구']
        },
      },
      "movieScheduleFlag": {
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "digitalized": true,            // 디지털 / 필름
        "lateNight": false,              // 심야 여부
        "morning": false,   
      },
      "room": "7관",                 // 상영관
      "movieCode": 234234,  
    },
    {
      "movie": {
        "movieName": "해리포터",
        "duration": 140,
        "movieRating": "15세관람가",
        "director": '토드 스필버그',
        "actors": ['조셉 고든 래빗', '호아킨 피닉스'],
        "genre": ['액션', '드라마'],
      },
      // startTime: dates.ZonedDateTime.now(),
      // endTime: dates.ZonedDateTime.now(),
      "totalSeat": 234,             // 총 좌석수
      "availableSeat": 123,             // 빈 좌석수
      "theater": {
        "theaterName": "왕십리 CGV",
        "theaterCode": 1533,
        "regionCode": 25,
        // "pos": {
        //   "xpos": 27.483674,
        //   "ypos": 57.123734,
        // },
        "brand": "cgv",
        "theaterFlag": {
          "locationalKeyword": ['왕십리', '한양대', '성동구']
        },
      },
      "movieScheduleFlag": {
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "digitalized": true,            // 디지털 / 필름
        "lateNight": false,              // 심야 여부
        "morning": false,   
      },
      "room": "7관",                 // 상영관
      "movieCode": 234234,  
    },
    {
      "movie": {
        "movieName": "반지의제왕",
        "duration": 140,
        "movieRating": "15세관람가",
        "director": '토드 스필버그',
        "actors": ['조셉 고든 래빗', '호아킨 피닉스'],
        "genre": ['액션', '드라마'],
      },
      // startTime: dates.ZonedDateTime.now(),
      // endTime: dates.ZonedDateTime.now(),
      "totalSeat": 234,             // 총 좌석수
      "availableSeat": 123,             // 빈 좌석수
      "theater": {
        "theaterName": "왕십리 CGV",
        "theaterCode": 1533,
        "regionCode": 25,
        // "pos": {
        //   "xpos": 27.483674,
        //   "ypos": 57.123734,
        // },
        "brand": "cgv",
        "theaterFlag": {
          "locationalKeyword": ['왕십리', '한양대', '성동구']
        },
      },
      "movieScheduleFlag": {
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "digitalized": true,            // 디지털 / 필름
        "lateNight": false,              // 심야 여부
        "morning": false,   
      },
      "room": "7관",                 // 상영관
      "movieCode": 234234,  
    },
    {
      "movie": {
        "movieName": "타짜",
        "duration": 140,
        "movieRating": "15세관람가",
        "director": '토드 스필버그',
        "actors": ['조셉 고든 래빗', '호아킨 피닉스'],
        "genre": ['액션', '드라마'],
      },
      // startTime: dates.ZonedDateTime.now(),
      // endTime: dates.ZonedDateTime.now(),
      "totalSeat": 234,             // 총 좌석수
      "availableSeat": 123,             // 빈 좌석수
      "theater": {
        "theaterName": "왕십리 CGV",
        "theaterCode": 1533,
        "regionCode": 25,
        // "pos": {
        //   "xpos": 27.483674,
        //   "ypos": 57.123734,
        // },
        "brand": "cgv",
        "theaterFlag": {
          "locationalKeyword": ['왕십리', '한양대', '성동구']
        },
      },
      "movieScheduleFlag": {
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "digitalized": true,            // 디지털 / 필름
        "lateNight": false,              // 심야 여부
        "morning": false,   
      },
      "room": "7관",                 // 상영관
      "movieCode": 234234,  
    },
  ]


  return response;
}
