#!/usr/bin/node

const fs = require('fs');
/* Read File */
fs.readFile(process.argv[2], 'utf8',
  function (error, data) {
  /* If an error exists, show it, otherwise show the file */
    console.log(error || data);
  });
