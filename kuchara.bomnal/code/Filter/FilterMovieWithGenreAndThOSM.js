module.exports.function = function filterMovieWithGenreAndThOSM (theaterOrderedScheduleWithMovie, genre, exceptExpression) {
  let result = [];
  let input = theaterOrderedScheduleWithMovie;

  // '제외하고', '빼고'와 같은 단어가 안들어온 경우
  // 해당 장르만 보여준다.
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movie.genre.includes(genre)){
        result.push(mosElement);
      }
    })
  } else {  
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.movie.genre.includes(genre)){
        result.push(mosElement);
      }
    })
  }

  return result
}
