let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithTheater (brand, regionCode, theaterCode) {

  

  let options = { 
    format: 'json',
    query: { 
      brand: brand,
      theaterCode: theaterCode,
      retionCode: regionCode
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchMovieWithTheater/', options); 

  return response;
}
