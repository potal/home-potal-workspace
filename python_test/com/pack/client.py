'''
Created on Nov 28, 2013

@author: potal
'''
import time
import connection
import baseclass
import threading
import mythread
import struct
from utils import helper

import LoginRoom
import ChatMessage
import GiveGift


class Client(object):
    
    def __init__(self,server_addr,server_port):
        self.mutex = threading.Lock();
        self.buff = '';
        self.user_money = 0;
        self.user_point = 0;
        self.is_running = True;
        self.my_connection = connection.MyConnection();
        self.my_connection.ConnectServer(server_addr, server_port);
        self.my_base_class = baseclass.BaseClass();
        self.my_base_class.SetSocket(self.my_connection.s);
        self.recv_thread = mythread.MyThread();
        self.recv_thread.SetSocket(self.my_connection.s,self);
        self.recv_thread.start();
        self.command_dict = {6013:LoginRoom.LoginRoomRS(self),
                             6005:ChatMessage.ChatMessage(self),
                             6045:GiveGift.GiveGiftRS(self)
                             }
        
    def RecvThread(self):
        while(self.is_running):
            buff = self.my_connection.s.recv(1024);
            if len(buff) != 0:
                self.recv_buff += buff;
                
    def Close(self):
        self.is_running = False;
        self.my_connection.Close();
        self.recv_thread.Close();
        
    def AnalyseTcpStoreBuffer(self):
        if len(self.buff) < 8:
            return '',0;
        s = struct.unpack('<3sh?h',self.buff[0:8]);
        msg_fmt = '<3sh?h{0}s3sh'.format(s[1]);
        if len(self.buff) < 13+s[1]:
            return '',0;
        unpacked_data = struct.unpack(msg_fmt,self.buff[0:13+s[1]]);
        buff = unpacked_data[4];
        header = '\x01\x02\x03';
        tail = '\x04\x05\x06';

        if cmp(unpacked_data[0],header) == 0 and cmp(unpacked_data[5],tail) == 0:
            self.buff = self.buff[13+s[1]:];
            return buff,s[1];
        else:
            self.buff = '';
            return '',0;
    
    def DispatchMsg(self,user_data,length):
        if length != len(user_data):
            return False;
        msg_header = struct.unpack('<hlh',user_data[0:8]);

        msg_fmt = '<hlh{0}s'.format(msg_header[2]);
        msg_body = struct.unpack(msg_fmt,user_data);
        if msg_body[0] != 5326:
            return False;
        msg_pack = msg_body[3];
        msg_id = struct.unpack('<h',msg_pack[0:2]);
        
        if self.command_dict.get(msg_id[0]) != None:
#            print self.command_dict[msg_id[0]];
            self.command_dict[msg_id[0]].Execute(msg_id[0],msg_pack,len(msg_pack));
        
        return True;
        
    def DealWithRecvPackage(self,recv_buff):
#        while True:
        if self.mutex.acquire():
            self.buff += recv_buff;
            buff,length = self.AnalyseTcpStoreBuffer();
            if len(buff) == 0:
                self.mutex.release();
                return 0;
            else:
                user_data = helper().xor_crypt_string(buff);
                self.DispatchMsg(user_data,length);
            self.mutex.release();
        return 0;
        
    def LoginRoom(self,room_id,user_id,password,nick_name=''):
        self.room_id = room_id;
        self.user_id = user_id;
        self.my_name = nick_name;
        self.login_state = 0;
        self.user_login = LoginRoom.LoginRoomRQ(self);
        self.user_login.LoginRoom(room_id, user_id, password, nick_name);
        
        count_time = 0;
        while True:
            time.sleep(1);
            if self.login_state == 1:
                
                return 1;
            count_time += 1;
            if count_time == 3:
                break;
        return self.login_state;
                  
    def ChatMessage(self,msg_text,user_talk_to = 0,is_private = False):
        chat_msg = ChatMessage.ChatMessage(self);
        return chat_msg.SendMessage(self.room_id,self.user_id,msg_text,user_talk_to,is_private);
    
    def GiveGift(self,dst_user_id,hero_uid,dst_user_name,gift_msg,gift_uid,gift_count):
        give_gift = GiveGift.GiveGiftRQ(self);
        give_gift.SendGiveGift(dst_user_id,hero_uid,dst_user_name,gift_msg,gift_uid,gift_count);
        

        
        
        