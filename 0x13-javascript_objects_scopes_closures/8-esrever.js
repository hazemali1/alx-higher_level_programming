#!/usr/bin/node
exports.esrever = function (list) {
  const s = [];
  for (let i = list.length - 1; i >= 0; i--) {
    s.push(list[i]);
  }
  return s;
};
