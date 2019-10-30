let console = require('console');
let fail = require('fail');

module.exports.function = function filterMovieWithTheaterNameAndTiOS (timeOrderedSchedule, theaterName, brand, exceptExpression) {

  let result = {
    'movie': timeOrderedSchedule.movie,
    'timeSchedule': [],
  }

  let _brand = false, _theaterName = false;
  if(typeof brand != 'undefined') _brand = true;
  if(typeof theaterName != 'undefined') _theaterName = true;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
      let brand_obj2str = timeScheduleElement.theaterInfo.brand + "";

      if(_brand) {
        if(_theaterName) {
          if(timeScheduleElement.theaterInfo.theaterName.includes(theaterName) && 
            brand_obj2str.includes(brand)) {
              result.timeSchedule.push(timeScheduleElement);
            }
        }
        else {
          if(brand_obj2str.includes(brand)){
            result.timeSchedule.push(timeScheduleElement);
          }
        }
      }
      else {
        if(timeScheduleElement.theaterInfo.theaterName.includes(theaterName)) {
          result.timeSchedule.push(timeScheduleElement);
        }
      }

    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
        let brand_obj2str = timeScheduleElement.theaterInfo.brand + "";

        if(_brand) {
          if(_theaterName) {
            if(timeScheduleElement.theaterInfo.theaterName.includes(theaterName) && 
              brand_obj2str.includes(brand)) {
                result.timeSchedule.push(timeScheduleElement);
              }
          }
          else {
            if(brand_obj2str.includes(brand)){
              result.timeSchedule.push(timeScheduleElement);
            }
          }
        }
        else {
          if(timeScheduleElement.theaterInfo.theaterName.includes(theaterName)) {
            result.timeSchedule.push(timeScheduleElement);
          }
        }

      })
    } else {
      timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
        let brand_obj2str = timeScheduleElement.theaterInfo.brand + "";

        if(_brand) {
          if(_theaterName) {
            if(!(timeScheduleElement.theaterInfo.theaterName.includes(theaterName) && 
              brand_obj2str.includes(brand))) {
                result.timeSchedule.push(timeScheduleElement);
              }
          }
          else {
            if(!brand_obj2str.includes(brand)){
              result.timeSchedule.push(timeScheduleElement);
            }
          }
        }
        else {
          if(!timeScheduleElement.theaterInfo.theaterName.includes(theaterName)) {
            result.timeSchedule.push(timeScheduleElement);
          }
        }
      })
    }
  }
  console.log(result);

  if(result.timeSchedule.length == 0) {
    throw fail.checkedError('There is no theater data', 'NoDataError', {})
  }

  return result;
}
