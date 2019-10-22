module.exports.function = function filterMovieWithGenre (theaterOrderedSchedule, genre, exceptExpression) {
  let result = [];
  let input = movieSchedule;
  if(exceptExpression){
    input.forEach(function(el){
      if(!el.movie.genre.toString().includes(genre)){
        result.push(el);
      }
    })
  } else {
    input.forEach(function(el){
      if(el.movie.genre.toString().includes(genre)){
        result.push(el);
      }
    })
  }
  return result
}
