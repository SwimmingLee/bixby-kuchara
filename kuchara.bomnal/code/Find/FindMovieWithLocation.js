const getUriList = require('api/makeRoomPropertyList.js');
const movieReturn = require('../sample/newStructure3.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithLocation (namedPointStructure) {

  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitude;

  let options = {
    format: 'json',
    query: {
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTimeOrderedScheduleWithPos/', options);

  let timeOrderedScheduleWithMovie = {
    movieOrderedSchedule: []
  };
  response.forEach(function(mosElement){
    let rp = mosElement.theaterSchedule.roomProperty;
    let db = mosElement.theaterSchedule.dubbing;
    let list = getUriList(rp, db);
    mosElement.theaterSchedule.roomPropertyUriList = [];
    list.forEach(function(el) {
      mosElement.theaterSchedule.roomPropertyUriList.push({roomPropertyUri: el});
    })
    timeOrderedScheduleWithMovie.movieOrderedSchedule.push(mosElement)
  });

  return timeOrderedScheduleWithMovie;
}
