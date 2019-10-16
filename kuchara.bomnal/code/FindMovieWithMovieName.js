const movieReturn = require('./sample/exampleReturn.js');

module.exports.function = function findMovieWithMovieName (movieName) {
  let response = movieReturn;
  let result = [];
  if(movieName){
    response.forEach(function(el){
      if(el.movie.movieName == movieName){
        result.push(el);
      }
    })
  } else {
    result = movieReturn;
  }

  // 수정: movieName을 api서버로 던지면 서버에서 일치하는 movieSchedule 객체를 반환해준다. 그걸 리턴 ㄴ

  return result;
}
