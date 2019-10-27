module.exports.function = function filterMovieWithTheaterNameAndThOSM (theaterOrderedScheduleWithMovie, theaterName, brand, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
  let input = theaterOrderedScheduleWithMovie;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })
    } else {
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].theaterInfo.brand.includes(brand)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })

    }
  }
  input.movieOrderedSchedule = result;
  // console.log(result);
  return input;
}
