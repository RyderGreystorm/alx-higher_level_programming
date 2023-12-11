#!/usr/bin/node

const myNum = +process.argv[2];

if (!isNaN(myNum)) {
  console.log('My number: ' + Math.floor(myNum));
} else {
  console.log('Not a number');
}
