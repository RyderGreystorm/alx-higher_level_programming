#!/usr/bin/node

function secondBiggest (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  const sortedNumbers = numbers.map(Number).sort((a, b) => b - a);
  return sortedNumbers[1];
}

const args = process.argv.slice(2);
const result = secondBiggest(args);

console.log(result);
