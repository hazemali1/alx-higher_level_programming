#!/usr/bin/node

const request = require('request');
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2]
request(url, function (_error, _response, body) {
  console.log(JSON.parse(body).title);
});
