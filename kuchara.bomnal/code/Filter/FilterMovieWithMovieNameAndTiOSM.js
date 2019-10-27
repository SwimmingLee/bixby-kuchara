let console = require('console');
module.exports.function = function filterMovieWithMovieNameAndTiOSM (timeOrderedScheduleWithMovie, movieName, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
  let input = timeOrderedScheduleWithMovie;

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    input.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].movie.movieName.includes(movieName)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
    })
  } else {
    if(!exceptExpression){
      input.forEach(function(mosElement){
        if(mosElement.movieOrderedSchedule[0].movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
        }
      })
    } else {
      input.forEach(function(mosElement){
        if(!mosElement.movieOrderedSchedule[0].movie.movieName.includes(movieName)){
          result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
        }
      })
    }
  }

  
  return result;
}
