module.exports.function = function makeTheaterStructure (brand, theaterName) {
  
  let theater = {
    "theaterName": theaterName,
    "theaterCode": -1,
    "regionCode": -1,
    "brand": brand,
    "theaterFlag": {
      "namedPointStructure": {
        'name': '',
        'point':{
          "latitude": -1,
          "longitude": -1,
        },
      }, 
    },
  }
  return theater;
}
