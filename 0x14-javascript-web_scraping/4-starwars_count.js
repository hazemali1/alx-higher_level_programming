#!/usr/bin/node

const request = require('request');
let count = 0;
request(process.argv[2], function (_error, _response, body) {
  const b = JSON.parse(body).results;
  for (let i = 0; i < b.length; i++) {
    for (let j = 0; j < b[i].characters.length; j++) {
			const char = b[i].characters[j].split('/')[5];
      if (char === '18') {
        count++;
      }
    }
  }
  console.log(count);
});
