<h1>JavaScript - Web scraping</h1>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Working with JSON data" href="https://intranet.hbtn.io/rltoken/MiTgYMkQEYW7Ydfr2Enb-A" target="_blank" rel="noopener">Working with JSON data</a></li>
<li><a title="The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco" href="https://intranet.hbtn.io/rltoken/FaAMZnG2vwWwzlkrYrhC0A" target="_blank" rel="noopener">The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco</a></li>
<li><a title="request module" href="https://intranet.hbtn.io/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ" target="_blank" rel="noopener">request module</a></li>
<li><a title="Modern JS" href="https://intranet.hbtn.io/rltoken/ULF1RX7OyNexRK1q7qpcwA" target="_blank" rel="noopener">Modern JS</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/y1YyQMtdFjC6uqUzoggDkQ" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why JavaScript programming is amazing</li>
<li>How to manipulate JSON data</li>
<li>How to use <code>request</code> and fetch API</li>
<li>How to read and write a file using <code>fs</code> module</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS using <code>node</code> (version 10.14.x)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/node</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should be <code>semistandard</code> compliant. <a title="Rules of Standard" href="https://intranet.hbtn.io/rltoken/Z50ZPNHxGgFadRcaHCXWLQ" target="_blank" rel="noopener">Rules of Standard</a> + <a title="semicolons on top" href="https://intranet.hbtn.io/rltoken/ZDy8VNGPo5AIV8I4YAJ7nA" target="_blank" rel="noopener">semicolons on top</a>. Also as reference: <a title="AirBnB style" href="https://intranet.hbtn.io/rltoken/VC05wFk369ONcZZR8uLtjw" target="_blank" rel="noopener">AirBnB style</a></li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>You are not allowed to use <code>var</code></li>
</ul>
<h2>More Info</h2>
<h3>Install Node 10</h3>
<pre><code>$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
</code></pre>
<h3>Install semi-standard</h3>
<p><a title="Documentation" href="https://intranet.hbtn.io/rltoken/ZDy8VNGPo5AIV8I4YAJ7nA" target="_blank" rel="noopener">Documentation</a></p>
<pre><code>$ sudo npm install semistandard --global
</code></pre>
<h3>Install <code>request</code> module and use it</h3>
<p><a title="Documentation" href="https://intranet.hbtn.io/rltoken/ZOiv4Q-sjWN87QlfMxg2PQ" target="_blank" rel="noopener">Documentation</a></p>
<pre><code>$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
</code></pre>
<p><strong>Notes:</strong> Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it&rsquo;s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).</p>