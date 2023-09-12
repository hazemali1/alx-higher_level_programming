#!/usr/bin/node

const Squar = require('./5-square.js');

class Square extends Squar {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write('r');
        }
      }
      console.log();
    }
  }
}
module.exports = Square;
