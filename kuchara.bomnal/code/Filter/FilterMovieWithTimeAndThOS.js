let console = require('console');

module.exports.function = function filterMovieWithTimeAndThOS (theaterOrderedSchedule, dateTimeExpression, isStartTime) {
  let result = [];
  let input = theaterOrderedSchedule;

  let timeInput = dateTimeExpression.dateTime.time.hour*60 + dateTimeExpression.dateTime.time.minute*1;

  // 이후 시작하는 영화
  if(typeof isStartTime == 'undefined'){
    input.theater.forEach(function(theaterElement){
      theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
        let time = theaterScheduleElement.startTime.split(":");
        let aTime = time[0]*60 + time[1]*1;
        if(aTime >= time){
          result.push(theaterScheduleElement);
        }
      })
      theaterElement.theaterSchedule = result;
      result = [];
    })
  } else {
    // 시작하는: 이후 시작하는 영화
    if(isStartTime){
      input.theater.forEach(function(theaterElement){
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let time = theaterScheduleElement.startTime.split(":");
          let aTime = time[0]*60 + time[1]*1;
          if(aTime >= time){
            result.push(theaterScheduleElement);
          }
        })
        theaterElement.theaterSchedule = result;
        result = [];
      })
    } else {    // 끝나는: 인풋시간 이전에 끝나는 영화
      input.theater.forEach(function(theaterElement){
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          let time = theaterScheduleElement.endTime.split(":");
          let aTime = time[0]*60 + time[1]*1;
          if(aTime <= time){
            result.push(theaterScheduleElement);
          }
        })
        theaterElement.theaterSchedule = result;
        result = [];
      })
    }
  }
  return input;
  
  // return {}
}
