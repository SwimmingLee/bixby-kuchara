module.exports.function = function filterMovieWithTheaterName (movieSchedule, theaterName, exceptExpression) {
  let result = [];
  let input = movieSchedule;
  if(exceptExpression){
    input.forEach(function(el){
      if(!el.theater.theaterName.includes(theaterName)){
        result.push(el);
      }
    })
  } else {
    input.forEach(function(el){
      if(el.theater.theaterName.includes(theaterName)){
        result.push(el);
      }
    })
  }
  return result
}
