module.exports.function = function filterMovieWithNationAndThOSM (theaterOrderedScheduleWithMovie, nation, isDomestic, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
​
​
  // 우리나라 키워드가 없으면,
  if(typeof isDomestic == 'undefined'){
    // '제외하고', '빼고'와 같은 단어가 안들어온 경우
    // 해당 장르만 보여준다.
    if(typeof exceptExpression == 'undefined'){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes(nation)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {  
      if(!exceptExpression){
        theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes(nation)){
          result.movieOrderedSchedule.push(mosElement);
        }
        })
      } else {
        theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.nation.includes(nation)){
          result.movieOrderedSchedule.push(mosElement);
        }
        })
      }
    }
​
  } else {
    // 우리나라 키워드가 들어오면,
    if(isDomestic){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes("한국")){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {    // 외국 키워드가 들어오면,
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.nation.includes("한국")){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }
​
  return result;
}