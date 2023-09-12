#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
let d = -1;
const initiallist = list.map(function (s) {
  d++;
  return s * d;
});
console.log(initiallist);
