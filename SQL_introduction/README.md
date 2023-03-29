<h1>SQL - Introduction</h1>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="What is Database &amp; SQL?" href="https://intranet.hbtn.io/rltoken/jRAhwW4u4YvZtLtMGU2_6g" target="_blank" rel="noopener">What is Database &amp; SQL?</a></li>
<li><a title="Install MySQL (MySQL Server)" href="https://intranet.hbtn.io/rltoken/s3m_emsaSthyY041Wacgxg" target="_blank" rel="noopener">Install MySQL (MySQL Server)</a></li>
<li><a title="A Basic MySQL Tutorial" href="https://intranet.hbtn.io/rltoken/m_0RMf4RcC5NrHyjY1xN3w" target="_blank" rel="noopener">A Basic MySQL Tutorial</a></li>
<li><a title="Basic SQL statements: DDL and DML" href="https://intranet.hbtn.io/rltoken/-Qrnbp5eKmo7ajPDZekjfg" target="_blank" rel="noopener">Basic SQL statements: DDL and DML</a> (<em>no need to read the chapter &ldquo;Privileges&rdquo;</em>)</li>
<li><a title="Basic queries: SQL and RA" href="https://intranet.hbtn.io/rltoken/wXN5s1qexSTMh--NkTF1_w" target="_blank" rel="noopener">Basic queries: SQL and RA</a></li>
<li><a title="SQL technique: functions" href="https://intranet.hbtn.io/rltoken/7khGjnehvjHnqNZ9yizggg" target="_blank" rel="noopener">SQL technique: functions</a></li>
<li><a title="SQL technique: subqueries" href="https://intranet.hbtn.io/rltoken/xnJcopQTZyUke3LdAkOwow" target="_blank" rel="noopener">SQL technique: subqueries</a></li>
<li><a title="What makes the big difference between a backtick and an apostrophe?" href="https://intranet.hbtn.io/rltoken/QEr3XcBPhIR-E8NSSn1nzg" target="_blank" rel="noopener">What makes the big difference between a backtick and an apostrophe?</a></li>
<li><a title="MySQL Cheat Sheet" href="https://intranet.hbtn.io/rltoken/DGejihlnOkkNq-qJFM15MA" target="_blank" rel="noopener">MySQL Cheat Sheet</a></li>
<li><a title="MySQL 8.0 SQL Statement Syntax" href="https://intranet.hbtn.io/rltoken/ePNUeloWxfiXwec7HeKe7Q" target="_blank" rel="noopener">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/6bUOgrGi5Yd_I65Jp9bAfg" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What&rsquo;s a database</li>
<li>What&rsquo;s a relational database</li>
<li>What does SQL stand for</li>
<li>What&rsquo;s MySQL</li>
<li>How to create a database in MySQL</li>
<li>What does <code>DDL</code> and <code>DML</code> stand for</li>
<li>How to <code>CREATE</code> or <code>ALTER</code> a table</li>
<li>How to <code>SELECT</code> data from a table</li>
<li>How to <code>INSERT</code>, <code>UPDATE</code> or <code>DELETE</code> data</li>
<li>What are <code>subqueries</code></li>
<li>How to use MySQL functions</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be executed on Ubuntu 20.04 LTS using <code>MySQL 8.0</code> (version 8.0.25)</li>
<li>All your files should end with a new line</li>
<li>All your SQL queries should have a comment just before (i.e. syntax above)</li>
<li>All your files should start by a comment describing the task</li>
<li>All SQL keywords should be in uppercase (<code>SELECT</code>, <code>WHERE</code>&hellip;)</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>The length of your files will be tested using <code>wc</code></li>
</ul>
<h2>More Info</h2>
<h3>Comments for your SQL file:</h3>
<pre><code>$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
</code></pre>
<h3>Install MySQL 8.0 on Ubuntu 20.04 LTS</h3>
<pre><code>$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
</code></pre>
<p>Connect to your MySQL server:</p>
<pre><code>$ sudo mysql
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)
Copyright (c) 2000, 2021, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
mysql&gt;
mysql&gt; quit
Bye
$
</code></pre>
<h3>Use the sandbox to run MySQL</h3>
<p><strong>In the container, credentials are <code>root/root</code></strong></p>
<ul>
<li>Ask for container <code>Ubuntu 20.04</code></li>
<li>Connect via SSH</li>
<li>OR connect via the Web terminal</li>
<li>In the container, you should start MySQL before playing with it:</li>
</ul>
<pre><code>$ service mysql start
 * Starting MySQL database server mysqld
$
$ cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
$
</code></pre>
<p><strong>In the container, credentials are <code>root/root</code></strong></p>