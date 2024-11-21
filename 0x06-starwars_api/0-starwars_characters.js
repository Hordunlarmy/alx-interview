#!/usr/bin/node

const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  const filmId = process.argv[2];
  const filmURL = `${API_URL}/films/${filmId}/`;

  request(filmURL, (err, _, body) => {
    if (err) {
      console.error(err);
      return;
    }

    const charactersURLs = JSON.parse(body).characters;
    const characterPromises = charactersURLs.map(
      (url) =>
        new Promise((resolve, reject) => {
          request(url, (charErr, __, charBody) => {
            if (charErr) {
              reject(charErr);
            } else {
              resolve(JSON.parse(charBody).name);
            }
          });
        }),
    );

    Promise.all(characterPromises)
      .then((names) => console.log(names.join('\n')))
      .catch((error) => console.error(error));
  });
}
