const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function showCloserTheaterList (theaterOrderedSchedule, namedPointStructure) {
  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitude;
  // let long = 127.123843;
  // let lat = 37.481395;

  let options = { 
    format: 'json',
    cacheTime: 0,
    query: { 
      movieName: theaterOrderedSchedule.movie.movieName,
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTheaterWithMoviePos/', options); 
  console.log(response);

  let obj = {
    'movieName': theaterOrderedSchedule.movie.movieName,
    theaterInfo: response,
  }

  return obj;
}
