#!/usr/bin/node
/**
 * Display the status code of GET request.
 */
const request = require('request');

request(process.argv[2], function (error, response) {
  console.log(error || 'code: ' + response.statusCode);
});
