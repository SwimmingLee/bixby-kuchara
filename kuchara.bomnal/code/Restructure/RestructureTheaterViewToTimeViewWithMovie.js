module.exports.function = function restructureTheaterViewToTimeViewWithMovie (theaterOrderedScheduleWithMovie) {

  theaterOrderedScheduleWithMovie.movieOrderedSchedule.sort(function(a, b){
    let time = a.theaterSchedule.startTime.split(":");
    let aTime = time[0]*60 + time[1]*1;
    time = b.theaterSchedule.startTime.split(":");
    let bTime = time[0]*60 + time[1]*1;
    return aTime-bTime;
  })


  return theaterOrderedScheduleWithMovie;
}
