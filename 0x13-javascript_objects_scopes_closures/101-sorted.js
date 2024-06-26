#!/usr/bin/node
/**
 * script that imports a dictionary of occurrences by user id and
 * computes a dictionary of user ids by occurrence.
 */
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  if (newDict[dict[key]]) {
    newDict[dict[key]].push(key);
  } else {
    newDict[dict[key]] = [key];
  }
}

console.log(newDict);
