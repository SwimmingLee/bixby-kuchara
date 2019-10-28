module.exports.function = function restructureTimeViewToTheaterViewWithMovie (timeOrderedScheduleWithMovie) {

  timeOrderedScheduleWithMovie.movieOrderedSchedule.sort(function(a, b){
    return (a.theaterInfo.theaterName < b.theaterInfo.theaterName);
    // if(a.theaterInfo.theaterName < b.theaterInfo.theaterName){
    //   return -1;
    // } else if(a.theaterInfo.theaterName > b.theaterInfo.theaterName){
    //   return 1;
    // } else {
    //   if(a.theaterSchedule.startTime > b.theaterSchedule.startTime){
    //     return -1;
    //   } else {
    //     return 1;
    //   }
    // }
  })

  let theaterOrderedScheduleWithMovie = {
    movieOrderedSchedule: []
  };

  timeOrderedScheduleWithMovie.movieOrderedSchedule.forEach(function(mosElement) {
    theaterOrderedScheduleWithMovie.movieOrderedSchedule.push(mosElement);
  });
  
  return theaterOrderedScheduleWithMovie;
}
