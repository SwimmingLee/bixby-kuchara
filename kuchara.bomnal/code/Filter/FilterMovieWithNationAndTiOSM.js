let console = require('console');
let fail = require('fail');

module.exports.function = function filterMovieWithNationAndTiOSM (timeOrderedScheduleWithMovie, nation, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };
​
  // 우리나라 키워드가 없으면,
  if(typeof isDomestic == 'undefined'){
    // '제외하고', '빼고'와 같은 단어가 안들어온 경우
    // 해당 장르만 보여준다.
    if(typeof exceptExpression == 'undefined'){
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes(nation)){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {
      if(!exceptExpression){
        timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes(nation)){
          result.movieOrderedSchedule.push(mosElement);
        }
        })
      } else {
        timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
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
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(mosElement.movie.nation.includes("한국")){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    } else {    // 외국 키워드가 들어오면,
      timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        if(!mosElement.movie.nation.includes("한국")){
          result.movieOrderedSchedule.push(mosElement);
        }
      })
    }
  }

  if(result.movieOrderedSchedule.length == 0) {
    throw fail.checkedError('There is no theater data', 'NoDataError', {})
  }

  return result;
}
