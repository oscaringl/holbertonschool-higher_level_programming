<h1><strong><code></code></strong>SQL - More queries</h1>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="How To Create a New User and Grant Permissions in MySQL" href="https://intranet.hbtn.io/rltoken/1tuxYhEv__bmrwkAicbjpA" target="_blank" rel="noopener">How To Create a New User and Grant Permissions in MySQL</a></li>
<li><a title="How To Use MySQL GRANT Statement To Grant Privileges To a User" href="https://intranet.hbtn.io/rltoken/PMozNP0LI2zJ-ycA-L6xoA" target="_blank" rel="noopener">How To Use MySQL GRANT Statement To Grant Privileges To a User</a></li>
<li><a title="MySQL constraints" href="https://intranet.hbtn.io/rltoken/AHI2a6vFyr8h4LeI6xK96w" target="_blank" rel="noopener">MySQL constraints</a></li>
<li><a title="SQL technique: subqueries" href="https://intranet.hbtn.io/rltoken/UvrRJYwhKKL-WcqdfR4ZTg" target="_blank" rel="noopener">SQL technique: subqueries</a></li>
<li><a title="Basic query operation: the join" href="https://intranet.hbtn.io/rltoken/vZviDvoYzQSi5asDz-ZsqA" target="_blank" rel="noopener">Basic query operation: the join</a></li>
<li><a title="SQL technique: multiple joins and the distinct keyword" href="https://intranet.hbtn.io/rltoken/vjcpTEMrRJUOXIWBdzzlMg" target="_blank" rel="noopener">SQL technique: multiple joins and the distinct keyword</a></li>
<li><a title="SQL technique: join types" href="https://intranet.hbtn.io/rltoken/s0sG5NqFN4nw4-k0KJNBbg" target="_blank" rel="noopener">SQL technique: join types</a></li>
<li><a title="SQL technique: union and minus" href="https://intranet.hbtn.io/rltoken/tv7XqDq1naSlqSz042VBjA" target="_blank" rel="noopener">SQL technique: union and minus</a></li>
<li><a title="MySQL Cheat Sheet" href="https://intranet.hbtn.io/rltoken/g8QlxhHt2_WHdIXE-2oYYw" target="_blank" rel="noopener">MySQL Cheat Sheet</a></li>
<li><a title="The Seven Types of SQL Joins" href="https://intranet.hbtn.io/rltoken/o6faV44f8S34zW3FiO5Mgg" target="_blank" rel="noopener">The Seven Types of SQL Joins</a></li>
<li><a title="MySQL Tutorial" href="https://intranet.hbtn.io/rltoken/T3VjE1yBfwJcd1hDD4tItw" target="_blank" rel="noopener">MySQL Tutorial</a></li>
<li><a title="SQL Style Guide" href="https://intranet.hbtn.io/rltoken/0NaQZjOUvQuWy0xGPhTkVw" target="_blank" rel="noopener">SQL Style Guide</a></li>
<li><a title="MySQL 8.0 SQL Statement Syntax" href="https://intranet.hbtn.io/rltoken/R5KAnzO4iwYo2LgD3eKL8A" target="_blank" rel="noopener">MySQL 8.0 SQL Statement Syntax</a></li>
</ul>
<p>Extra resources around relational database model design:</p>
<ul>
<li><a title="Design" href="https://intranet.hbtn.io/rltoken/A81_Vk2TV-f_f5wG0HK6Zw" target="_blank" rel="noopener">Design</a></li>
<li><a title="Normalization" href="https://intranet.hbtn.io/rltoken/cwgE_DVy7l3ap6lCVJsPZQ" target="_blank" rel="noopener">Normalization</a></li>
<li><a title="ER Modeling" href="https://intranet.hbtn.io/rltoken/1JFNpSloiEAI7aLW2rnyKw" target="_blank" rel="noopener">ER Modeling</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/SXrjP8A_no4j3TMHUC4NBw" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>How to create a new MySQL user</li>
<li>How to manage privileges for a user to a database or table</li>
<li>What&rsquo;s a <code>PRIMARY KEY</code></li>
<li>What&rsquo;s a <code>FOREIGN KEY</code></li>
<li>How to use <code>NOT NULL</code> and <code>UNIQUE</code> constraints</li>
<li>How to retrieve datas from multiple tables in one request</li>
<li>What are subqueries</li>
<li>What are <code>JOIN</code> and <code>UNION</code></li>
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
<h3>How to import a SQL dump</h3>
<pre><code>$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password:
$ curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password:
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password:
id name
1 Drama
2 Mystery
3 Adventure
4 Fantasy
5 Comedy
6 Crime
7 Suspense
8 Thriller
$
</code></pre>
<p><img src="https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230329%2Feu-west-3%2Fs3%2Faws4_request&amp;X-Amz-Date=20230329T184943Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=ccecd31f184ee55a819e69b45e827c167d808dd1bed97fc3646fa2ad74781570" alt="" /></p>