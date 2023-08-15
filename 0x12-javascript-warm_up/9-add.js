#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const t = process.argv[2] ? parseInt(process.argv[2]) : NaN;
const d = process.argv[3] ? parseInt(process.argv[3]) : NaN;

add(t, d);
