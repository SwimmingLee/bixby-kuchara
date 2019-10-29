module.exports.function = function filterMovieWithRoomFromTheaterOrderWithMovie (theaterOrderedScheduleWithMovie, roomPropertyEnum, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  // 제외해줘 표현 없으면 그거만 보여주기
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      let obj2str = mosElement.theaterSchedule.roomProperty + "";
      if(obj2str.includes(roomPropertyEnum)){
        result.movieOrderedSchedule.push(mosElement);
      }
    })
  } else {
    if(!exceptExpression){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        let obj2str = mosElement.theaterSchedule.roomProperty + "";
        if(obj2str.includes(roomPropertyEnum)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        let obj2str = mosElement.theaterSchedule.roomProperty + "";
        if(!obj2str.includes(roomPropertyEnum)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }

  return result;
}
