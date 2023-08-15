#!/usr/bin/node

const x = Math.trunc(parseFloat(process.argv[2]));

if (typeof x === 'string' || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < x; i++) {
  console.log('C is fun');
}
