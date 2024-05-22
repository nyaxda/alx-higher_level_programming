#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(path, body, 'utf8', err => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('code:', response.statusCode);
  }
});
