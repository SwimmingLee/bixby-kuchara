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
    cacheTime: 0,
    query: {
      longitude: long,
      latitude: lat,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTimeOrderedScheduleWithPos/', options);

  let timeOrderedScheduleWithMovie = {
    movieOrderedSchedule: []
  };
  console.log (response);
  response.forEach(function(mosElement){
    let rp = mosElement.theaterSchedule.roomProperty;
    // let db = mosElement.theaterSchedule.dubbing;
    let db = false;
    let list = getUriList(rp, db);
    mosElement.theaterSchedule.roomPropertyUriList = [];
    list.forEach(function(el) {
      mosElement.theaterSchedule.roomPropertyUriList.push({roomPropertyUri: el});
    })
    
    timeOrderedScheduleWithMovie.movieOrderedSchedule.push(mosElement)
  });

  let checkedMOS = [];

  console.log(timeOrderedScheduleWithMovie)
  // timeOrderedScheduleWithMovie.movieOrderedSchedule.every(function(el){
  //   if(typeof el.theaterSchedule == 'undefined'){
  //     return true;
  //   } else if(typeof el.theaterInfo == 'undefined'){
  //     return true;
  //   } else if(typeof el.movie == 'undefined'){
  //     return true;
  //   }
  //   checkedMOS.push(el);
  // })
  // timeOrderedScheduleWithMovie.movieOrderedSchedule = checkedMOS;

  return timeOrderedScheduleWithMovie;
}
