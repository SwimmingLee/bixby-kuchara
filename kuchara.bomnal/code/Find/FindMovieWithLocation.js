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
    timeOrderedScheduleWithMovie.movieOrderedSchedule.push(mosElement)
  })

  return timeOrderedScheduleWithMovie;
}
