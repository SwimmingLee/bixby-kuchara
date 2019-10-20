const movieReturn = require('./sample/exampleReturn.js');
let console = require('console');

module.exports.function = function findMovieWithMovieName (movieInput) {
  let response = movieReturn;

  console.log(response);
  console.log(movieInput);
  
  let result = [];
  if(typeof movieInput != 'undefiened'){
    response.forEach(function(el){
      if(el.movie.movieName == movieInput.movieName){
        result.push(el);
      }
    })
  } else {
    result = movieReturn;
  }

  // 수정: movieName을 api서버로 던지면 서버에서 일치하는 movieSchedule 객체를 반환해준다. 그걸 리턴 ㄴ

  return result;
}
