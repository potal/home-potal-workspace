'''
Created on Nov 28, 2013

@author: potal
'''
#!usr/bin/python
import client
import time
if __name__ == '__main__':
    print 'start';
    mk_test_client = client.Client('192.168.1.125',8135);
    login_state = mk_test_client.LoginRoom(15000, 92002, 'sean999999', 'test_92002');
    if login_state != 1:
        print 'Login Failed';
    else:
        time.sleep(3);
        msg_state = mk_test_client.ChatMessage("msg_text", 0, False);
        if msg_state == False:
            print 'Send Message Failed';
        else:
            mk_test_client.GiveGift(550003, '', 'Test_550003', '', '1', 2);

    time.sleep(10);
    mk_test_client.Close();
    time.sleep(2);
    print 'end';