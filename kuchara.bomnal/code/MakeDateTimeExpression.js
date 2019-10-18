let dates = require('dates');

module.exports.function = function makeDateTimeExpression (timeInput) {

  let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')

  let dateTimeExpressionObj = {
    // 'date': {
    //   'year': zonedDateTime.getYear(),
    //   'month': zonedDateTime.getMonth(),
    //   'day': zonedDateTime.getDay()
    // },
    'dateTime': zonedDateTime.getDateTime(),
  }


  return dateTimeExpressionObj;

}
