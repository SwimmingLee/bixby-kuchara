let dates = require('dates')
let console = require('console')

module.exports.function = function openBrowser (movieScheduleDetail) {
  let response;
  if (movieScheduleDetail.brand == 'cgv') {
    let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')
    let today = { 'dateTime': zonedDateTime.getDateTime() }

    response = 'http://m.cgv.co.kr/Schedule/?tc=' + movieScheduleDetail.theaterCode + '&t=T&ymd='
       + today.dateTime.date.year + today.dateTime.date.month
        + today.dateTime.date.day + '&src=';
  }
  else if (movieScheduleDetail.brand == 'megabox') {
    response = 'http://megabox.co.kr/?menuId=theater-detail&region='
      + movieScheduleDetail.regionCode + '&cinema=' + movieScheduleDetail.theaterCode;
  }
  else if (movieScheduleDetail.brand == 'lottecinema') {
    response = 'https://www.lottecinema.co.kr/LCMW/Contents/Cinema/cinema-detail.aspx?divisionCode=1&detailDivisionCode='
    + movieScheduleDetail.regionCode + '&cinemaID=' + movieScheduleDetail.theaterCode;
  }

  console.log (response)

  return response;
}
