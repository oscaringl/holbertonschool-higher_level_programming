/* Updates colour of HTML header to (#FF0000) tag DIV#red_header is clicked */

const $ = window.$;
$('DIV#red_header').click(function () {
  $('HEADER').css('color', '#FF0000');
});
