#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (_error, _response, body) {
  const myDict = {};
  const b = JSON.parse(body);
  for (let i = 0; i < b.length; i++) {
    if (b[i].completed && !myDict[b[i].userId]) {
      myDict[b[i].userId] = 0;
    }
    if (b[i].completed) {
      myDict[b[i].userId]++;
    }
  }
  console.log(myDict);
});
