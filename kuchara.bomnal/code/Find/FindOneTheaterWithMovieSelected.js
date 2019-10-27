const movieReturn = require('sample/newStructure.js');
const getUriList = require('api/makeRoomPropertyList.js');
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

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchMovieScheduleWithMovieTheater/', options);
  console.log(response);

  response.theater.forEach(function(theaterElement){
    theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
      let rp = theaterScheduleElement.roomProperty;
      let db = theaterScheduleElement.dubbing;
      let list = getUriList(rp, db);
      console.log(list);
      theaterScheduleElement.roomPropertyUriList = [];
      list.forEach(function(el){
        theaterScheduleElement.roomPropertyUriList.push({roomPropertyUri: el});
      })

      console.log(theaterScheduleElement.roomPropertyUriList);
    })
  })

  return response;
}
