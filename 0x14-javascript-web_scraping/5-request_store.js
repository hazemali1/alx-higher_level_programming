#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const request = require('request');
request(process.argv[2], function (_error, _response, body) {
  fs.writeFile(process.argv[3], body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
