module.exports.function = function filterMovieWithRoom (movieSchedule, room) {

  let result = [];
  let input = movieSchedule;
  input.forEach(function(el){
    if(el.room.includes(room)){
      result.push(el);
    }
  })
  return result
}