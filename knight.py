"""
Class Knight 
""" 

class Knight:
    #Init some attributes
    __knightHP       = 0
    __knightMaxHP    = 0
    __knightLv       = 0
    __knightRingSign = 0
    __ringSignList   = list()
    __journeyList    = list()

    def __init__(self, knightHP, knightLv, knightRingSign, knightJourneyList):
        self.__knightHP       = int(knightHP)
        self.__knightLv       = int(knigthLv)
        self.__knightMaxHP    = int(knightHP)
        self.__knightRingSign = knightRingSign
        self.__ringSignList   = [int(knightRingSign)]
        self.__journeyList    = knightJourneyList

    #Get set methods for Knight attributes
    def getKnightHP(self):
        return self.__knightHP

    def setKnightHP(self, newHP):
        self.__knightHP = newHP
    
    def getKnightMaxHP(self):
        return self.__knightMaxHP

    def setKnigthMaxHP(self, newMaxHP):
        self.__knightMaxHP = newMaxHP

    def getKnightLv(self):
        return self.__knightLv

    def setKnightLv(self, newLv):
        self.__knightLv = newLv

    def getRingSign(self):
        return self.__knightRingSign

    def setRingSign(self, newSign):
        self.__knightRingSign = newSign

    #List methods for Knight attributes
    def getJourneyList(self):
        return self.__journeyList
    
    def addJourneyList(self, newJourney):
        self.__journeyList.append(newJourney)

    def deleteJourneyList(self):
        self.__journeyList.clear()

    def getRingSign(self):
        return self.__knightRingSign
    
    def addRingSign(self, ringSign):
        self.__ringSignList.append(ringSign)

    def deleteRingSign(self):
        self.__ringSignList.clear()

