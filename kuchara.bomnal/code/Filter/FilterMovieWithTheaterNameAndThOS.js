let console = require('console');

module.exports.function = function filterMovieWithTheaterNameAndTheaterOrderedSchedule (theaterOrderedSchedule, theaterName, brand, exceptExpression) {
  let result = {
    'movie': theaterOrderedSchedule.movie,
    'theater': [],
  }

  // 만약 얕은 복사라면 내부에 들어가는 일부 데이터들은 깨질 수 있음. 트레이닝 꼭 테스트!!

  let _brand = false, _theaterName = false;
  if(typeof brand != 'undefined') _brand = true;
  if(typeof theaterName != 'undefined') _theaterName = true;

  // 부정어가 안들어오면, 그것만
  if(typeof exceptExpression == 'undefined'){
    theaterOrderedSchedule.theater.forEach(function(theaterElement){
      let brand_obj2str = theaterElement.theaterInfo.brand + "";

      if(_brand) { // 브랜드
        if(_theaterName) { // 지점 명
          if(theaterElement.theaterInfo.theaterName.includes(theaterName) && 
          brand_obj2str.includes(brand)) {
            result.theater.push(theaterElement);
          }
        }
        else {
          if(brand_obj2str.includes(brand)){
            result.theater.push(theaterElement);
          }
        }
      }
      else {
        if(theaterElement.theaterInfo.theaterName.includes(theaterName)) {
          result.theater.push(theaterElement);
        }
      }

    })
  } else {  // 부정어가 들어오면, 제외
    if(!exceptExpression){
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        let brand_obj2str = theaterElement.theaterInfo.brand + "";

        if(_brand) { // 브랜드
          if(_theaterName) { // 지점 명
            if(theaterElement.theaterInfo.theaterName.includes(theaterName) && 
            brand_obj2str.includes(brand)) {
              result.theater.push(theaterElement);
            }
          }
          else {
            if(brand_obj2str.includes(brand)){
              result.theater.push(theaterElement);
            }
          }
        }
        else {
          if(theaterElement.theaterInfo.theaterName.includes(theaterName)) {
            result.theater.push(theaterElement);
          }
        }

      })
    } else {
      theaterOrderedSchedule.theater.forEach(function(theaterElement){
        let brand_obj2str = theaterElement.theaterInfo.brand + "";

        if(_brand) {
          if(_theaterName) {
            if(!(theaterElement.theaterInfo.theaterName.includes(theaterName) && 
            brand_obj2str.includes(brand))) {
              result.theater.push(theaterElement);
            }
          }
          else {
            if(!brand_obj2str.includes(brand)){
              result.theater.push(theaterElement);
            }
          }
        }
        else {
          if(!theaterElement.theaterInfo.theaterName.includes(theaterName)) {
            result.theater.push(theaterElement);
          }
        }

      })
    }
  }

  console.log(result);
  return result;
}
