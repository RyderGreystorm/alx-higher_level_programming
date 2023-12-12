#!/usr/bin/node

const arr = process.argv;

function add (a, b) {
  return a + b;
}

const result = add(Math.floor(+arr[2]), Math.floor(+arr[3]));
console.log(result);
