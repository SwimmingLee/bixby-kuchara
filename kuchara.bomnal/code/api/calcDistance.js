module.exports.function = function calcDistance (latsrc, longsrc, latdst, longdst) {
  let latDistance = latsrc - latdst;
  let longDistance = longsrc - longdst;

  if(latDistance < 0){
    latDistance = latDistance * (-1);
  }
  if(longDistance < 0){
    longDistance = longDistance * (-1);
  }
  
  let longmin = Math.floor(longDistance*100);
  let longsec = Math.floor(longDistance*10000) - longmin*100;

  let px = longmin*1.48 + longsec*0.025;

  let latmin = Math.floor(latDistance*100);
  let latsec = Math.floor(latDistance*10000) - latmin*100;

  let py = latmin*1.85 + latsec*0.031;

  console.log(latDistance);
  console.log(longDistance);
  console.log(px);
  console.log(py);
  let distance = Math.sqrt(px*px + py*py);
  distance = Math.floor(distance*1000);
  console.log(distance);
  return distance;  //미터단위
}
