module.exports.function = function makeNamedPointStructure (locationalKeyword) {

  // 키워드로 posx, y 넣은 namedPoint객체 만들어서 반환
  let obj = {
    'name': locationalKeyword,
    'point': {
      latitude: 35.1232342,
      longitude: 123.2323824,
    }
  }
  return obj;
}
