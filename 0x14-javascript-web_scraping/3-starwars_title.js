#!/usr/bin/node

const request = require('request');

const episode = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('code:', response.statusCode);
  }
});
