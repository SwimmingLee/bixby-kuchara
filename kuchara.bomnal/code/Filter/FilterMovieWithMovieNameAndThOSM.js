module.exports.function = function filterMovieWithMovieNameAndThOSM (theaterOrderedScheduleWithMovie, movieName, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
  
  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.movieName.includes(movieName)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {
    if(!exceptExpression){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }

  return result;
}