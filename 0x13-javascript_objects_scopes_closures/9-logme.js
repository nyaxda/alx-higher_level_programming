#!/usr/bin/node
/**
 * function that prints the number of arguments and the new argument value.
 */
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
