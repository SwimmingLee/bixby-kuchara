module.exports = function makeRoomPropertyList (roomProperty, dubbing) {
​
  let splited = roomProperty.split(',');
  let list = [];
​
  let namespace = "images/Room_Property_icon/";
  let cgv = "Rm_Property_Cgv_icon/";
  let mega = "Rm_Property_Mega_icon/";
  let lotte = "Rm_Property_Lotte_icon/";
  let general = "Rm_Property_general_icon/";

  if(dubbing){
    list.push(namespace + general + "general_dubbing_2px.png")
  }
​
  splited.forEach(function(el){
    // megabox
    if(el == 'MX'){
      list.push(namespace + mega + "Megabox_MX_2px.png")
    } else if(el == '필름소사이어티') {
      list.push(namespace + mega + "Megabox_FILM_SOCIETY_2px.png")
    } else if(el == '컴포트') {
      list.push(namespace + mega + "Megabox_COMFORT_2px.png")
    } else if(el == '더부티크') {
      list.push(namespace + mega + "Megabox_BOUTIQUE_2px.png")
    } else if(el == '더부티크S') {
      list.push(namespace + mega + "Megabox_BOUTIQUE_S_2px.png")
    } else if(el == '샤롯데') {
      list.push(namespace + lotte + "Lotte_CHARLOTTE_2px.png")
    } else if(el == '샤롯데 프라이빗') {
      list.push(namespace + lotte + "CHARLOTTEP_2px.png")
    } else if(el == '씨네패밀리') {
      list.push(namespace + lotte + "Lotte_CINEFAMILY_2px.png")
    } else if(el == '슈퍼플렉스 G') {
      list.push(namespace + lotte + "Lotte_SUPERPLEXG_2px.png")
    } else if(el == '슈퍼 S') {
      list.push(namespace + lotte + "Lotte_SUPERS_2px.png")
    } else if(el == 'IMAX') {
      list.push(namespace + cgv + "cgv_IMAX_2px.png")
    } else if(el == 'SCREENX') {
      list.push(namespace + cgv + "cgv_SCREENX_2px.png")
    } else if(el == 'SOUNDX') {
      list.push(namespace + cgv + "cgv_SOUNDX_2px.png")
    } else if(el == 'STARIUM') {
      list.push(namespace + cgv + "cgv_STARIUM_2px.png")
    } else if(el == 'GOLD CLASS') {
      list.push(namespace + cgv + "cgv_GOLDCLASS_2px.png")
    } else if(el == 'CINE de CHEF') {
      list.push(namespace + cgv + "cgv_CINEdeCHEF_2px.png")
    } else if(el == 'TEMPUR CINEMA') {
      list.push(namespace + cgv + "cgv_TEMPURCINE_2px.png")
    } else if(el == 'PREMIUM') {
      list.push(namespace + cgv + "cgv_PREMIUM_2px.png")
    } else if(el == 'SUBPAC') {
      list.push(namespace + cgv + "SUBPAC_2px.png")
    } else if(el == '씨네앤리빙룸') {
      list.push(namespace + cgv + "cgv_CINELIVING_2px.png")
    } else if(el == 'ART') {
      list.push(namespace + cgv + "ART_2px.png")
    } else if(el == 'SKYBOX') {
      list.push(namespace + cgv + "cgv_SKYBOX_2px.png")
    } else {
      
    }
  })
  return list;
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
