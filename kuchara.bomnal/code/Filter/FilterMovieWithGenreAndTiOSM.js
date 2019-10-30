let console = require('console');
let fail = require('fail');

module.exports.function = function filterMovieWithGenreAndTiOSM (timeOrderedScheduleWithMovie, genreEnum, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // '제외하고', '빼고'와 같은 단어가 안들어온 경우
  // 해당 장르만 보여준다.
  if(typeof exceptExpression == 'undefined'){
    timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.genre.includes(genreEnum)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {  
    if(!exceptExpression){
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.genre.includes(genreEnum)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.genre.includes(genreEnum)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }

  if(result.movieOrderedSchedule.length == 0) {
    throw fail.checkedError('There is no theater data', 'NoDataError', {})
  }

  return result
}
