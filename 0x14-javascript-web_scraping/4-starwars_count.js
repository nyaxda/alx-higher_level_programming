#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const film = data.results.filter(film => film.characters.some(character => character.endsWith('/18/')));
    console.log(film.length);
  } else {
    console.log('code:', response.statusCode);
  }
});
