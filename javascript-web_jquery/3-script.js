/* Adds class red to HTML tag HEADER to (#FF0000) when DIV#red_header clicked */

const $ = window.$;
$('DIV#red_header').click(function () {
  $('HEADER').addClass('red');
});
