module.exports.function = function filterMovieWithNationAndThOSM (theaterOrderedScheduleWithMovie, nation, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // '제외하고', '빼고'와 같은 단어가 안들어온 경우
  // 해당 장르만 보여준다.
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.nation.includes(nation)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {  
    if(!exceptExpression){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.nation.includes(nation)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    } else {
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.movie.nation.includes(nation)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    }
  }

  return result;
}