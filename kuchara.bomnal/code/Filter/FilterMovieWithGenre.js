module.exports.function = function filterMovieWithGenre (movie, genre, exceptExpression) {
  let result = [];
  let input = movie;

  // '제외하고', '빼고'와 같은 단어가 안들어온 경우
  // 해당 장르만 보여준다.
  if(typeof exceptExpression == 'undefined'){
    input.forEach(function(el){
      if(el.genre.toString().includes(genre)){
        result.push(el);
      }
    })
  } else {  
    input.forEach(function(el){
      if(!el.genre.toString().includes(genre)){
        result.push(el);
      }
    })
  }

  return result
}
