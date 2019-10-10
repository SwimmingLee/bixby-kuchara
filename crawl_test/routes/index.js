var express = require('express');
var router = express.Router();

const request = require('request');
const cheerio = require('cheerio');
const Iconv = require('iconv').Iconv;
const iconv = new Iconv('CP949', 'utf-8//translit//ignore');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/crawlingTest', function(req, res, next) {
  let url = 'http://movie.naver.com/movie/sdb/rank/rmoive.nhn'
  
  request({url, encoding: null}, function(err, response, body) {
    
    let htmlDoc = iconv.convert(body).toString()
    let resultArr = [];
    const $ = cheerio.load(htmlDoc);
    let colArr = $(".tit3")
    for(let i = 0; i < colArr.length; i++) {
      resultArr.push(colArr[i].children[1].attribs.title)
    }
    res.json(resultArr);
	 //console.log(body);
  });
})

module.exports = router;
