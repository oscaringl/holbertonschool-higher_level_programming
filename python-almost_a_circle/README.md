<h1>Python - Almost a circle</h1>

<h2>Background Context</h2>
<p>In this project, you will review everything about Python:</p>
<ul>
<li>Import</li>
<li>Exceptions</li>
<li>Class</li>
<li>Private attribute</li>
<li>Getter/Setter</li>
<li>Class method</li>
<li>Static method</li>
<li>Inheritance</li>
<li>Unittest</li>
<li>Read/Write file</li>
</ul>
<p>You will also learn about:</p>
<ul>
<li><code>args</code> and <code>kwargs</code></li>
<li>Serialization/Deserialization</li>
<li>JSON</li>
</ul>
<p><video autoplay="autoplay" loop="loop" width="300" height="150" data-mce-fragment="1"></video></p>
<h2>Step by step</h2>
<ul>
<li>Write the first class Base</li>
<li>Write the class Rectangle that inherits from Base</li>
<li>Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)</li>
<li>Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance</li>
<li>Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don&rsquo;t need to handle x and y here</li>
<li>Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance</li>
<li>Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y</li>
<li>Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute</li>
<li>Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes</li>
<li>Write the class Square that inherits from Rectangle</li>
<li>Update the class Square by adding the public getter and setter size</li>
<li>Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes</li>
<li>Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle</li>
<li>Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square</li>
<li>Update the class Base by adding the class method def save<em>to</em>file(cls, list<em>objs): that writes the JSON string representation of list</em>objs to a file</li>
<li>Update the class Base by adding the static method def from<em>json</em>string(json<em>string): that returns the list of the JSON string representation json</em>string</li>
<li>Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set</li>
<li>Update the class Base by adding the class method def load<em>from</em>file(cls): that returns a list of instances</li>
</ul>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="args/kwargs" href="https://intranet.hbtn.io/rltoken/1VFpovKWOxo91RtP2lebZg" target="_blank" rel="noopener">args/kwargs</a></li>
<li><a title="JSON encoder and decoder" href="https://intranet.hbtn.io/rltoken/DfJsuOTXTv2t7ycPfEXZuw" target="_blank" rel="noopener">JSON encoder and decoder</a></li>
<li><a title="unittest module" href="https://intranet.hbtn.io/rltoken/_jqAzT_nImg88Bk36NHjMw" target="_blank" rel="noopener">unittest module</a></li>
<li><a title="Python test cheatsheet" href="https://intranet.hbtn.io/rltoken/n7aJtd_G82AIQ9hxMg7nng" target="_blank" rel="noopener">Python test cheatsheet</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/H-uthlOO7nk1vorFnZtI7A" target="_blank" rel="noopener">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>