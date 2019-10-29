module.exports.function = function filterMovieWithRoomFromTheaterOrder (theaterOrderedSchedule, roomPropertyEnum, exceptExpression) {

  let result = {
    'movie': theaterOrderedSchedule.movie,
    'theater': [],
  }

  // 부정어가 안들어오면, mx관만 보여줘
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedSchedule.theater.forEach(function(theaterElement){
      theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
        if(theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
          result.push(theaterElement);
        }
      })
    })
  } else { // 부정어가 들어왔어!
    if(!exceptExpression){ // ~~ 만 보여줄래
      let theaterTemp = {};
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          if(theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        if(theaterTemp.theaterSchedule.length)
          result.theater.push(theaterTemp);
      })
    } else { // ~~ 빼고 보여줘~~
      let theaterTemp = {};
        theaterOrderedSchedule.theater.forEach(function(theaterElement){
        theaterTemp = theaterElement;
        let theaterScheduleTemp = [];
        theaterElement.theaterSchedule.forEach(function(theaterScheduleElement){
          if(!theaterScheduleElement.roomProperty.includes(roomPropertyEnum)){
            theaterScheduleTemp.push(theaterScheduleElement);
          }
        })
        theaterTemp.theaterSchedule = theaterScheduleTemp;
        if(theaterTemp.theaterSchedule.length)
          result.theater.push(theaterTemp);
      })
    }
  }

  return result;
}
