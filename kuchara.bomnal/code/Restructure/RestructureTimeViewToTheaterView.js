let console = require('console');

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
    let newIconUri = timeScheduleElement.theaterInfo.iconUri;

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
        // console.log("123123");
      }
      // console.log("456456");
    })
    // console.log(theaterInfo);

    if(found == false){
      theaterOrderedSchedule.theater.push({
        "theaterInfo": theaterInfo,
        "theaterSchedule": [],
      })
      
      theaterOrderedSchedule.theater[theaterOrderedSchedule.theater.length-1].theaterSchedule.push(theaterSchedule);
    }
  })

  theaterOrderedSchedule.theater.forEach(function(theaterElement){
    theaterElement.theaterSchedule.sort(function(a, b){
      let time = a.startTime.split(":");
      let aTime = time[0]*60 + time[1]*1;
      time = b.startTime.split(":");
      let bTime = time[0]*60 + time[1]*1;
      return aTime-bTime;
    })
  })

  console.log(theaterOrderedSchedule);
  
  return theaterOrderedSchedule;
}
