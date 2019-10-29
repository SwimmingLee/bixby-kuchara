let console = require('console');

module.exports.function = function filterMovieWithTheaterNameAndTiOS (timeOrderedSchedule, theaterName, brand, exceptExpression) {

  let result = {
    'movie': timeOrderedSchedule.movie,
    'timeSchedule': [],
  }

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    let timeScheduleTemp = {};
    timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
      timeScheduleTemp = timeScheduleElement;
      let theaterInfoTemp = [];
      timeScheduleElement.theaterInfo.forEach(function(theaterInfoElement) {
        if(!theaterInfoElement.theaterName.includes(theaterName)) {
          theaterInfoTemp.push(theaterInfoElement);
        }
      })
      timeScheduleTemp.theaterInfo = temp;
      result.timeSchedule.push(timeScheduleTemp);
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      let timeScheduleTemp = {};
        timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
          timeScheduleTemp = timeScheduleElement;
          let theaterInfoTemp = [];
          timeScheduleElement.theaterInfo.forEach(function(theaterInfoElement) {
            if(!theaterInfoElement.theaterName.includes(theaterName)) {
              theaterInfoTemp.push(theaterInfoElement);
            }
          })
        timeScheduleTemp.theaterInfo = temp;
        result.timeSchedule.push(timeScheduleTemp);
      })
    } else {
      let timeScheduleTemp = {};
        timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
          timeScheduleTemp = timeScheduleElement;
          let theaterInfoTemp = [];
          timeScheduleElement.theaterInfo.forEach(function(theaterInfoElement) {
            if(!theaterInfoElement.theaterName.includes(theaterName)) {
              theaterInfoTemp.push(theaterInfoElement);
            }
          })
        timeScheduleTemp.theaterInfo = temp;
        result.timeSchedule.push(timeScheduleTemp);
      })
    }
  }
  console.log(result);
  return result;
}
