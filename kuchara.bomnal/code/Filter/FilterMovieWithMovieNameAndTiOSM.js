let console = require('console');
let fail = require('fail');

module.exports.function = function filterMovieWithMovieNameAndTiOSM (timeOrderedScheduleWithMovie, movieName, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.movieName.includes(movieName)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {
    if(!exceptExpression){
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }

  if(result.movieOrderedSchedule.length == 0) {
    throw fail.checkedError('There is no theater data', 'NoDataError', {})
  }
  
  return result;
}
