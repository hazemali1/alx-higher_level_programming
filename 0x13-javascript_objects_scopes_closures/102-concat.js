#!/usr/bin/node
const fs = require('fs');
const s = process.argv[2];
const d = process.argv[3];
const q = process.argv[4];
fs.writeFileSync(q, fs.readFileSync(s, 'utf8') + fs.readFileSync(d, 'utf8'));
