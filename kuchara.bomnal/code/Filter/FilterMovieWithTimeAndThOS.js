let console = require('console');

module.exports.function = function filterMovieWithTimeAndThOS (theaterOrderedSchedule, dateTimeExpression, isStartTime) {
  let result = {
    'movie': theaterOrderedSchedule.movie,
    'theater': [],
  }

  let timeInput = dateTimeExpression.dateTime.time.hour*60;
  if (typeof dateTimeExpression.dateTime.time.minute != 'undefined') {
    timeInput += dateTimeExpression.dateTime.time.minute*1;
  }

  // input.theater = result; 이런 느낌?
  // 이후 시작하는 영화
  if(typeof isStartTime == 'undefined'){
    let theaterTemp = {};
    theaterOrderedSchedule.theater.forEach(function(theaterElement){
      theaterTemp = theaterElement;
      theaterTemp.theaterSchedule = [];
      theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
        let time = theaterScheduleElement.startTime + "";
        time = time.split(":");
        let aTime = time[0]*60 + time[1]*1;
        if(aTime >= timeInput){
          theaterTemp.theaterSchedule.push(theaterScheduleElement);
        }
      })
      result.theater.push(theaterTemp);
    })
  } else {
    // 시작하는: 이후 시작하는 영화
    if(isStartTime){
      let theaterTemp = {};
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let time = theaterScheduleElement.startTime + "";
          time = time.split(":");
          let aTime = time[0]*60 + time[1]*1;
          if(aTime >= timeInput){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        result.theater.push(theaterTemp);
      })
    } else {    // 끝나는: 인풋시간 이전에 끝나는 영화
      let theaterTemp = {};
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let time = theaterScheduleElement.startTime + "";
          time = time.split(":");
          let aTime = time[0]*60 + time[1]*1;
          if(aTime <= timeInput){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        result.theater.push(theaterTemp);
      })
    }
  }
  return result;
}
