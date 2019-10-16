module.exports.function = function filterMovieWithMovieName (movieSchedule, movieName, exceptExpression) {
  let result = [];
  let input = movieSchedule;
  if(exceptExpression){
    input.forEach(function(el){
      if(!el.movie.movieName.includes(movieName)){
        result.push(el);
      }
    })
  } else {
    input.forEach(function(el){
      if(el.movie.movieName.includes(movieName)){
        result.push(el);
      }
    })
  }
  return result
}
