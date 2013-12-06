#coding=utf-8
'''
Created on Nov 25, 2013

@author: mmiku
'''
import struct
import socket

class helper(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def print_hex(self,data):
        ret = ' '.join(x.encode('hex') for x in data)
        print(ret)
        return
    
    def ipstr2int(self,ipstring):
    #     print socket.inet_aton(ipstring)
    #     print(ipstring)
        return struct.unpack("!I",socket.inet_aton(ipstring))[0]

        
    def xor_crypt_string(self,data, key='123456', encode=False, decode=False):
        from itertools import izip, cycle
        import base64
        if decode:
            data = base64.decodestring(data)
        xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
        #     print "",xored
        if encode:
            return base64.encodestring(xored).strip()
        return xored   
    
        