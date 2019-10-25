let console = require('console');

module.exports.function = function filterMovieWithTheaterNameAndTheaterOrderedSchedule (theaterOrderedSchedule, theaterName, brand, exceptExpression) {
  let result = [];
  let input = theaterOrderedSchedule;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    input.theater.forEach(function(theaterElement){
      if(!theaterElement.theaterInfo.theaterName.includes(theaterName)){
        result.push(theaterElement);
      }
    })
  } else {  // 부정어가 들어오면, 제외
    input.forEach(function(el){
      if(theaterElement.theaterInfo.theaterName.includes(theaterName)){
        result.push(theaterElement);
      }
    })
  }
  theaterOrderedSchedule.theater = result;
  console.log(result);
  return theaterOrderedSchedule;
}
