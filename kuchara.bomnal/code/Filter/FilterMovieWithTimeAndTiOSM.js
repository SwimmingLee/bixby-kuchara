module.exports.function = function filterMovieWithTimeAndTiOSM (timeOrderedScheduleWithMovie, dateTimeExpression, isStartTime) {
  let result = [];
  let input = timeOrderedScheduleWithMovie;

  let timeInput = dateTimeExpression.dateTime.time.hour*60 + dateTimeExpression.dateTime.time.minute*1;

  // 이후 시작하는 영화
  if(typeof isStartTime == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      let time = mosElement.theaterSchedule.startTime.split(":");
      let aTime = time[0]*60 + time[1]*1;
      if(aTime >= time){
        result.push(mosElement);
      }
    })
  } else {
    // 시작하는: 이후 시작하는 영화
    if(isStartTime){
      input.movieOrderedSchedule.forEach(function(mosElement){
      let time = mosElement.theaterSchedule.startTime.split(":");
      let aTime = time[0]*60 + time[1]*1;
      if(aTime >= time){
        result.push(mosElement);
      }
    })
    } else {    // 끝나는: 인풋시간 이전에 끝나는 영화
      input.movieOrderedSchedule.forEach(function(mosElement){
      let time = mosElement.theaterSchedule.startTime.split(":");
      let aTime = time[0]*60 + time[1]*1;
      if(aTime <= time){
        result.push(mosElement);
      }
    })
    }
  }
  input.movieOrderedSchedule = result;
  return input;
}
