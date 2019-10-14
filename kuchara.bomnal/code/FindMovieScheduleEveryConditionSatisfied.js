let http = require('http');
let config = require('config');
let dates = require('dates');

module.exports.function = function FindMovieScheduleEveryConditionSatisfied (movieName, theaterName, startTime) {
  let options = {
    format: "json",
    query: {
      movieName: movieName,
      theaterName: theaterName,
      startTime: startTime,
    }
  }
  
  // let response = http.getUrl(config.get('remote.url') + '/searchMovieWithFullParameter', options);

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
        "movieName": "조커123",
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
    }
  ]

  return response;
}



// MovieSchedule = {
//     movie: Object,
//     startTime: DateTime(),
//     endTime: DateTime(),
//     totalSeat: 0,             // 총 좌석수
//     availableSeat: 0,             // 빈 좌석수
//     theater: Object,
//     movieScheduleFlag: Object,
//     room: "",                 // 상영관
//     code: 0,                  // 각 영화사마다 조커의 코드가 달라서 movie에 안넣고 여기에 둠

//   }


// Movie = {
//     movieName: "",
//     duration: 0,
//     movieRating: 0,           // 관람등급
//     director: '',
//     actors: [],
//     genre: [],
//   }


  // Theater = {
  //   theaterName: "",
  //   code: 0,
  //   regioncode: 0,
  //   pos: Object,
  //   brand: Enum,
  //   TheaterFlag: Object,

  //   // roooms
  // }