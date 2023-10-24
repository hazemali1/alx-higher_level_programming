#!/usr/bin/node

const fs = require('fs');
fs.readdirSync(argv[1], 'utf-8')
console.log(argv[1]);
