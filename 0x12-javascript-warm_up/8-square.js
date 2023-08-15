#!/usr/bin/node

const x = Math.trunc(parseFloat(process.argv[2]));

if (typeof x === 'string' || isNaN(process.argv[2])) {
  console.log('Missing size');
}

for (let i = 0; i < x; i++) {
  let row = '';
  for (let j = 0; j < x; j++) {
    row += 'x';
  }
  console.log(row);
}