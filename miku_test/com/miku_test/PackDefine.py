'''
Created on Dec 5, 2013

@author: potal
'''
import miku

class ApplyMicRQ(object):
    
    def __init__(self):
        self.mwMsgID = 6023;
        self.mi64UserID = 0;
        self.miMicType = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeInteger(self.miMicType);
        
        return pack_data.buff;

class ApplyMicRS(object):
    def __init__(self):
        self.mwMsgID = 6024;
        self.mi64UserID = 0;
        self.miMicType = 0;
        self.miMicIndex = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miMicType = unpack_data.SerializeInteger(self.miMicType);
        self.miMicIndex = unpack_data.SerializeInteger(self.miMicIndex);
        self.miResult = unpack_data.SerializeInteger(self.miResult);

class SpeakerInfoListID(object):
    def __init__(self):
        self.mwMsgID = 6022;
        self.mbySpeakerCount = 0;
        self.mstrSpeakerInfoList = {};
    def Pack(self):
        pass;
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mbySpeakerCount = unpack_data.SerializeByte(self.mbySpeakerCount);
        if self.mbySpeakerCount <= 0:
            return;
        speak_info_buff = unpack_data.buff;
        for i in range(0,self.mbySpeakerCount):
            temp_speaker_info = SpeakerInfo();
            speak_info_buff = temp_speaker_info.Unpack(speak_info_buff);
            self.mstrSpeakerInfoList[i] = temp_speaker_info;
            
class SpeakerInfo(object):
    def __init__(self):
        self.mi64DstUserID = 0;
        self.mbyMicIndex = 0;
        self.mi64SpeakerUserID = 0;
        self.mbContainAudioInfo = False;
        self.mstrAudioInfo = AudioInfo();
        self.mbContainVideoInfo = False;
        self.mstrVideoInfo = VideoInfo();
        self.mlReserved1 = 0;
        self.mlReserved2 = 0;
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeLongLong(self.mi64DstUserID);
        pack_data.SerializeByte(self.mbyMicIndex);
        pack_data.SerializeLongLong(self.mi64SpeakerUserID);
        pack_data.SerializeByte(self.mbContainAudioInfo);
        
        audio_buff = self.mstrAudioInfo.Pack();
        pack_data.SerializeString(audio_buff);
        
        pack_data.SerializeByte(self.mbContainVideoInfo);
        
        video_buff = self.mstrVideoInfo.Pack();
        pack_data.SerializeString(video_buff);
        
        pack_data.SerializeLong(self.mlReserved1);
        pack_data.SerializeLong(self.mlReserved2);
        
        return pack_data.buff;
    
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mi64DstUserID = unpack_data.SerializeLongLong(self.mi64DstUserID);
        self.mbyMicIndex = unpack_data.SerializeByte(self.mbyMicIndex);
        self.mi64SpeakerUserID = unpack_data.SerializeLongLong(self.mi64SpeakerUserID);
        self.mbContainAudioInfo = unpack_data.SerializeByte(self.mbContainAudioInfo);
        unpack_data.buff = self.mstrAudioInfo.Unpack(unpack_data.buff);
        self.mbContainVideoInfo = unpack_data.SerializeByte(self.mbContainVideoInfo);
        unpack_data.buff = self.mstrVideoInfo.Unpack(unpack_data.buff);
        self.mlReserved1 = unpack_data.SerializeLong(self.mlReserved1);
        self.mlReserved2 = unpack_data.SerializeLong(self.mlReserved2);
    
class AudioInfo(object):
    def __init__(self):
        self.mbyCodecType = 0;
        self.mlSamplesPerSec = 0;
        self.mwKBitsPerSec = 0;
        self.mbyChannels = 0;
        self.mbyBitsPerSample = 0;
        self.mulChannelID = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeByte(self.mbyCodecType);
        pack_data.SerializeLong(self.mlSamplesPerSec);
        pack_data.SerializeWord(self.mwKBitsPerSec);
        pack_data.SerializeByte(self.mbyChannels);
        pack_data.SerializeByte(self.mbyBitsPerSample);
        pack_data.SerializeLong(self.mulChannelID);
        return pack_data.buff;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mbyCodecType = unpack_data.SerializeByte(self.mbyCodecType);
        self.mlSamplesPerSec = unpack_data.SerializeLong(self.mlSamplesPerSec);
        self.mwKBitsPerSec = unpack_data.SerializeWord(self.mwKBitsPerSec);
        self.mbyChannels = unpack_data.SerializeByte(self.mbyChannels);
        self.mbyBitsPerSample = unpack_data.SerializeByte(self.mbyBitsPerSample);
        self.mulChannelID = unpack_data.SerializeLong(self.mulChannelID);
        
        return unpack_data.buff;
        
class VideoInfo(object):
    def __init__(self):
        self.mbyCodecType = 0;
        self.mbyFramePerSecond = 0;
        self.mwFrameWidth = 0;
        self.mwFrameHeight = 0;
        self.mwBitCount = 0;
        self.mulChannelID = 0;
        self.mbyMicType = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeByte(self.mbyCodecType);
        pack_data.SerializeByte(self.mbyFramePerSecond);
        pack_data.SerializeWord(self.mwFrameWidth);
        pack_data.SerializeWord(self.mwFrameHeight);
        pack_data.SerializeWord(self.mwBitCount);
        pack_data.SerializeLong(self.mulChannelID);
        pack_data.SerializeByte(self.mbyMicType);
        return pack_data.buff;
    
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mbyCodecType = unpack_data.SerializeByte(self.mbyCodecType);
        self.mbyFramePerSecond = unpack_data.SerializeByte(self.mbyFramePerSecond);
        self.mwFrameWidth = unpack_data.SerializeWord(self.mwFrameWidth);
        self.mwFrameHeight = unpack_data.SerializeWord(self.mwFrameHeight);
        self.mwBitCount = unpack_data.SerializeWord(self.mwBitCount);
        self.mulChannelID = unpack_data.SerializeLong(self.mulChannelID);
        self.mbyMicType = unpack_data.SerializeByte(self.mbyMicType);
        
        return unpack_data.buff;
        
class ApplyPrivateMicRQ(object):
    def __init__(self):
        self.mwMsgID = 6030;
        self.mi64UserID = 0;
        self.miMicType = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeInteger(self.miMicType);
        
        return pack_data.buff;
        
class ApplyPrivateMicRS(object):
    def __init__(self):
        self.mwMsgID = 6031;
        self.mi64UserID = 0;
        self.miMicType = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miMicType = unpack_data.SerializeInteger(self.miMicType);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        
class PutPublicMicRQ(object):
    def __init__(self):
        self.mwMsgID = 6026;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;
        self.miMicType = 0;
        self.mlReserved = 0;
    
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64ManagerID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeInteger(self.miMicType);
        pack_data.SerializeLong(self.mlReserved);
        
        return pack_data.buff;

class PutPublicMicRS(object):
    def __init__(self):
        self.mwMsgID = 6027;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;
        self.miMicIndex = 0;
        self.miMicType = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64ManagerID = unpack_data.SerializeLongLong(self.mi64ManagerID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miMicIndex = unpack_data.SerializeInteger(self.miMicIndex);
        self.miMicType = unpack_data.SerializeInteger(self.miMicType);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        
class PutPrivateMicRQ(object):
    def __init__(self):
        self.mwMsgID = 6038;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;    
        self.miMicType = 0;
        self.mlReserved = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64ManagerID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeInteger(self.miMicType);
        pack_data.SerializeLong(self.mlReserved);
        
        return pack_data.buff;

class PutPrivateMicRS(object):
    def __init__(self):
        self.mwMsgID = 6039;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64ManagerID = unpack_data.SerializeLongLong(self.mi64ManagerID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        
class InvitePrivateMicRQ(object):
    def __init__(self):
        self.mwMsgID = 6034
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        self.miTimeout = 0;
        self.mlReserved = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLongLong(self.mi64DstUserID);
        pack_data.SerializeInteger(self.miTimeout);
        pack_data.SerializeLong(self.mlReserved);
        
        return pack_data.buff;
    
class InvitePrivateMicRS(object):
    def __init__(self):
        self.mwMsgID = 6035;
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        self.mlDstChannelID = 0;
        self.mlThisChannelID = 0;
        self.mlReserved = 0;
        self.miResult = 0;
        self.mszReason = '';
    
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLongLong(self.mi64DstUserID);
        pack_data.SerializeLong(self.mlDstChannelID);
        pack_data.SerializeLong(self.mlThisChannelID);
        pack_data.SerializeLong(self.mlReserved);
        pack_data.SerializeInteger(self.miResult);
        pack_data.SerializeString(self.mszReason);
        
        return pack_data.buff;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.mi64DstUserID = unpack_data.SerializeLongLong(self.mi64DstUserID);
        self.mlDstChannelID = unpack_data.SerializeLong(self.mlDstChannelID);
        self.mlThisChannelID = unpack_data.SerializeLong(self.mlThisChannelID);
        self.mlReserved = unpack_data.SerializeLong(self.mlReserved);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        self.mszReason = unpack_data.SerializeString(self.mszReason);

class UserStopSpeakID(object):
    def __init__(self):
        self.mwMsgID = 6025;
        self.mi64UserID = 0;
        self.miIndex = 0;
        self.miChannelID = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeInteger(self.miIndex);
        pack_data.SerializeInteger(self.miChannelID);
        return pack_data.buff;
    
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miIndex = unpack_data.SerializeInteger(self.miIndex);
        self.miChannelID = unpack_data.SerializeInteger(self.miChannelID);

class GetUserIPRQ(object):
    def __init__(self):
        self.mwMsgID = 6077;
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        self.mlReserved = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLongLong(self.mi64DstUserID);
        pack_data.SerializeLong(self.mlReserved);
        
class GetUserIPRS(object):
    def __init__(self):
        self.mwMsgID = 6078;
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        self.mszDstUserIP = '';
        self.mszDstUserAddr = '';
        self.mlReserved = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.mi64DstUserID = unpack_data.SerializeLongLong(self.mi64DstUserID);
        self.mszDstUserIP = unpack_data.SerializeString(self.mszDstUserIP);
        self.mszDstUserAddr = unpack_data.SerializeString(self.mszDstUserAddr);
        
class KickOutRoomRQ(object):
    def __init__(self):
        self.mwMsgID = 6065;
        self.mlRoomID = 0;
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        
    def Pack(self):        
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLong(self.mlRoomID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLongLong(self.mi64DstUserID);
        
class KickOutRoomRS(object):
    def __init__(self):
        self.mwMsgID = 6066;
        self.mlRoomID = 0;
        self.mi64UserID = 0;
        self.mi64DstUserID = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mlRoomID = unpack_data.SerializeLong(self.mlRoomID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.mi64DstUserID = unpack_data.SerializeLongLong(self.mi64DstUserID);     
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        
class RoomBlackListRQ(object):
    def __init__(self):
        self.mwMsgID = 6051;
        self.mlRoomID = 0;
        self.miOperator = 0;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;
        self.mlReserved = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLong(self.mlRoomID);
        pack_data.SerializeInteger(self.miOperator);
        pack_data.SerializeLongLong(self.mi64ManagerID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLong(self.mlReserved);
        
class RoomBlackListRS(object):
    def __init__(self):
        self.mwMsgID = 6052;
        self.mlRoomID = 0;
        self.miOperator = 0;
        self.mi64ManagerID = 0;
        self.mi64UserID = 0;
        self.mszPhotoUID = '';
        self.mszBlackUserName = '';
        self.miResult = 0;
        self.mlReserved = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mlRoomID = unpack_data.SerializeLong(self.mlRoomID);
        self.miOperator = unpack_data.SerializeInteger(self.miOperator);
        self.mi64ManagerID = unpack_data.SerializeLongLong(self.mi64ManagerID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);     
        self.mszPhotoUID = unpack_data.SerializeString(self.mszPhotoUID);
        self.mszBlackUserName = unpack_data.SerializeString(self.mszBlackUserName);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        self.mlReserved = unpack_data.SerializeLong(self.mlReserved);
        
class UserDiceGameRQ(object):
    def  __init__(self):
        self.mwMsgID = 5050;
        self.mi64UserID = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        
class UserDiceGameID(object):
    def __init__(self):
        self.mwMsgID = 5051;
        self.mi64UserID = 0;
        self.miRand = 0;
        self.miResult = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.miRand = unpack_data.SerializeInteger(self.miRand);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        
class UserSmashGoldEggRQ(object):
    def __init__(self):
        self.mwMsgID = 6514;
        self.mi64UserID = 0;
        self.mlRoomID = 0;
        
    def Pack(self):
        pack_data = miku.CSerialize('',1);
        pack_data.SerializeWord(self.mwMsgID);
        pack_data.SerializeLongLong(self.mi64UserID);
        pack_data.SerializeLong(self.mlRoomID);
        
class UserSmashGoldEggRS(object):
    def __init__(self):
        self.mwMsgID = 6515;
        self.mi64UserID = 0;
        self.mlRoomID = 0;
        self.miResult = 0;
        self.miCountEggs = 0;
        self.mi64GotCumoney = 0;
        self.mi64UserCumoney = 0;
        self.mdwTickTime = 0;
        
    def Unpack(self,buff):
        unpack_data = miku.CSerialize(buff,2);
        self.mwMsgID = unpack_data.SerializeWord(self.mwMsgID);
        self.mi64UserID = unpack_data.SerializeLongLong(self.mi64UserID);
        self.mlRoomID = unpack_data.SerializeLong(self.mlRoomID);
        self.miResult = unpack_data.SerializeInteger(self.miResult);
        self.miCountEggs = unpack_data.SerializeInteger(self.miCountEggs);
        self.mi64GotCumoney = unpack_data.SerializeLongLong(self.mi64GotCumoney);
        self.mi64UserCumoney = unpack_data.SerializeLongLong(self.mi64UserCumoney);
        self.mdwTickTime = unpack_data.SerializeInteger(self.mdwTickTime);
        
        
        
