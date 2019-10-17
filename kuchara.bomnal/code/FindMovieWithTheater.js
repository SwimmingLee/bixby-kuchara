let console = require('console');
let http = require('http');
let config = require('config');
// const movieReturn = require('./sample/exampleReturn.js');

module.exports.function = function findMovieWithTheater (namedPointStructure, brand) {

  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitutde;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,
      brand: brand,
    }
  };

  let response = http.getUrl(config.get('remote.url') + '/searchWithTheater', options); 

  if(namedPointStructure){
    console.log("no namedPointStructure")
  } else {
    console.log(namedPointStructure)
  }

  return response;
}
