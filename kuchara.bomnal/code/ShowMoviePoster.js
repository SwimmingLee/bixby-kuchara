let http = require("http");
let config = require("config");
let console = require("console");

const movieReturn = require('./sample/exampleMovieReturn.js');

module.exports.function = function showMoviePoster (namedPointStructure) {

  let targetPosition = namedPointStructure;
  // let long = targetPosition.point.longitude;
  // let lat = targetPosition.point.latitutde;
  let long = 127.123843;
  let lat = 37.481395;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchMovieListWithPos/', options); 
  console.log(response);
  return response;
}
