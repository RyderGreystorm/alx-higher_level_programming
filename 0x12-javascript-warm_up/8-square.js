#!/usr/bin/node

const x = Math.trunc(parseFloat(process.argv[2]));

if (typeof x === 'string' || isNaN(process.argv[2])) {
  console.log('Missing size');
}
if (x > 0) {
  for (let i = 0; i < x; i++) {
    let row = '';
    for (let j = 0; j < x; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
