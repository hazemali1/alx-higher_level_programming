#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (_error, _response, body) {
  const myDict = {};
  const b = JSON.parse(body);
  let count = 0;
  let num = 1;
  for (let i = 0; i < b.length; i++) {
    if (b[i].userId !== num) {
      myDict[num] = count;
      count = 0;
      num = b[i].userId;
    }
    if (b[i].completed) {
      count++;
    }
  }
  myDict[num] = count;
  console.log(myDict);
});
