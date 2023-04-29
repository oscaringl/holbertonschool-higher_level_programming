/**
 * Toggles class of HTML tag HEADER element must always have one class red and green.
 * DIV#toggle_header
 */

const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('HEADER').toggleClass('red green');
});
