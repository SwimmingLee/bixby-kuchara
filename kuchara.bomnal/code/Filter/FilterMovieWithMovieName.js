module.exports.function = function filterMovieWithMovieName (timeOrderedSchedule, movieName, exceptExpression) {
  let result = [];
  let input = timeOrderedSchedule;

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    input.forEach(function(el){
      if(el.movie.movieName.includes(movieName)){
        result.push(el);
      }
    })
  } else {
    input.forEach(function(el){
      if(!el.movie.movieName.includes(movieName)){
        result.push(el);
      }
    })
  }


  return result
}
