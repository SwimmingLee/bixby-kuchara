module.exports.function = function filterMovieWithRoomFromTimeOrder (timeOrderedSchedule, roomPropertyEnum, exceptExpression) {
  let result = {
    'movie': timeOrderedSchedule.movie,
    'timeSchedule': [],
  }

  // 부정어가 안들어오면, mx관만 보여줘
  if(typeof exceptExpression == 'undefined'){
    timeOrderedSchedule.timeSechedule.forEach(function(timeSecheduleElement){
      let obj2str = timeSecheduleElement.roomProperty + "";
      if(obj2str.includes(roomPropertyEnum)){
        result.push(timeSecheduleElement);
      }
    })
  } else {    // 부정어가 들어오면,  
    if(!exceptExpression){
      timeOrderedSchedule.timeSechedule.forEach(function(timeSecheduleElement){
        let obj2str = timeSecheduleElement.roomProperty + "";
        if(obj2str.includes(roomPropertyEnum)){
          result.push(timeSecheduleElement);
        }
      })
    } else {
      timeOrderedSchedule.timeSechedule.forEach(function(timeSecheduleElement){
        let obj2str = timeSecheduleElement.roomProperty + "";
        if(!obj2str.includes(roomPropertyEnum)){
          result.push(timeSecheduleElement);
        }
      })
    }
  }
  
  return result;
}
