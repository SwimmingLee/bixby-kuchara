let http = require('http');
let config = require('config');

module.exports.function = function findTheaterWithMovieSelected (namedPointStructure) {

  // let long = namedPointStructure.point.longitude;
  // let lat = namedPointStructure.point.latitutde;
  let long = 127.123843;
  let lat = 37.481394;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,

    }
  };
  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTheaterWithPosWithMovieName/', options); 

  return response;
}
