#!/usr/bin/node
const dict = require('./101-data').dict;
const newdict = {};
for (const id in dict) {
  if (dict.id in newdict) {
    newdict[dict.id].push(id);
  } else {
    newdict[dict.id] = [id];
  }
}
console.log(newdict);
