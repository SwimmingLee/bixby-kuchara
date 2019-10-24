const movieReturn = require('sample/newStructure.js');
let console = require('console');
let http = require('http');
let config = require('config');

module.exports.function = function findMovieWithMovieAndPos (movieInput, namedPointStructure) {
  let targetPosition = namedPointStructure;
  let long = targetPosition.point.longitude;
  let lat = targetPosition.point.latitutde;

  let options = { 
    format: 'json',
    query: { 
      longitude: long,
      latitude: lat,
    }
  };

  // let response = http.getUrl(config.get('remote.url') + '/searchWithPos', options); 
  // response.theater.forEach(function(theaterElement){
  //   if(theaterElement.theaterInfo.brand == 'cgv'){
  //     theaterElement.theaterInfo.iconUri = "/images/brand/theater/1x/cgv.png"
  //   } else if(theaterElement.theaterInfo.brand == 'megabox'){
  //     theaterElement.theaterInfo.iconUri = "/images/brand/theater/1x/lottecinema.png"
  //   } else {
  //     theaterElement.theaterInfo.iconUri = "/images/brand/theater/1x/megabox.png"
  //   }
  // })
  // console.log(response);

  return movieReturn;
}
