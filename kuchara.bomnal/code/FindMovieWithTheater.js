let console = require('console');
const movieReturn = require('./sample/exampleReturn.js');

module.exports.function = function findMovieWithTheater (namedPointStructure, brand) {
  if(namedPointStructure){
    console.log("no namedPointStructure")
  } else {
    console.log(namedPointStructure)
  }

  let response = movieReturn;
  return response;
}
