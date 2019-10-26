const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findOneTheaterWithMovieSelected (movieName, brand, regionCode, theaterCode) {
  let targetPosition = namedPointStructure;
  
  let options = {
    format: 'json',
    query: {
      movieName: movieName,
      brand: brand,
      regionCode: regionCode,
      theaterCode: theaterCode,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/???/', options);
  console.log(response);
  return response;
}
