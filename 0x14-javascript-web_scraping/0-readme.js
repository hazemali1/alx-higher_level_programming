#!/usr/bin/node

const process = require('process');
const fs = require('fs');
f = fs.readdirSync(process.argv[1], 'utf-8');
console.log(f);
