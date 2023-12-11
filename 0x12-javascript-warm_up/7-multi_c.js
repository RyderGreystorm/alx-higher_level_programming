#!/usr/bin/node

const arr = process.argv;
if (isNaN(arr[2])) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(arr[2]);
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
