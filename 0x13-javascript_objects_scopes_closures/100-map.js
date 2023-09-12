#!/usr/bin/node
const list = require('./100-data');
console.log(list);
let d = -1;
console.log(list.map(function (s) {
  d++;
  return s * d;
}));
