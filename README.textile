h2. leveldb-server

* Async leveldb server and client based on zeromq
* Storage engine *"leveldb":http://code.google.com/p/leveldb/*
* Networking library *"zeromq":http://www.zeromq.org/*
* We use leveldb-server at *"Safebox":http://safebox.fabulasolutions.com/* 

h3. License

New BSD license. Please see license.txt for more details.

h2. Features

* Very simple key-value storage
* Data is sorted by key - allows @range@ queries
* Data is automatically compressed 
* Can act as persistent cache
* For our use at *"Safebox":http://safebox.fabulasolutions.com/* it replaced memcached+mysql
* Simple backups @cp -rf level.db backup.db@ 
* Networking/wiring from @zeromq@ messaging library - allows many topologies
* Async server for scalability and capacity
* Sync client for easy coding
* Easy polyglot client bindings. See *"zmq bindings":http://www.zeromq.org/bindings:_start*

<pre>
>>> db.put("k3", "v3")
'True'
>>> db.get("k3")
'v3'
>>> db.range()
'[{"k1": "v1"}, {"k2": "v2"}, {"k3": "v3"}]'
>>> db.range("k1", "k2")
'[{"k1": "v1"}, {"k2": "v2"}]'
>>> db.delete('k1')
>>>
</pre>

Will be adding high availability, replication and autosharding using the same zeromq framework. 

h3. Dependencies

<pre>
python 2.6+ (older versions with simplejson)
zmq
pyzmq
leveldb
pyleveldb 
</pre>

h2. Getting Started

Instructions for an EC2 Ubuntu box.

h3. Installing zeromq

<pre>
wget http://download.zeromq.org/zeromq-2.1.10.tar.gz
tar xvfz zeromq-2.1.10.tar.gz
cd zeromq-2.1.10
sudo ./configure
sudo make
sudo make install
</pre>

h3. Installing pyzmq

<pre>
wget https://github.com/zeromq/pyzmq/downloads/pyzmq-2.1.10.tar.gz
tar xvfz pyzmq-2.1.10.tar.gz
cd pyzmq-2.1.10/
sudo python setup.py configure --zmq=/usr/local/lib/
sudo python setup.py install
</pre>

h3. Installing leveldb and pyleveldb

<pre>
svn checkout http://py-leveldb.googlecode.com/svn/trunk/ py-leveldb-read-only
cd py-leveldb-read-only
sudo compile_leveldb.sh
sudo python setup.py install
</pre>

h3. Starting the "leveldb-server":https://github.com/srinikom/leveldb-server/blob/master/leveldb-server.py

<pre>
> python leveldb-server.py -h
Usage: leveldb-server.py 
	-p [port and host settings] Default: tcp://127.0.0.1:5147
	-f [database file name] Default: level.db

leveldb-server

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -p HOST, --host=HOST  
  -d DBFILE, --dbfile=DBFILE
> python leveldb-server.py
</pre>

h3. Using the "leveldb-client-py":https://github.com/srinikom/leveldb-server/blob/master/clients/py/leveldbClient/database.py

<pre>
> cd clients/py/
> sudo python setup.py install
> python 
>>> from leveldbClient import database
>>> db = database.leveldb()
>>> db.get("Key")
>>> db.put("K", "V")
>>> db.range()
>>> db.range(start, end)
>>> db.delete("K")
</pre>

h2. Backups

<pre>
> cp -rpf level.db backup.db
</pre>

h2. Known issues and work in progress

Would love your pull requests on
* Benchmarking and performance analysis
* client libraries for other languages
* [issue] zeromq performance issues with 1M+ inserts at a time
* [feature] timeouts in client library
* [feature] support for counters
* [feature] limit support in range queries
* Serializing and seperate threads for get/put/range in leveldb-server
* HA/replication/autosharding and possibly pub-sub for replication

h2. Thanks

Thanks to all the folks who have contributed to all the dependencies. Special thanks to pyzmq/examples/mongo* author for inspiration. 
