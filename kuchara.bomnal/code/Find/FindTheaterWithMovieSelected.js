let http = require('http');
let config = require('config');

module.exports.function = function findTheaterWithMovieSelected (namedPointStructure, movie) {

  let long = namedPointStructure.point.longitude;
  let lat = namedPointStructure.point.latitutde;

  if(typeof movie == 'undefined'){
    let options = { 
      format: 'json',
      query: { 
        longitude: long,
        latitude: lat,
        movieName: movie.movieName
      }
    };
  // let response = http.getUrl(config.get('remote.url') + '/api-name', options); 
  // 위치와 영화이름을 받아서 해당 위치 주변의 해당영화를 상영하는 영화관 리스트(TheaterInfo-TimeOrderedSchedule) 반환 
  } else {
    let options = { 
      format: 'json',
      query: { 
        longitude: long,
        latitude: lat,
      }
    };
    // let response = http.getUrl(config.get('remote.url') + '/api-name', options); 
    // 위치를 받아서 해당 위치 주변의 영화관 리스트(TheaterInfo-TimeOrderedSchedule) 반환 
  }


  // console.log(response);


  return {}
}
