const getUriList = require('api/makeRoomPropertyList.js');
const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithMovieAndPos (movie, namedPointStructure) {
  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitude;
  // let long = 127.123843;
  // let lat = 37.481395;

  let options = {
    format: 'json',
    cacheTime: 0,
    query: {
      longitude: long,
      latitude: lat,
      movieName: movie.movieName,
    }
  };

  let response = http.getUrl(config.get('remote.url') + 'movie_api/searchTheaterOrderedScheduleWithPos/', options);
  // let response = movieReturn;
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

  console.log("rpurilist");
  console.log(response);

  // let checkedTheater = [];

  // response.theater.every(function(theaterEl){
  //   theaterEl.theaterSchedule.every(function(scheduleEl){

  //   })
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

  return response;
}
