module.exports.function = function filterMovieWithTimeAndTiOS (timeOrderedSchedule, dateTimeExpression, isStartTime) {
  let result = [];
  let input = movieSchedule;

  // 이후 시작하는 영화
  if(typeof isStartTime == 'undefined'){
  //   input.forEach(function(el){
  //     if(!el.theater.theaterName.includes(theaterName)){
  //       result.push(el);
  //     }
  //   })
  // } else {
  //   input.forEach(function(el){
  //     if(el.theater.theaterName.includes(theaterName)){
  //       result.push(el);
  //     }
  //   })
  } else {
    // 시작하는: 이후 시작하는 영화
    if(isStartTime){

    } else {    // 끝나는: 인풋시간 이전에 끝나는 영화

    }
  }
  return result
  
  return {}
}
