#!/usr/bin/node
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}

if (process.argv.length === 4) {
  console.log(add(process.argv[2], process.argv[3]));
} else {
  console.log(NaN);
}
