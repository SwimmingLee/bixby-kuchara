module.exports.function = function restructureTimeViewToTheaterViewWithMovie (timeOrderedScheduleWithMovie) {


  timeOrderedScheduleWithMovie.movieOrderedSchedule.sort(function(a, b){
    if(a.theaterInfo.theaterName < b.theaterInfo.theaterName){
      return -1;
    } else if(a.theaterInfo.theaterName > b.theaterInfo.theaterName){
      return 1;
    } else {
      if(a.theaterSchedule.startTime > b.theaterSchedule.startTime){
        return -1;
      } else {
        return 1;
      }
    }
  })

  return timeOrderedScheduleWithMovie;
}
