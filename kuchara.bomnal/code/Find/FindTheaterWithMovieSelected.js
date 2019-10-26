const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function showCloserTheaterList (movieName, namedPointStructure) {
  let targetPosition = namedPointStructure;
  // let long = targetPosition.point.longitude;
  // let lat = targetPosition.point.latitutde;
  let long = 127.123843;
  let lat = 37.481395;

  let options = { 
    format: 'json',
    query: { 
      movieName: movieName,
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTheaterWithMPos/', options); 
  console.log(response);

  let obj = {
    'movieName': movieName,
    theaterInfo: response,
  }

  return obj;
}
