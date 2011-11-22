#!/usr/bin/env python
#Copyright (c) 2011 Fabula Solutions. All rights reserved.
#Use of this source code is governed by a BSD-style license that can be
#found in the license.txt file.

# leveldb client
import zmq
import threading
import time
import json

class leveldb(object):
    """leveldb client"""
    def __init__(self, host="tcp://127.0.0.1:5147", timeout=10*1000):
        self.host = host
        self.timeout = timeout
        self.connect()
    
    def connect(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.XREQ)
        self.socket.connect(self.host)
        
    def get(self, key):
        self.socket.send_multipart(['get', json.dumps(key)])
        return self.socket.recv_multipart()[0]
    
    def put(self, key, value):
        self.socket.send_multipart(['put', json.dumps([key, value])])
        return self.socket.recv_multipart()[0]
    
    def delete(self, key):
        self.socket.send_multipart(['delete',  json.dumps(key)])
        return self.socket.recv_multipart()[0]
    
    def range(self, start=None, end=None):
        self.socket.send_multipart(['range', json.dumps([start, end])])
        return self.socket.recv_multipart()[0]

    def close(self):
        self.socket.close()
        self.context.term()

