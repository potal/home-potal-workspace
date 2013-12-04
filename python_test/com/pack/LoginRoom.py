'''
Created on Nov 28, 2013

@author: potal
'''
import serialize
import baseclass
import hashlib

class LoginRoomRQ(object):

    def __init__(self,client):
        self.client = client;
        
        self.mwTypeID = 6001 
        self.mszVersion = '500'
        self.mlRoomID = 0;
        self.mi64UserId = 0;
        self.mszNickName = '';
        self.mwPhotoNum = 0;
        self.mszPassword= "";
        self.mbySource = 0;
        self.mlUserState = 0;
        self.mszUserPwd = '';
        self.mbyUserLanguage = 0;
        self.mszPhotoUID = "";
        self.mszMacAddr = "";
        self.mszMCode = "";
        self.mszAccountUID ="";
        
    def Pack(self,room_id,user_id,password,nick_name=''):

        self.mlRoomID = room_id;
        self.mi64UserId = user_id;
        self.mszNickName = nick_name;
        self.mszUserPwd = hashlib.md5(password).hexdigest();
    
        pack_data = serialize.CSerialize('',0,1);
        pack_data.SerializeWord(self.mwTypeID);
        pack_data.SerializeString(self.mszVersion);
        pack_data.SerializeLong(self.mlRoomID);
        pack_data.SerializeLongLong(self.mi64UserId);
        pack_data.SerializeString(self.mszNickName);
        pack_data.SerializeWord(self.mwPhotoNum);
        pack_data.SerializeString(self.mszPassword);
        pack_data.SerializeByte(self.mbySource);
        pack_data.SerializeLong(self.mlUserState);
        pack_data.SerializeString(self.mszUserPwd);
        pack_data.SerializeByte(self.mbyUserLanguage);
        pack_data.SerializeString(self.mszPhotoUID);
        pack_data.SerializeString(self.mszMacAddr);
        pack_data.SerializeString(self.mszMCode);
        pack_data.SerializeString(self.mszAccountUID);

        base_class = baseclass.BaseClass();
        
        base_class.Pack(pack_data.buff, len(pack_data.buff));
    
    def LoginRoom(self,room_id,user_id,password,nick_name=''):
        self.Pack(room_id,user_id,password,nick_name);
        
        
class LoginRoomRS():

    def __init__(self,client):
        self.client = client;
        
        self.mwMsgID = 6013;
        self.mbyResult = 0;
        self.mi64UserId = 0;
        self.mlRoomID = 0;
        self.mszErrInfo = '';
        self.mszVoiceIp = '';
        self.musVoicePort = 0;
        self.miUserPopdom = 0;
        self.miRole = 0;
        self.miRoleLevel = 0;
        self.mi64Score = 0;
        self.mi64CUMoney = 0;
        self.miManageType = 0;
        self.mlCityType = 0;
        self.mszSealUID = '';
        self.mszReserved = '';
        self.mlRoomType = '';
        self.mszUserGrade = '';
        self.miCountEffects = 0;
        self.mpUserEffects = 0;
    
    def Unpack(self,buff,buff_len):
        unpacked_data = serialize.CSerialize(buff,buff_len,2);
        
        self.mwMsgID = unpacked_data.SerializeWord(self.mwMsgID);
        self.mbyResult = unpacked_data.SerializeByte(self.mbyResult);
        self.mi64UserId = unpacked_data.SerializeLongLong(self.mi64UserId);
        self.mlRoomID = unpacked_data.SerializeLong(self.mlRoomID);
        self.mszErrInfo = unpacked_data.SerializeString(self.mszErrInfo);
        self.mszVoiceIp = unpacked_data.SerializeString(self.mszVoiceIp);
        self.musVoicePort = unpacked_data.SerializeWord(self.mwMsgID);
        self.miUserPopdom = unpacked_data.SerializeInteger(self.miUserPopdom);
        self.miRole = unpacked_data.SerializeInteger(self.miRole);
        self.miRoleLevel = unpacked_data.SerializeInteger(self.miRoleLevel);
        self.mi64Score = unpacked_data.SerializeLongLong(self.mi64Score);
        self.mi64CUMoney = unpacked_data.SerializeLongLong(self.mi64CUMoney);
        self.miManageType = unpacked_data.SerializeInteger(self.miManageType);
        self.mlCityType = unpacked_data.SerializeLong(self.mlCityType);
        self.mszSealUID = unpacked_data.SerializeString(self.mszSealUID);
        self.mszReserved = unpacked_data.SerializeString(self.mszReserved);
        self.mlRoomType = unpacked_data.SerializeLong(self.mlRoomType);
        self.mszUserGrade = unpacked_data.SerializeString(self.mszUserGrade);
        self.miCountEffects = unpacked_data.SerializeInteger(self.miCountEffects);
#        self.mpUserEffects = unpacked_data.SerializeString(self.mpUserEffects);
    
    def Execute(self,msg_id,buff,buff_len):

        self.Unpack(buff, buff_len);
        
        if self.mi64UserId == self.client.user_id:
            self.client.login_state = self.mbyResult;
            self.client.user_money = self.mi64CUMoney;
            self.client.user_point = self.mi64Score;

    
    
    
    
    
    
    
    
    