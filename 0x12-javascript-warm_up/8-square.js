#!/usr/bin/node

const num = Math.floor(+process.argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    let pattern = '';
    for (let j = 0; j < num; j++) {
      pattern += 'X';
    }
    console.log(pattern);
  }
}
