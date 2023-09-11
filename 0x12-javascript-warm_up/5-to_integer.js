#!/usr/bin/node
if (typeof(process.argv[2]) === "number") {
	console.log(process.argv[2]);
} else {
	console.log('Not a number');
}
