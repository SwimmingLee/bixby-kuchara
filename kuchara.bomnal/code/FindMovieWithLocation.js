const movieReturn = require('./sample/exampleReturn.js');
let console = require('console');

module.exports.function = function findMovieWithLocation (namedPointStructure) {

  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitutde;

  
  

  return movieReturn;
}
