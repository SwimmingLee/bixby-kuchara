module.exports.function = function filterMovieWithTheaterNameAndThOSM (theaterOrderedScheduleWithMovie, theaterName, brand, exceptExpression) {
  let result = {
    movieOrderedSchedule: []
  };

  let _brand = false, _theaterName = false;
  if(typeof brand != 'undefined') _brand = true;
  if(typeof theaterName != 'undefined') _theaterName = true;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
      let brand_obj2str = mosElement.theaterInfo.brand + "";
      if(_brand) {
        if(_theaterName) {
          if(mosElement.theaterInfo.theaterName.includes(theaterName) && 
            brand_obj2str.includes(brand)){
            result.movieOrderedSchedule.push(mosElement);
          }
        }
        else {
          if(brand_obj2str.includes(brand)){
            result.movieOrderedSchedule.push(mosElement);
          }
        }
      }
      else {
        if(mosElement.theaterInfo.theaterName.includes(theaterName)){
          result.movieOrderedSchedule.push(mosElement);
        }
      }
    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        let brand_obj2str = mosElement.theaterInfo.brand + "";
        if(_brand) {
          if(_theaterName) {
            if(mosElement.theaterInfo.theaterName.includes(theaterName) && 
              brand_obj2str.includes(brand)){
              result.movieOrderedSchedule.push(mosElement);
            }
          }
          else {
            if(brand_obj2str.includes(brand)){
              result.movieOrderedSchedule.push(mosElement);
            }
          }
        }
        else {
          if(mosElement.theaterInfo.theaterName.includes(theaterName)){
            result.movieOrderedSchedule.push(mosElement);
          }
        }
      })
    } else {
      theaterOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement){
        let brand_obj2str = mosElement.theaterInfo.brand + "";
        if(_brand) {
          if(_theaterName) {
            if(!(mosElement.theaterInfo.theaterName.includes(theaterName) && 
              brand_obj2str.includes(brand))){
              result.movieOrderedSchedule.push(mosElement);
            }
          }
          else {
            if(!brand_obj2str.includes(brand)){
              result.movieOrderedSchedule.push(mosElement);
            }
          }
        }
        else {
          if(!mosElement.theaterInfo.theaterName.includes(theaterName)){
            result.movieOrderedSchedule.push(mosElement);
          }
        }
      })
    }
  }
  // console.log(result);
  return result;
}
