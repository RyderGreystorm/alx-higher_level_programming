#!/usr/bin/node

const dict = require('./101-data').dict;

const newdic = {};
for (const key in dict) {
  if (newdic[dict[key]] === undefined) {
    newdic[dict[key]] = [];
  }
  newdic[dict[key]].push(key);
}

console.log(newdic);
