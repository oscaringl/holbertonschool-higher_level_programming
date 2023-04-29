#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie:
 * The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 */
const request = require('request');
request.get('http://swapi.co/api/films/' + process.argv[2], (err, resp, body) => {
  if (err) console.log(err);
  else if (resp.statusCode === 200) {
    let film = JSON.parse(body);
    let promises = [];
    for (let ch of film.characters) {
      promises.push(new Promise((resolve, reject) => {
        request.get(ch, (err, resp, body) => {
          if (err) {
            reject(err);
          } else if (resp.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(Error('Unknown'));
          }
        });
      }));
    }
    Promise.all(promises).then((names) => names.forEach((name) => console.log(name)));
  }
});
