'''
Created on Nov 28, 2013

@author: potal
'''
#import os
#import time
import socket

class MyConnection(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.s = -1;
    def ConnectServer(self,server_addr,server_port):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        if self.s == -1:
            return False;
        self.s.connect((server_addr,server_port));
        return True;
    
    def SendData(self,send_buff,send_buff_len):
        ret_len = self.s.send(send_buff,send_buff_len);
        if ret_len != send_buff_len:
            print "send error";
            return False;
        print "send ok";
        return True;
    
    def Close(self):
        self.s.close();
    

    
    
        
        