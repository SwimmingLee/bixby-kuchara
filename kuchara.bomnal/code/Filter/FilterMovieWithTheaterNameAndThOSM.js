module.exports.function = function filterMovieWithTheaterNameAndThOSM (theaterOrderedScheduleWithMovie, theaterName, brand, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    } else {
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    }
  }
  // console.log(result);
  return result;
}
