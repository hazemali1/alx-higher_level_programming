#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (_error, _response, body) {
  for (let i = 0; i < JSON.parse(body).characters.length; i++) {
    request(JSON.parse(body).characters[i], function (_error2, _response2, body2) {
      console.log(JSON.parse(body2).name);
    });
  }
});
