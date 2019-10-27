module.exports.function = function filterMovieWithRoomFromTheaterOrderWithMovie (theaterOrderedScheduleWithMovie, roomPropertyEnum, exceptExpression) {
  let result = [];
  let input = theaterOrderedScheduleWithMovie;

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    input.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.push(mosElement);
      }
    })
  } else {
    if(!exceptExpression){
      input.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
          result.push(mosElement);
        }
      })
    } else {
      input.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
          result.push(mosElement);
        }
      })
    }
  }

  input.movieOrderedSchedule = result;

  return input;
}
