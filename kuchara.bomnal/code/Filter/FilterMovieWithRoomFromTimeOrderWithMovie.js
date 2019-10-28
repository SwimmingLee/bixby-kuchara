module.exports.function = function filterMovieWithRoomFromTimeOrderWithMovie (timeOrderedScheduleWithMovie, roomPropertyEnum, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {
    if(!exceptExpression){
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    } else {
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      if(!mosElement.theaterSchedule.roomProperty.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement);
      }
      })
    }
  }

  return result;
}
