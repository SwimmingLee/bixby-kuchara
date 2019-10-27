const movieReturn = require('sample/newStructure.js');
const getUriList = require('api/makeRoomPropertyList.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findOneTheaterWithMovieSelected (movieName, brand, regionCode, theaterCode) {

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

  let obj = {
    movie: response[0].movie,
    theater: {
      theaterInfo: response[0].theaterInfo,
      theaterSchedule: [],
    }
  }

  response.forEach(function(responseElement) {
    let rp = responseElement.theaterSchedule.roomProperty;
    let db = responseElement.theaterSchedule.dubbing;
    let list = getUriList(rp, db);
    responseElement.theaterSchedule.roomPropertyUriList = [];
    list.forEach(function(el) {
      responseElement.theaterSchedule.roomPropertyUriList.push({roomPropertyUri: el});
    })
    obj.theater.theaterSchedule.push(responseElement.theaterSchedule);
  });

  return obj;
}
