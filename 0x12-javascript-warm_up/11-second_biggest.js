#!/usr/bin/node
if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const d = [];
  for (let i = 2; i < process.argv.length; i++) {
    d[i] = process.argv[i];
  }
  d.sort((a, b) => b - a);
  console.log(d[1]);
}
