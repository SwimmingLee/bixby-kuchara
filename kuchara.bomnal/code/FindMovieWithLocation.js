// const movieReturn = require('./sample/exampleReturn.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithLocation (namedPointStructure) {

  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitutde;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + '/searchWithPos', options); 
  
  console.log(response);

  return response;
}
