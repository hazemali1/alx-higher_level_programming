#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
function print (url, index) {
  if (index === url.length) {
    return;
  }
  request(url[index], function (_error2, _response2, body2) {
    console.log(JSON.parse(body2).name);
    print(url, index + 1);
  });
}
request(url, function (_error, _response, body) {
  print(JSON.parse(body).characters, 0);
});
