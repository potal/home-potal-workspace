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
        上公麦
        参数：1表示上小麦，2表示上大麦
        
        返回值：
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

        '''
        下麦
        '''
        user1.UserStopSpeak();
        time.sleep(1);
        user2.UserStopSpeak();
        
        '''
        抱公麦
        参数：第一个参数：被抱人ID 第二个参数：被抱麦的类型，1小麦，2大麦
        
        返回值：
        ret_result:抱麦结果，1为成功，非1失败
        manager_id:抱麦人ID 
        user_id:被抱麦人ID
        mic_index:抱麦的序号
        mic_type:麦的类型
        '''
        (ret_result,manager_id,user_id,mic_index,mic_type) = user1.UserPutPublicMic(user2.mi64UserId,1);
        print ret_result,manager_id,user_id,mic_index,mic_type;
        time.sleep(2);
        if ret_result == 1:
            user2.UserStopSpeak();
        
        '''
        抱私麦
        参数返回值与抱公麦一致，不赘述
        '''
        (ret_result,manager_id,user_id,mic_index,mic_type) = user1.UserPutPrivateMic(user2.mi64UserId, 1);
        print ret_result,manager_id,user_id,mic_index,mic_type;
        time.sleep(2);
        
        '''
        如果成功被抱私麦，那么邀请某个人(比如92002)观看私麦
        '''
        if ret_result == 1:
            '''
            邀请观看私麦
            参数：第一参数：被邀请人ID ，第二参数：超时时间
            返回值：
            result:邀请是否成功
            manager_id:邀请人ID
            user_id:被邀请人ID
            '''
            
            (result,manager_id,user_id) = user2.UserInvitePrivateMic(user1.mi64UserId, 120);
            print result,manager_id,user_id;
        
        '''
        是否同意邀请
        参数：第一参数：邀请人ID ，第二参数，1同意，2不同意
        返回值 与上函数相同，不再赘述
        '''
        (result,manager_id,user_id) = user1.UserAgreeInvitePrivateMic(user2.mi64UserId,1);
        print result,manager_id,user_id;
        
        '''
        查看IP
        参数：被查询者的ID
        返回值：被查询者ID，被查询者IP，被查询者地址(为空正确)
        '''
        (dst_user_id,user_ip,user_addr) = user1.UserGetOtherIP(user2.mi64UserId);
        print dst_user_id,user_ip,user_addr;
        
        '''
        踢人
        参数：被踢者ID
        返回值：是否被踢成功：1成功，非1失败  被踢者ID  房间ID
        '''
        (ret_result,dst_user_id,room_id) = user1.UserKickOutRoom(user2.mi64UserId);
        print ret_result,dst_user_id,room_id;
        
        '''
        丢骰子
        返回值:是否成功，游戏者ID，骰子点数
        '''
        (ret_result,user_id,rand_num) = user1.UserPlayDiceGame();
        print ret_result,user_id,rand_num;
        
        '''
        砸金蛋游戏
        返回值：砸蛋结果，剩余金蛋数量，获得的酷币，用户最后的酷币
        '''
        (ret_result,count_eggs,got_money,all_money) = user1.UserSmashGoldEgg();
        print ret_result,count_eggs,got_money,all_money;
        
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
    
