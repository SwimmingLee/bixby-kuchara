let console = require('console');
let fail = require('fail');

module.exports.function = function filterMovieWithRoomFromTheaterOrder (theaterOrderedSchedule, roomPropertyEnum, exceptExpression) {

  let result = {
    'movie': theaterOrderedSchedule.movie,
    'theater': [],
  }

  // 부정어가 안들어오면, mx관만 보여줘
  if(typeof exceptExpression == 'undefined'){
    let theaterTemp = {};
    theaterOrderedSchedule.theater.forEach(function(theaterElement){
      theaterTemp = theaterElement;
      let theaterScheduleTemp = [];
      theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
        let obj2str = theaterScheduleElement.roomProperty + "";
        if(obj2str.includes(roomPropertyEnum)){
          theaterScheduleTemp.push(theaterScheduleElement);
        }
      })
      theaterTemp.theaterSchedule = theaterScheduleTemp;
      if(theaterTemp.theaterSchedule.length)
        result.theater.push(theaterTemp);
    })
  } else { // 부정어가 들어왔어!
    if(!exceptExpression){ // ~~ 만 보여줄래
      let theaterTemp = {};
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let obj2str = theaterScheduleElement.roomProperty + "";
          if(obj2str.includes(roomPropertyEnum)){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        if(theaterTemp.theaterSchedule.length)
          result.theater.push(theaterTemp);
      })
    } else { // ~~ 빼고 보여줘~~
      let theaterTemp = {};
        theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let obj2str = theaterScheduleElement.roomProperty + "";
          if(!obj2str.includes(roomPropertyEnum)){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        if(theaterTemp.theaterSchedule.length)
          result.theater.push(theaterTemp);
      })
    }
  }

  if(result.theater.length == 0) {
    throw fail.checkedError('There is no theater data', 'NoDataError', {})
  }

  return result;
}
