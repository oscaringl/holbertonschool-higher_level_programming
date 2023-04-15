<h1>Python - Object-relational mapping</h1>
<h2>Before you start&hellip;</h2>
<p><strong>Please make sure your MySQL server is in 8.0</strong> -&gt; <a title="How to install MySQL 8.0 in Ubuntu 20.04" href="https://intranet.hbtn.io/rltoken/XGGI_GSNhqZU7q_GlvDkCQ" target="_blank" rel="noopener">How to install MySQL 8.0 in Ubuntu 20.04</a></p>
<h2>Background Context</h2>
<p>In this project, you will link two amazing worlds: Databases and Python!</p>
<p>In the first part, you will use the module <code>MySQLdb</code> to connect to a MySQL database and execute your SQL queries.</p>
<p>In the second part, you will use the module <code>SQLAlchemy</code> (don&rsquo;t ask me how to pronounce it&hellip;) an Object Relational Mapper (ORM).</p>
<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be &ldquo;What can I do with my objects&rdquo; and not &ldquo;How this object is stored? where? when?&rdquo;. You won&rsquo;t write any SQL queries only Python code. Last thing, your code won&rsquo;t be &ldquo;storage type&rdquo; dependent. You will be able to change your storage easily without re-writing your entire project.</p>
<p>Without ORM:</p>
<pre><code>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
 print(row)
cur.close()
conn.close()
</code></pre>
<p>With an ORM:</p>
<pre><code>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)
session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
 print("{}: {}".format(state.id, state.name))
session.close()
</code></pre>
<p>Do you see the difference? Cool, right?</p>
<p>The biggest difficulty with ORM is: The syntax!</p>
<p>Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don&rsquo;t read the entire documentation before starting, just jump on it if you don&rsquo;t get something.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Object-relational mappers" href="https://intranet.hbtn.io/rltoken/tCytNeWUzuWhAn9APwtp9A" target="_blank" rel="noopener">Object-relational mappers</a></li>
<li><a title="mysqlclient/MySQLdb documentation" href="https://intranet.hbtn.io/rltoken/V8KJv3QCReECPZ0V-kXRwg" target="_blank" rel="noopener">mysqlclient/MySQLdb documentation</a> (<em>please don&rsquo;t pay attention to <code>_mysql</code></em>)</li>
<li><a title="MySQLdb tutorial" href="https://intranet.hbtn.io/rltoken/j_7jU3C9Jsa0o53pgfwxOQ" target="_blank" rel="noopener">MySQLdb tutorial</a></li>
<li><a title="SQLAlchemy tutorial" href="https://intranet.hbtn.io/rltoken/7y1s8FDE_0S-uhBtCgt5-A" target="_blank" rel="noopener">SQLAlchemy tutorial</a></li>
<li><a title="SQLAlchemy" href="https://intranet.hbtn.io/rltoken/j6kxlUETdjiFwiu0k_JI6Q" target="_blank" rel="noopener">SQLAlchemy</a></li>
<li><a title="mysqlclient/MySQLdb" href="https://intranet.hbtn.io/rltoken/vzsiR8tCdY3_OWsMH33jUA" target="_blank" rel="noopener">mysqlclient/MySQLdb</a></li>
<li><a title="Introduction to SQLAlchemy" href="https://intranet.hbtn.io/rltoken/7m6F57mBASM7A2r_GcIeMA" target="_blank" rel="noopener">Introduction to SQLAlchemy</a></li>
<li><a title="Flask SQLAlchemy" href="https://intranet.hbtn.io/rltoken/riV6WcWo1MGRpF3WSmv4Zw" target="_blank" rel="noopener">Flask SQLAlchemy</a></li>
<li><a title="10 common stumbling blocks for SQLAlchemy newbies" href="https://intranet.hbtn.io/rltoken/uRrjdEkHmjrVenCqjwJRWQ" target="_blank" rel="noopener">10 common stumbling blocks for SQLAlchemy newbies</a></li>
<li><a title="Python SQLAlchemy Cheatsheet" href="https://intranet.hbtn.io/rltoken/RfLwdV21O_TVoQU4iwaIFw" target="_blank" rel="noopener">Python SQLAlchemy Cheatsheet</a></li>
<li><a title="SQLAlchemy ORM Tutorial for Python Developers" href="https://intranet.hbtn.io/rltoken/2BoGpuT2vAaoeuC3SN_wPA" target="_blank" rel="noopener">SQLAlchemy ORM Tutorial for Python Developers</a> (<em><strong>Warning:</strong> This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL</em>)</li>
<li><a title="SQLAlchemy Tutorial" href="https://intranet.hbtn.io/rltoken/DrwY56jSHCOADKEbSOBa0A" target="_blank" rel="noopener">SQLAlchemy Tutorial</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/zAH3PxVw_N-4dQ45aCW8yw" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to <code>SELECT</code> rows in a MySQL table from a Python script</li>
<li>How to <code>INSERT</code> rows in a MySQL table from a Python script</li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8.5)</li>
<li>Your files will be executed with <code>MySQLdb</code> version <code>2.0.x</code></li>
<li>Your files will be executed with <code>SQLAlchemy</code> version <code>1.4.x</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
<li>You are not allowed to use <code>execute</code> with sqlalchemy</li>
</ul>
<h2>More Info</h2>
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
<h3>Install <code>MySQLdb</code> module version <code>2.0.x</code></h3>
<p>For installing <code>MySQLdb</code>, you need to have <code>MySQL</code> installed.</p>
<pre><code>$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
&gt;&gt;&gt; import MySQLdb
&gt;&gt;&gt; MySQLdb.version_info
(2, 0, 3, 'final', 0)
</code></pre>
<h3>Install <code>SQLAlchemy</code> module version <code>1.4.x</code></h3>
<pre><code>$ sudo pip3 install SQLAlchemy
...
$ python3
&gt;&gt;&gt; import sqlalchemy
&gt;&gt;&gt; sqlalchemy.__version__
'1.4.22'
</code></pre>
<p>Also, you can have this warning message:</p>
<pre><code>/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")
 cursor.execute(statement, parameters)
</code></pre>
<p>You can ignore it.</p>
