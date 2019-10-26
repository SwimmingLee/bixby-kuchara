const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithMovieAndPos (movieInput, namedPointStructure) {
  let targetPosition = namedPointStructure;
  // let long = targetPosition.point.longitude;
  // let lat = targetPosition.point.latitutde;
  let long = 127.123843;
  let lat = 37.481394;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,
      movieName: movieInput.movieName,
    }
  };
  
  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTheaterOrderedScheduleWithPos/', options); 

  return response;
}
