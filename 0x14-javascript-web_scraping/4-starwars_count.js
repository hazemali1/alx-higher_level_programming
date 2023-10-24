#!/usr/bin/node

const request = require('request');
let count = 0;
const id = 'https://swapi-api.alx-tools.com/api/people/18/';
request(process.argv[2], function (_error, _response, body) {
  const b = JSON.parse(body).results;
  for (let i = 0; i < b.length; i++) {
    for (let j = 0; j < b[i].characters.length; j++) {
      if (b[i].characters[j] === id) {
        count++;
      }
    }
  }
  console.log(count);
});
