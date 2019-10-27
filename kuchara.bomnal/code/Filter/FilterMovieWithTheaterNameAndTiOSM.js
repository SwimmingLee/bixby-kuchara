module.exports.function = function filterMovieWithTheaterNameAndTiOSM (timeOrderedScheduleWithMovie, theaterName, brand, exceptExpression) {
  let result = [];
  let input = timeOrderedScheduleWithMovie;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.theaterInfo.theaterName.includes(theaterName)){
        result.push(mosElement);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      input.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.theaterInfo.theaterName.includes(theaterName)){
          result.push(mosElement);
        }
      })
    } else {
      input.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.theaterInfo.theaterName.includes(theaterName)){
          result.push(mosElement);
        }
      })

    }
  }
  input.movieOrderedSchedule = result;
  // console.log(result);
  return input;
}
