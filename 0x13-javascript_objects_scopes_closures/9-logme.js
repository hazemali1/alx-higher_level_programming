#!/usr/bin/node
let s = 0;
exports.logMe = function (item) {
  console.log(s + ': ' + item);
  s++;
};
