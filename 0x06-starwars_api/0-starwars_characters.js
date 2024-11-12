#!/usr/bin/env node
const request = require('request');

const options = {
  uri: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  json: true
};
request(options, (err, res, body) => {
  if (err) { return console.log(err); }
  const actors = body.characters;
  extractInOrder(actors, 0);
});

const extractInOrder = (actors, key) => {
  if (actors.length === key) {
    return;
  }
  request(actors[key], (err, _, body) => {
    if (err) { return console.log(err); }
    console.log(JSON.parse(body).name);
    extractInOrder(actors, key + 1);
  });
};
