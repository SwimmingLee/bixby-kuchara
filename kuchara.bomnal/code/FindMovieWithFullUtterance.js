let console = require('console');

module.exports.function = function findMovieWithFullUtterance (isStartTime, movieName, timeInput, locationalKeyword, brand) {
  // 경우의 수
  // [moviename, locationalkeyword, timeinput, isstarttime, brand]
  let mode = "";
  if(movieName){
    mode += '1';
  } else {
    mode += '0';
  }
  if(locationalKeyword){
    mode += '1';
  } else {
    mode += '0';
  }
  if(timeInput){
    mode += '1';
  } else {
    mode += '0';
  }
  if(isStartTime){    // false일 경우 생각해보기
    mode += '1';
  } else {
    mode += '0';
  }
  if(brand){
    mode += '1';
  } else {
    mode += '0';
  }

  console.log(mode);

  
  return {}
}
