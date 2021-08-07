from mhash import *
import datetime
import time

class tockenManage:
    def __init__(self):
        self.tockenMap = {}
    
    def setTocken(self,name):
        mtime = int(time.time())
        tocken = md5(name + "12asd123" + str(mtime) )
        mapdata = (name,mtime)
        self.tockenMap[tocken] = mapdata
        return tocken
    
    def checkTocken(self,tocken):
        if(tocken in self.tockenMap):
            mapdata = self.tockenMap[tocken]
            #超时
            mapTime = mapdata[1]
            if  int(time.time()) -mapTime > 300 :
                return False
            return True
        else:
            return False

    
    def removeTocken(self,tocken):
        if tocken in self.tockenMap:
            del self.tockenMap[tocken]


    def getTockenName(self,tocken):
        if(tocken in self.tockenMap):
            mapdata = self.tockenMap[tocken]
            return mapdata[0]
        return ''


if __name__ == "__main__":
    tm = tockenManage()
    tm.setTocken('name')