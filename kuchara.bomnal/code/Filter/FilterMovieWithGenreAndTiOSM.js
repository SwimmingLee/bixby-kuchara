module.exports.function = function filterMovieWithGenreAndTiOSM (timeOrderedScheduleWithMovie, genreEnum, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
  let input = timeOrderedScheduleWithMovie;

  // '제외하고', '빼고'와 같은 단어가 안들어온 경우
  // 해당 장르만 보여준다.
  if(typeof exceptExpression == 'undefined'){
    
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].movie.genre.includes(genreEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      
    })
  } else {  
    if(!exceptExpression){
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].movie.genre.includes(genreEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })
    } else {
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.movieOrderedSchedule[0].movie.genre.includes(genreEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })
      
    }
  }

  return result
}
