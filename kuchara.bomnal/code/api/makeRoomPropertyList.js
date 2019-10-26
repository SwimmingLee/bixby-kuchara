module.exports.function = function makeRoomPropertyList (roomProperty, room, subtitle) {

  let splited = roomProperty.split(',');
  let list = [];

  let namespace = "images/roomProperty/";
  let cgv = "Rm_Property_Cgv_icon/";
  let mega = "Rm_Property_Mega_icon/"
  let lotte = "Rm_Property_Lotte_icon/"

  splited.forEach(function(el){
    // megabox
    if(el == 'MX'){
      list.push(namespace + mega + "Megabox_MX_2px.png")
    } else if(el == '필름소사이어티') {
      list.push(namespace + mega + "Megabox_FILM_SOCIETY_2px.png")
    } else if(el == '컴포트') {
      
    } else if(el == '더부티크') {
      
    } else if(el == '더부리크S') {
      
    } else if(el == '샤롯데') {
      
    } else if(el == '샤롯데 프라이빗') {
      
    } else if(el == '씨네패밀리') {
      
    } else if(el == '슈퍼플렉스 G') {
      
    } else if(el == '슈퍼 S') {
      
    } else if(el == 'IMAX') {
      
    } else if(el == 'SCREENX') {
      
    } else if(el == 'SOUNDX') {
      
    } else if(el == 'STARIUM') {
      
    } else if(el == 'GOLD CLASS') {
      
    } else if(el == 'CINE de CHEF') {
      
    } else if(el == 'TEMPUR CINEMA') {
      
    } else if(el == 'PREMIUM') {
      
    } else if(el == 'SUBPAC') {
      
    } else if(el == '씨네앤리빙룸') {
      
    } else if(el == 'ART') {
      
    } else if(el == 'SKYBOX') {
      
    } else {
      
    }
  })
  return {}
}


// IMAX
// SCREENX
// SOUNDX
// STARIUM
// SphereX
// GOLD CLASS
// CINE de CHEF
// TEMPUR CINEMA
// PREMIUM
// SUBPAC
// 씨네앤리빙룸
// ART
// SKYBOX
