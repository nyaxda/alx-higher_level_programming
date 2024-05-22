#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const number = data.filter(person => person.completed === true);
    const dict = {};
    number.forEach(task => {
      if (task.userId in dict) {
        dict[task.userId]++;
      } else {
        dict[task.userId] = 1;
      }
    });
    console.log(dict);
  } else {
    console.log('code:', response.statusCode);
  }
});
