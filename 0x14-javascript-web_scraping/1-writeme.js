#!/usr/bin/node

const fs = require('fs');
const PathToWrite = process.argv[2];
const StringToWrite = process.argv[3];

fs.writeFile(PathToWrite, StringToWrite, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
