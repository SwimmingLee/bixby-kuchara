module.exports.function = function filterMovieWithMovieNameAndThOSM (theaterOrderedScheduleWithMovie, movieName, exceptExpression) {
  let result = [];
  let input = theaterOrderedScheduleWithMovie;

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.movieName.includes(movieName)){
        result.push(mosElement);
      }
    })
  } else {
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.movie.movieName.includes(movieName)){
        result.push(mosElement);
      }
    })
  }

  input.movieOrderedSchedule = result;

  return input;
}