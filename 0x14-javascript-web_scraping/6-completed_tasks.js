#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (_error, _response, body) {
	const my_dict = {};
	const b = JSON.parse(body);
	let count = 0;
	let num = 1;
	for (let i = 0; i < b.length; i++) {
		if (b[i].userId !== num) {
			my_dict[num] = count;
			num = b[i].userId;
		if (b[i].completed) {
			count++;
		}
	}
}
console.log(my_dict);
});
