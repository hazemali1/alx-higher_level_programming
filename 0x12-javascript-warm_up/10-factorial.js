#!/usr/bin/node
function factorial(s) {
  return s === 1? 1 : s * factorial(s - 1);
}

let d;
if (process.argv.length === 2) {
  d = factorial(1);
} else {
  d = factorial(process.argv[2]);
}
console.log(d);
