module.exports.function = function filterMovieWithRoom (movieSchedule, roomProperty) {

  let result = [];
  let input = movieSchedule;
  input.forEach(function(el){
    if(el.room.includes(room)){
      result.push(el);
    }
  })

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
