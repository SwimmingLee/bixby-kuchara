// 시간순 보기
module.exports = [
  {
    "movieName": "조커가조커가조커가조커가조커가조커가조커는조커다",
    "duration": 130,
    "movieRating": "15세관람가",
    "director": '스티븐 스필버그',
    "actors": ['히스레저', '조셉 고든 래빗'],
    "genre": '액션, 드라마',
    "imgUrl":"https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167635_P27_100146.jpg",
    "userRating":0.0,
   
    'schedule': [
      {
        'startTime': '18:00',
        'endTime': '19:50',
        "totalSeat": 234,             // 총 좌석수
        "availableSeat": 123,             // 빈 좌석수
        "room": "1관",                 // 상영관 
        "subtitle": true,               // 자막여부
        "dubbing": false,                // 더빙여부
        "roomProperty": "IMAX",

        "theaterInfo": {
          "theaterName": "영통",
          "theaterCode": 1533,
          "regionCode": 25,
          "brand": "megabox",
          'latitude':123.123,
          'longitude':123.123,
        },
      },

      {
        'startTime': '18:00',
        'endTime': '19:50',
        "totalSeat": 234,             // 총 좌석수
        "availableSeat": 123,             // 빈 좌석수
        "room": "1관",                 // 상영관 
        "theater": {
          "theaterName": "영통",
          "theaterCode": 1533,
          "regionCode": 25,
          "brand": "megabox",
        },
        "sheduleAttr": {
          "subtitle": true,               // 자막여부
          "dubbing": false,                // 더빙여부
          "roomProperty": "IMAX"
        },
      },
    ],
      
  },
]
  