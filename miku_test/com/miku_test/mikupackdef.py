#coding=utf-8
'''
Created on Nov 28, 2013

@author: mmiku
'''


import miku
from utils import helper

class STRU_CL_CRS_LOGIN_ROOM_RQ:
    def __init__(self):
        self.mwTypeID = 6001             #WORD package type DEF_CRS_PACK_BASE+1
        self.macVersion = ""             # VERSION_LEN 10+1
        self.mlRoomID = 0
        self.mi64UserId = 0              #bigint
        self.macNickName = ""            #NICK_NAME_LEN + 1 20+1
        self.mwPhotoNum = 0
        self.macPassword= ""             #UC_HALL_PWD_LEN + 1 128+1
        self.mbySource = 0
        self.mlUserState = 0
        self.macUserPwd = ""      
        self.mbyUserLanguage = 0
        self.mszPhotoUID = ""
        self.mszMacAddr = ""
        self.mszMCode = ""
        self.mszAccountUID =""

    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwTypeID)
        pack_data.SerializeString(self.macVersion)
        pack_data.SerializeLong(self.mlRoomID)
        pack_data.SerializeLongLong(self.mi64UserId)
        pack_data.SerializeString(self.macNickName)
        pack_data.SerializeWord(self.mwPhotoNum)
        pack_data.SerializeString(self.macPassword)
        pack_data.SerializeByte(self.mbySource)
        pack_data.SerializeLong(self.mlUserState)
        pack_data.SerializeString(self.macUserPwd)
        pack_data.SerializeByte(self.mbyUserLanguage)
        pack_data.SerializeString(self.mszPhotoUID)
        pack_data.SerializeString(self.mszMacAddr)
        pack_data.SerializeString(self.mszMCode)
        pack_data.SerializeString(self.mszAccountUID)
        return pack_data.buff

class STRU_CL_CRS_LOGIN_ROOM_RS_LE:
    def __init__(self):
        self.mwTypeID = 6013
        self.mbyResult  = 0
        self.mi64UserId = 0;
        self.mlRoomID = 0;
        self.macErrInfo = ""
        self.mszVoiceIp = ""
        self.musVoicePort = ""
        self.miUserPopdom = 0;
        self.miRole = 0
        self.miRoleLevel = 0
        self.mi64Score = 0
        self.mi64CUMoney = 0
        self.miManageType = 0
        self.mlCityType = 0
        self.mszSealUID = ""
        self.macReserved = ""
        self.mlRoomType = 0
        self.mszUserGrade = ""
        self.miCountEffects = 0

    def UnPack(self,msg_body):
        unpack_data = miku.CSerialize(msg_body,2);
        self.mwTypeID = unpack_data.SerializeWord("");
        self.mbyResult = unpack_data.SerializeByte("");
        self.mi64UserId = unpack_data.SerializeLongLong("");
        self.mlRoomID = unpack_data.SerializeLong("");
        self.macErrInfo = unpack_data.SerializeString("");
        self.mszVoiceIp = unpack_data.SerializeString("");
        self.musVoicePort = unpack_data.SerializeWord("");
        self.miUserPopdom = unpack_data.SerializeInteger("");
        self.miRole = unpack_data.SerializeInteger("");
        self.miRoleLevel = unpack_data.SerializeInteger("");
        self.mi64Score = unpack_data.SerializeLongLong("");
        self.mi64CUMoney = unpack_data.SerializeLongLong("");
        self.miManageType = unpack_data.SerializeInteger("");
        self.mlCityType = unpack_data.SerializeLong("");
        self.mszSealUID = unpack_data.SerializeString("");
        self.macReserved = unpack_data.SerializeString("");
        self.mlRoomType = unpack_data.SerializeLong("");
        self.mszUserGrade = unpack_data.SerializeString("");
        self.miCountEffects = unpack_data.SerializeInteger("");
        
class STRU_CL_CRS_MESSAGE_ID:
    def __init__(self):
        self.mwTypeID = 6005
        self.mlRoomId = 0;		
	self.mi64UserId = 0;		
	self.mi64DestUserId = 0;	
	self.mbPrivate = 0;		
	self.miResult = 0;		
	self.miCount = 0;		
	self.macText = "";		
	self.mlReserved = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwTypeID)
        pack_data.SerializeLong(self.mlRoomId)
        pack_data.SerializeLongLong(self.mi64UserId)
        pack_data.SerializeLongLong(self.mi64DestUserId)
        pack_data.SerializeByte(self.mbPrivate)
        pack_data.SerializeInteger(self.miResult)
        pack_data.SerializeInteger(self.miCount)
        pack_data.SerializeString(self.macText)
        pack_data.SerializeLong(self.mlReserved)
        
        return pack_data.buff
    
    def UnPack(self,msg_body):
        unpack_data = miku.CSerialize(msg_body,2);
        self.mwTypeID = unpack_data.SerializeWord("")
        self.mlRoomId = unpack_data.SerializeLong("")
        self.mi64UserId = unpack_data.SerializeLongLong("")
        self.mi64DestUserId = unpack_data.SerializeLongLong("")
        self.mbPrivate = unpack_data.SerializeByte("")
        self.miResult = unpack_data.SerializeInteger("")
        self.miCount = unpack_data.SerializeInteger("")
        self.macText = unpack_data.SerializeString("")
        self.mlReserved = unpack_data.SerializeLong("")

class STRU_CL_CRS_GIVE_GIFT_RQ:
    def __init__(self):
        self.mwTypeID = 6044
        self.mlRoomId = 0
        self.mi64UserId = 0             
        self.mi64DestUserId = 0
        self.mszHeroUID = ""              
        self.mszUserName = ""            
        self.mszDstUserName = ""
        self.mszMsgUtf8 =""
        self.mszGiftUID = ""             
        self.miContractId = 0
        self.miBegin = 0
        self.miCount = 0
        self.miTotal = 0
        self.miReserved = 0

    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwTypeID)
        pack_data.SerializeLong(self.mlRoomId)
        pack_data.SerializeLongLong(self.mi64UserId)
        pack_data.SerializeLongLong(self.mi64DestUserId)
        pack_data.SerializeString(self.mszHeroUID)
        pack_data.SerializeString(self.mszUserName)
        pack_data.SerializeString(self.mszDstUserName)
        pack_data.SerializeString(self.mszMsgUtf8)
        pack_data.SerializeString(self.mszGiftUID)
        pack_data.SerializeInteger(self.miContractId)
        pack_data.SerializeInteger(self.miBegin)
        pack_data.SerializeInteger(self.miCount)
        pack_data.SerializeInteger(self.miTotal)
        pack_data.SerializeInteger(self.miReserved)
        return pack_data.buff

class STRU_CL_CRS_GIVE_GIFT_RS:
    def __init__(self):
        self.mwTypeID = 6045
        self.mlRoomId = 0
        self.mi64UserId = 0             
        self.mi64DestUserId = 0
        self.mszUserName = ""              
        self.mszDstUserName = ""            
        self.mszMsgUtf8 = ""
        self.mszGiftUID =""
        self.mwGiftType = 0             
        self.miResult = 0
        self.miContractId = 0
        self.miBegin = 0
        self.miCount = 0
        self.miTotal = 0
        self.mi64LeftPoints = 0
        self.mi64LeftGolden = 0
        self.mi64PaidGolden = 0
        self.mi64PaidPoints = 0
        self.mi64DstLeftPoints = 0
        self.mi64DstLeftGolden = 0
        self.mi64DstGotPoints = 0
        self.mi64DstGotGolden = 0
        self.mi64LuckyGolden = 0
        self.miDisplayPlace = 0
        self.mlGiftCount = 0
        #self.mlTime
        
    def UnPack(self,msg_body):
        unpack_data = miku.CSerialize(msg_body,2);
        self.mwTypeID = unpack_data.SerializeWord("")
        self.mlRoomId = unpack_data.SerializeLong("")
        self.mi64UserId = unpack_data.SerializeLongLong("")
        self.mi64DestUserId = unpack_data.SerializeLongLong("")
        self.mszUserName = unpack_data.SerializeString("")
        self.mszDstUserName = unpack_data.SerializeString("")
        self.mszMsgUtf8 = unpack_data.SerializeString("")
        self.mszGiftUID = unpack_data.SerializeString("")
        self.mwGiftType = unpack_data.SerializeWord("")
        self.miResult = unpack_data.SerializeInteger("")
        self.miContractId = unpack_data.SerializeLongLong("")
        self.miBegin = unpack_data.SerializeInteger("")
        self.miCount = unpack_data.SerializeInteger("")
        self.miTotal = unpack_data.SerializeInteger("")
        self.mi64LeftPoints = unpack_data.SerializeLongLong("")
        self.mi64LeftGolden = unpack_data.SerializeLongLong("")
        self.mi64PaidGolden = unpack_data.SerializeLongLong("")
        self.mi64PaidPoints = unpack_data.SerializeLongLong("")
        self.mi64DstLeftPoints = unpack_data.SerializeLongLong("")
        self.mi64DstGotGolden = unpack_data.SerializeLongLong("")
        self.mi64LuckyGolden = unpack_data.SerializeLongLong("")
        self.miDisplayPlace = unpack_data.SerializeInteger("")
        self.mlGiftCount = unpack_data.SerializeLong("")
        
