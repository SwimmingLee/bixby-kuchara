const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function showCloserTheaterList (movie) {
  let targetPosition = namedPointStructure;
  // let long = targetPosition.point.longitude;
  // let lat = targetPosition.point.latitutde;
  let long = 127.123843;
  let lat = 37.481395;

  let options = { 
    format: 'json',
    query: { 
      movieName: movie.movieName,
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchMovieListWithPos/', options); 
  console.log(response);

  let obj = {
    'movie': movie,
    theaterInfo: response,
  }

  return obj;
}
