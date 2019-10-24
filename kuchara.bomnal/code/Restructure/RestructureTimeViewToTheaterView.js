module.exports.function = function restructureTimeViewToTheaterView (timeOrderedSchedule) {
  
  let theaterOrderedSchedule = {
    'movie':{
      "movieName": timeOrderedSchedule.movie.movieName,
      "duration": timeOrderedSchedule.movie.duration,
      "movieRating": timeOrderedSchedule.movie.movieRating,
      "director": timeOrderedSchedule.movie.director,
      "actors": timeOrderedSchedule.movie.actors,
      "genre": timeOrderedSchedule.movie.genre,
      "imgUrl": timeOrderedSchedule.movie.imgUrl,
      "userRating": timeOrderedSchedule.movie.userRating,
      "nation": timeOrderedSchedule.movie.nation,
    },
    
    'theater': []
  }
  
  timeOrderedSchedule.timeSchedule.forEach(function(timeScheduleElement){
    let newStartTime = timeScheduleElement.startTime;
    let newEndtime = timeScheduleElement.endTime;
    let newTotalSeat = timeScheduleElement.totalSeat;
    let newAvailableSeat = timeScheduleElement.availableSeat;
    let newRoom = timeScheduleElement.room;
    let newSubtitle = timeScheduleElement.subtitle;
    let newDubbing = timeScheduleElement.dubbing;
    let newRoomProperty = timeScheduleElement.roomProperty;

    let newTheaterName = timeScheduleElement.theaterInfo.theaterName;
    let newTheaterCode = timeScheduleElement.theaterInfo.theaterCode;
    let newRegionCode = timeScheduleElement.theaterInfo.regionCode;
    let newBrand = timeScheduleElement.theaterInfo.brand;
    let newLatitude = timeScheduleElement.theaterInfo.latitude;
    let newLongitude = timeScheduleElement.theaterInfo.longitude;

    let theaterInfo = {
      'brand' : newBrand,
      "theaterName": newTheaterName,
      'longitude' : newLongitude,
      'latitude' : newLatitude,
      "theaterCode": newTheaterCode,
      "regionCode": newRegionCode,
      'iconUri': newIconUri,
    }

    let theaterSchedule = {
      'startTime': newStartTime,
      'endTime': newEndtime,
      "totalSeat": newTotalSeat,     // 총 좌석수
      "availableSeat": newAvailableSeat,            // 빈 좌석수
      "subtitle": newSubtitle,               // 자막여부
      "dubbing": newDubbing,
      "room": newRoom,
      "roomProperty": newRoomProperty
    }

    let found = false;
    theaterOrderedSchedule.theater.forEach(function(theaterElement){
      if(theaterInfo.theaterCode == theaterElement.theaterInfo.theaterCode 
            && theaterInfo.regionCode == theaterElement.theaterInfo.regionCode){
        theaterElement.theaterSchedule.push(theaterSchedule);
        found = true;
      }
    })

    if(found){
      theater.push({
        "theaterInfo": theaterInfo,
        "theaterSchedule": [],
      })
      theater.theaterSchedule.push(theaterSchedule);
    }
  })

  
  return theaterOrderedSchedule;
}
