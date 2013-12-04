'''
Created on Nov 28, 2013

@author: potal
'''
import threading

class MyThread(threading.Thread):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        threading.Thread.__init__(self);
        
    def SetSocket(self,sock,client_):
        self.is_running = True;
        self.sock = sock;
        self.client_ = client_;
        
    def run(self):
        while self.is_running:
            buff = self.sock.recv(1024);
            self.client_.DealWithRecvPackage(buff);
            
    def Close(self):
        self.is_running = False;