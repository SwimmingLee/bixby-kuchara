module.exports.function = function filterMovieWithTimeAndTiOS (timeOrderedSchedule, dateTimeExpression, isStartTime) {
  let result = {
    'movie': timeOrderedSchedule.movie,
    'timeSchedule': [],
  }

  let timeInput = dateTimeExpression.dateTime.time.hour*60;
  if (typeof dateTimeExpression.dateTime.time.minute != 'undefined') {
    timeInput += dateTimeExpression.dateTime.time.minute*1;
  }

  // 이후 시작하는 영화
  if(typeof isStartTime == 'undefined'){
    timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
      let time = mosElement.theaterSchedule.startTime + "";
      time = time.split(":")
      let aTime = time[0]*60 + time[1]*1;
      if(aTime >= timeInput){
        result.timeSchedule.push(timeScheduleElement);
      }
    })
  } else {
    // 시작하는: 이후 시작하는 영화
    if(isStartTime){
      timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
        let time = mosElement.theaterSchedule.startTime + "";
        time = time.split(":")
        let aTime = time[0]*60 + time[1]*1;
        if(aTime >= timeInput){
          result.timeSchedule.push(timeScheduleElement);
        }
      })
    } else {    // 끝나는: 인풋시간 이전에 끝나는 영화
      timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
        let time = mosElement.theaterSchedule.endTime + "";
        time = time.split(":")
        let aTime = time[0]*60 + time[1]*1;
        if(aTime <= timeInput){
          result.timeSchedule.push(timeScheduleElement);
        }
      })
    }
  }

  return result;
}
