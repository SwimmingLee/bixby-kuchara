module.exports.function = function filterMovieWithRoomFromTheaterOrder (theaterOrderedSchedule, roomPropertyEnum, exceptExpression) {

  let result = [];
  let input = theaterOrderedSchedule;

  // 부정어가 안들어오면, mx관만 보여줘
  if(typeof exceptExpression == 'undefined'){
    input.theater.forEach(function(theaterElement){
      theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
        if(theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
          result.push(theaterElement);
        }
      })
    })
  } else {    // 부정어가 들어오면,  
    if(!exceptExpression){
      input.theater.forEach(function(theaterElement){
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          if(theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
            result.push(theaterElement);
          }
        })
      })
    } else {
      input.theater.forEach(function(theaterElement){
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          if(!theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
            result.push(theaterElement);
          }
        })
      })
    }
    
  }
  input.theater = result;
  return input;
}
