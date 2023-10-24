#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (_error, _response, body) {
  const myDict = {};
  const b = JSON.parse(body);
  let count = 0;
  let num = 1;
  for (let i = 0; i < b.length; i++) {
    if (b[i].userId !== num) {
      myDict[b[i].userId] = 0;
      count = 1;
      num = b[i].userId;
    }
    if (count === 0) {
      myDict[b[i].userId] = 0;
      count = 1;
    }
    if (b[i].completed) {
      myDict[num]++;
    }
  }
  console.log(myDict);
});
