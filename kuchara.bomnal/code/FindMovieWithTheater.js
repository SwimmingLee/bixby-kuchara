let console = require('console');
const movieReturn = require('./sample/exampleReturn.js');

module.exports.function = function findMovieWithTheater (locationalKeyword, brand) {
  if(locationalKeyword){
    console.log("no locational keyword")
  } else {
    console.log(locationalKeyword)
  }

  let response = movieReturn;
  return response;
}
