module.exports.function = function filterMovieWithRoomFromTimeOrder (timeOrderedSchedule, roomPropertyEnum, exceptExpression) {
  let result = [];
  let input = timeOrderedSchedule;

  // 부정어가 안들어오면, mx관만 보여줘
  if(typeof exceptExpression == 'undefined'){
    input.timeSechedule.forEach(function(timeSecheduleElement){
      if(timeSecheduleElement.roomProperty.includes(roomPropertyEnum)){
        result.push(timeSecheduleElement);
      }
    })
  } else {    // 부정어가 들어오면,  
    input.timeSechedule.forEach(function(timeSecheduleElement){
      if(!timeSecheduleElement.roomProperty.includes(roomPropertyEnum)){
        result.push(timeSecheduleElement);
      }
    })
  }
  input.timeSechedule = result;
  return input;
}
