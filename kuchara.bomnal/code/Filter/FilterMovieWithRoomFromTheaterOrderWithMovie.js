module.exports.function = function filterMovieWithRoomFromTheaterOrderWithMovie (theaterOrderedScheduleWithMovie, roomPropertyEnum, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
  let input = theaterOrderedScheduleWithMovie;

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
    })
  } else {
    if(!exceptExpression){
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.movieOrderedSchedule[0].theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })
    } else {
      input.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.movieOrderedSchedule[0].theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement.movieOrderedSchedule[0]);
      }
      })
    }
  }

  input.movieOrderedSchedule = result;

  return input;
}
