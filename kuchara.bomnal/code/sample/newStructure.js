// 영화관 순 보기
module.exports = 
  {
    'movie':{
      'movieName': "조커",
      "duration": 130,
      "movieRating": "15세관람가",
      "director": '스티븐 스필버그',
      "actors": '히스레저, 조셉 고든 래빗',
      "genre": '액션, 드라마',
      "imgUrl":"https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167635_P27_100146.jpg",
      "userRating":0.0,
      'nation': 'korea'
    },

    'theater':[
      {
        'theaterInfo': {
          'brand' : "cgv",
          "theaterName": "영통",
          'longitude' : 123.123,
          'latitude' : 123.123,
          "theaterCode": 1533,
          "regionCode": 25,
          'iconUri':"/images/brand/theater/1x/cgv.png",
        },
        'theaterSchedulePack' : [
          {
          'theaterSchedule': [
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_1px.png"
              // morning, latenight
            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_2px.png"
            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_4px.png"
            }
          ]},
          {
          'theaterSchedule': [
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_8px.png"

            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": 'IMAX'

            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": 'IMAX'
            }
          ] },
          {
          'theaterSchedule': [
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_1px.png"

            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_2px.png"

            },
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_4px.png"
            }
          ] },
          {
          'theaterSchedule': [
            {
              'startTime': '18:00',
              'endTime': '19:50',
              "totalSeat": 234,             // 총 좌석수
              "availableSeat": 123,             // 빈 좌석수
              "subtitle": true,               // 자막여부
              "dubbing": true,
              "room": '7관',
              "roomProperty": "/images/roomProperty/padding_8px.png"
            },
          ]
          }
        ]
      },
      {
        'theaterInfo': {
          'brand' : "cgv",
          "theaterName": "영토옹",
          'longitude' : 123.123,
          'latitude' : 123.123,
          "theaterCode": 1533,
          "regionCode": 25,
          'iconUri':"/images/brand/theater/1x/lotte.png",  // 만들어야 함!
        },
        'theaterSchedulePack' : [
          {
          'theaterSchedule': [
          {
            'startTime': '18:00',
            'endTime': '19:50',
            "totalSeat": 234,             // 총 좌석수
            "availableSeat": 123,             // 빈 좌석수
            "subtitle": true,               // 자막여부
            "dubbing": true,
            "room": '7관',
            "roomProperty": "/images/roomProperty/padding_1px.png"
            // morning, latenight
          },
          {
            'startTime': '18:00',
            'endTime': '19:50',
            "totalSeat": 234,             // 총 좌석수
            "availableSeat": 123,             // 빈 좌석수
            "subtitle": true,               // 자막여부
            "dubbing": true,
            "room": '7관',
            "roomProperty": "/images/roomProperty/padding_2px.png"
          },
          {
            'startTime': '18:00',
            'endTime': '19:50',
            "totalSeat": 234,             // 총 좌석수
            "availableSeat": 123,             // 빈 좌석수
            "subtitle": true,               // 자막여부
            "dubbing": true,
            "room": '7관',
            "roomProperty": "/images/roomProperty/padding_4px.png"
          }
          ]},
          {
            'theaterSchedule':
          [
          {
            'startTime': '18:00',
            'endTime': '19:50',
            "totalSeat": 234,             // 총 좌석수
            "availableSeat": 123,             // 빈 좌석수
            "subtitle": true,               // 자막여부
            "dubbing": true,
            "room": '7관',
            "roomProperty": "/images/roomProperty/padding_8px.png"
          },
          ]
          }
        ]
      },
    ]
  }