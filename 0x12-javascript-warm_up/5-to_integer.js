#!/usr/bin/node

if (typeof process.argv[2] === 'string' && !isNaN(process.argv[2])) {
  console.log('My number:', Math.trunc(parseFloat(process.argv[2])));
} else {
  console.log('Not a number');
}
