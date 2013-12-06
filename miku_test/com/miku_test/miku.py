#coding=utf-8
'''
Created on Nov 28, 2013

@author: mmiku
'''
import random
import struct
import socket
import threading
import time 
from utils import helper

def mikupack(msg,data,datafmt):
    msg_temp_fmt = ""
    msg_temp = ""
   
    if(0 == cmp("s",datafmt)):
        msg_temp_fmp = "<{0}sH{1}s".format(len(msg),len(data))
        msg_temp = struct.pack(msg_temp_fmp,msg,len(data),data)
    else:
        msg_temp_fmp = "<{0}s{1}".format(len(msg),datafmt)
        msg_temp = struct.pack(msg_temp_fmp,msg,data)

    return msg_temp

class MikuBase(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.msock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.mlRoomId = 0
        self.mi64CUMoney = 0;
        self.mi64Score = 0;
        self.lwPackSerial = random.randint(1,65536)
        self.recvbuf = ""
        self.macPackHeader=struct.pack('<BBB',1,2,3)
        self.macPackTail = struct.pack("<BBB",4,5,6)
        self.lwPackType =5326
        self.thread_running = False
        self.msglist = []
        self.msglock = threading.Lock()
        
    def __del__(self):
        self.Close()
    
    def ConnectToServer(self,serip,servport):
        self.msock.connect((serip,servport))
        self.thread_running = True
        self.start()
        
    def Close(self):
        self.thread_running = False
        self.msock.close()

    def run(self):
        while (self.thread_running):
            self.RecvFun()
            time.sleep(0.001)

    def SendPacket(self,msg_body):
        lbyVersion = 1;
        
        msg_header_body = "";
        msg_header_body = mikupack(msg_header_body,self.lwPackType,"H")
        msg_header_body = mikupack(msg_header_body,self.mlRoomId,"l")
        msg_header_body = mikupack(msg_header_body,msg_body,"s")

        msg = helper().xor_crypt_string(msg_header_body)

        self.lwPackSerial = self.lwPackSerial+1
        lwTailDecryptLen = lwDecryptLen = len(msg)
        packet_fmt = "<3sHBH{0}s3sH".format(lwDecryptLen)
        packet = struct.pack(packet_fmt,self.macPackHeader,lwDecryptLen,lbyVersion,self.lwPackSerial,msg,self.macPackTail,lwTailDecryptLen)

        self.msock.sendall(packet)

    def GetMsg(self,msgtype):
        self.msglock.acquire()
        index = 0
        for element in self.msglist:
            msg_temp = element[0:2]
            data = struct.unpack("<h",msg_temp)
            if(msgtype == data[0]):
                del self.msglist[index]
                self.msglock.release()
                return True,element
            
            index = index + 1
            
        self.msglock.release()
        return False,""

    def Waitfor(self,msgtype,timeout):
        statrttime = time.time()
        while(1):
            if((time.time()-statrttime) > timeout):
                break
            (result,msg) = self.GetMsg(msgtype)
            if(result):
                return result,msg
        return False,""

    def ClearMsgList(self):
        self.msglock.acquire()
        del self.msglist[:]
        self.msglock.release()

    def RecvFun(self):
        buf = self.msock.recv(1024)
        if not(buf):
            return False
#        fmt = "{0}s{1}s".format(len(self.recvbuf),len(buf));
#        self.recvbuf = struct.pack(fmt,self.recvbuf,buf)
        self.recvbuf += buf;
        
        while(len(self.recvbuf) >= 13):
            tempstr = self.recvbuf[0:8];
            (packheader,headdecryptLen) = struct.unpack("<3sH",tempstr[0:5]);
            
            if(len(self.recvbuf) <(headdecryptLen + 13)):
                return;
            
            tempstr = self.recvbuf[0:(headdecryptLen + 13)];
            packet_fmt = "<3sHBH{0}s3sH".format(headdecryptLen);
            (packheader,headdecryptLen,virsion,serial,msg,packtail,taildecryptLen) = struct.unpack(packet_fmt,tempstr)
            if(0 != cmp(packheader,self.macPackHeader)) or (0 != cmp(packtail,self.macPackTail)):
                break;

            self.recvbuf = self.recvbuf[(headdecryptLen + 13):]

            msg = helper().xor_crypt_string(msg)
            tempstr = msg[0:8]
            (packtype,lRoomId,bodylen) = struct.unpack("<HlH",tempstr)

            msg_fmt = "<HlH{0}s".format(bodylen)
            (packtype,lRoomId,bodylen,msg_body) = struct.unpack(msg_fmt,msg)
            (msgtype) = struct.unpack("<H",msg_body[0:2])
            if msgtype == 6024:
                print msgtype,time.time();
            self.msglock.acquire()
            self.msglist.append(msg_body)
            self.msglock.release()
            #self.DealRecvPacket(msgtype,msg_body)


class CSerialize(object):
    def __init__(self,buff,serialize_type):
        self.serialize_type = serialize_type;
        if serialize_type == 1:
            self.buff = '';
        else:
            self.buff = buff;
    
    def SerializeByte(self,value):
        if self.serialize_type == 1: 
            self.buff += struct.pack('<?',value);
            return len(self.buff);
        else:
            data = struct.unpack('<?',self.buff[0:1]);
            self.buff = self.buff[1:];
            return data[0];
        
    def SerializeWord(self,value):
        if self.serialize_type == 1:
            self.buff += struct.pack('<h',value);
            return len(self.buff);
        else:
            data = struct.unpack('<h',self.buff[0:2]);
            self.buff = self.buff[2:];
            return data[0];
      
    def SerializeInteger(self,value):
        if self.serialize_type == 1:
            self.buff += struct.pack('<i',value);
            return len(self.buff);
        else:
            data = struct.unpack('<i',self.buff[0:4]);
            self.buff = self.buff[4:];
            return data[0];
        
    def SerializeLong(self,value):
        if self.serialize_type == 1:
            self.buff += struct.pack('<l',value);
            return len(self.buff);
        else:
            data = struct.unpack('<l',self.buff[0:4]);
            self.buff = self.buff[4:];
            return data[0];
        
    def SerializeLongLong(self,value):
        if self.serialize_type == 1:
            self.buff += struct.pack('<q',value);
            return len(self.buff);
        else:
            data = struct.unpack('<q',self.buff[0:8]);
            self.buff = self.buff[8:];
            return data[0];
    
    def SerializeString(self,value):
        if self.serialize_type == 1:
            length = len(value);
            msg_fmt = '<h{0}s'.format(length);
            self.buff += struct.pack(msg_fmt,length,value);
            return len(self.buff);
        else:
            get_len = struct.unpack('<h',self.buff[0:2]);
            msg_fmt = '<h{0}s'.format(get_len[0]);
            data = struct.unpack(msg_fmt,self.buff[0:2+get_len[0]]);
            self.buff = self.buff[2+get_len[0]:];
            return data[1];

        
