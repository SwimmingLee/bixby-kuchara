let dates = require('dates');
let console = require('console');

module.exports.function = function makeDateTimeExpression (dateTimeExpression, detachedTime) {

  let zonedDateTime = new dates.ZonedDateTime('Asia/Seoul')

  let dateTimeExpressionObj = {
    'dateTime': zonedDateTime.getDateTime(),
  }

  console.log(dateTimeExpressionObj);
  console.log(dateTimeExpression);
  console.log(detachedTime);

  if(typeof dateTimeExpression != 'undefined'){
    dateTimeExpressionObj.dateTime.date.year = dateTimeExpression.date.year;
    dateTimeExpressionObj.dateTime.date.month = dateTimeExpression.date.month;
    dateTimeExpressionObj.dateTime.date.day = dateTimeExpression.date.day;
  } 

  // console.log(detachedTime.amPM);
  // console.log(typeof(detachedTime.amPM));
  
  if(typeof detachedTime != 'undefined'){
    let hourin = detachedTime.hour ;
    let minin = detachedTime.minute;

    // 오후 태그가 달려있으면 시간에 12더하기
    if(detachedTime.amPM == 'Pm'){
      hourin = hourin + 12;  
    } else {  // 현재시간이 인풋시간보다 뒷시간이면 시간에 12더하기
      let currenttime = dateTimeExpressionObj.dateTime.time.hour*60 + dateTimeExpressionObj.dateTime.time.minute*1;
      let inputtime = hourin*60 + minin*1
      if(currenttime > inputtime){
        hourin = hourin + 12;
      }
    }

    dateTimeExpressionObj.dateTime.time.hour = hourin;
    dateTimeExpressionObj.dateTime.time.minute = minin;
  }
  console.log(dateTimeExpressionObj);

  return dateTimeExpressionObj;

}
