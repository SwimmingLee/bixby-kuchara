let console = require('console');

module.exports.function = function filterMovieWithTheaterNameAndTiOS (timeOrderedSchedule, theaterName, brand, exceptExpression) {

  let result = [];
  let input = timeOrderedSchedule;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    input.timeSchedule.forEach(function(timeScheduleElement){
      if(!timeScheduleElement.theaterInfo.theaterName.includes(theaterName)){
        result.push(timeScheduleElement);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      input.timeSchedule.forEach(function(timeScheduleElement){
        if(!timeScheduleElement.theaterInfo.theaterName.includes(theaterName)){
          result.push(timeScheduleElement);
        }
      })
    } else {
      input.timeSchedule.forEach(function(timeScheduleElement){
        if(timeScheduleElement.theaterInfo.theaterName.includes(theaterName)){
          result.push(timeScheduleElement);
        }
      })

    }
  }
  timeOrderedSchedule.timeSchedule = result;
  // console.log(result);
  return timeOrderedSchedule;
}
