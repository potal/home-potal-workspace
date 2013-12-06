#coding=utf-8
'''
Created on Nov 28, 2013

@author: mmiku
'''
import unittest
import mikuktv
import time

class TestCase1(unittest.TestCase):

    '''测试登陆、发言、送礼'''
    def test_myTest1(self):      
        user1 = mikuktv.mikuktv()
        user2 = mikuktv.mikuktv()
        user1.ConnectToServer("192.168.1.155",8105)
        user2.ConnectToServer("192.168.1.155",8105)
        #tes.ConnectToServer("112.124.35.41",9010)

        '''
        EnterRoom：进房间
        result： 结果,取值：True、Fasle
        miResult：登录房间的结果,取值1成功，其他表示失败 
        '''
        (result,miResult) = user1.EnterRoom(90019,"sean999999","sean_python")
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)

        (result,miResult) = user2.EnterRoom(8880101,"353432","8880101")
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)

        '''
        SendMsg：发言函数
        result： 结果,取值：True、Fasle
        miResult：登录房间的结果,取值1成功，其他表示失败
        miUserID：发言者的ID
        miDstUserID：接收者的ID
        miPirvate：是否是悄悄话
        mszTest:发言的内容
        '''
        (result,miReuslt,miUserID,miDstUserID,miPirvate,mszText) = user1.SendMsg(8880101,"<FONT>/HX/ hello /FN/，/KL/test msg.</FONT>")
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)
        if(90019 != miUserID):
            self.assertTrue(False)
        if(8880101 != miDstUserID):
            self.assertTrue(False)
        if(0 != miPirvate):
            self.assertTrue(False)
        if(0 != cmp(mszText,"<FONT>/HX/ hello /FN/，/KL/test msg.</FONT>")):
            self.assertTrue(False)
        
        '''
        RecvMsg：接收发言函数
        result： 结果,取值：True、Fasle
        miResult：登录房间的结果,取值1成功，其他表示失败
        miUserID：发言者的ID
        miDstUserID：接收者的ID
        miPirvate：是否是悄悄话
        mszTest:发言的内容
        '''
        (result,miReuslt,miUserID,miDstUserID,miPirvate,mszText) = user2.RecvMsg(0,0,"")
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)
        if(90019 != miUserID):
            self.assertTrue(False)
        if(8880101 != miDstUserID):
            self.assertTrue(False)
        if(0 != miPirvate):
            self.assertTrue(False)
        if(0 != cmp(mszText,"<FONT>/HX/ hello /FN/，/KL/test msg.</FONT>")):
            self.assertTrue(False)

        '''清除消息列表列表'''
        user2.ClearMsgList()
        
        '''
        SendGift:送礼函数
        result： 结果,取值：True、Fasle
        miResult：登录房间的结果,取值1成功，其他表示失败
        miUserID：送礼者的ID
        miDstUserID：接收者的ID
        miCount：礼物的个数
        mszGiftID:礼物的ID
        '''
        (result,miReuslt,miUserID,miDstUserID,miCount,mszGiftID) = user1.SendGift(8880101,"2",1)
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)
        if(90019 != miUserID):
            self.assertTrue(False)
        if(8880101 != miDstUserID):
            self.assertTrue(False)
        if(1 != miCount):
            self.assertTrue(False)
        if(0 != cmp(mszGiftID,"2")):
            self.assertTrue(False)


        '''
        RecvGift:收礼函数
        result： 结果,取值：True、Fasle
        miResult：登录房间的结果,取值1成功，其他表示失败
        miUserID：送礼者的ID
        miDstUserID：接收者的ID
        miCount：礼物的个数
        mszGiftID:礼物的ID
        '''
        (result,miReuslt,miUserID,miDstUserID,miCount,mszGiftID) = user2.RecvGift(0,0,"")
        if not(result):
            self.assertTrue(False)
        if(1 != miResult):
            self.assertTrue(False)
        if(90019 != miUserID):
            self.assertTrue(False)
        if(8880101 != miDstUserID):
            self.assertTrue(False)
        if(1 != miCount):
            self.assertTrue(False)
        if(0 != cmp(mszGiftID,"2")):
            self.assertTrue(False)
        
        '''
        ret_result： 0失败,1进入麦序,2成功上麦
        user_id： 排麦的用户
        mic_type： 当ret_result=1时，为麦序类型，当=2时为上麦用户
        mic_index： 排麦的序号
        '''
        (ret_result,user_id,mic_type,mic_index) = user1.UserApplyPublicMic(1);
        print ret_result,user_id,mic_type,mic_index;

        time.sleep(2);
        (ret_result1,user_id1,mic_type1,mic_index1) = user2.UserApplyPublicMic(1);
        print ret_result1,user_id1,mic_type1,mic_index1;

        user1.UserStopSpeak();
        time.sleep(1);
        user2.UserStopSpeak();
        
        user1.UserPutPublicMic(user2.mi64UserId,1);
        print("Success")
        self.assertTrue(True)
        
        '''
        Close:退出房间函数
        '''
        time.sleep(30);
        
        user1.Close()
        user2.Close()
        
if __name__ == '__main__':
    unittest.main()
    
