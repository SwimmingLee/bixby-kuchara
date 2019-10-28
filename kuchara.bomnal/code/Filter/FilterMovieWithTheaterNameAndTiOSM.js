module.exports.function = function filterMovieWithTheaterNameAndTiOSM (timeOrderedScheduleWithMovie, theaterName, brand, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterInfo.theaterName.includes(theaterName)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterInfo.theaterName.includes(theaterName)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    } else {
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.theaterInfo.theaterName.includes(theaterName)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    }
  }
  // console.log(result);
  return input;
}
