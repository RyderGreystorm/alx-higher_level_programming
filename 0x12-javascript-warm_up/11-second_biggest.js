#!/usr/bin/node

const arr = process.argv;

if (arr.length < 3 || arr.length === 3) {
  console.log(0);
} else {
  const newArr = arr.slice(2).map(Number);
  const sortedArr = newArr.sort((a, b) => b - a);
  console.log(sortedArr[1]);
}
