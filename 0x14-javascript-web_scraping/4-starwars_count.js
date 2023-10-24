#!/usr/bin/node

const request = require('request');
let count = 0;
id = "https://swapi-api.alx-tools.com/api/people/18/"
request(process.argv[2], function (_error, _response, body) {
	b = JSON.parse(body).results;
	for (let i = 0; i < b.lenght; i++) {
		for (let j = 0; j < b[i].characters.lenght; j++) {
			if (body[i].characters[j] === id) {
				count++;
			}
		}
	}
  console.log(count);
});
