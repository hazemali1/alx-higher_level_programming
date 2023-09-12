#!/usr/bin/node
exports.call = function(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};