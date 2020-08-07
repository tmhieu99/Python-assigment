
class Event: 
    __index     = 0
    __eventCode = 0
    __ringSignO = 0
    __levelO    = 0

    def __init__(self, index, eventCode):
        self.__index = index
        #Convert from eventCode string to int 
        self.__eventCode = int(eventCode)

    def getLevelO(self):
        return self.__levelO

    def getRingSignO(self):
        return self.__ringSignO

    def eventNotExist(self):
        return (-1,-1,-1)

    def journeyFinished(self):
        return (0,-1,-1)

    def checkEventCode(self):
        if self.__eventCode == 0: 
            return self.journeyFinished()
        elif self.__eventCode == 9 or self.__eventCode < 8 or self.__eventCode > 100 or self.__eventCode in range (80,90):
            return self.eventNotExist
        
        # Get event type from event code 
        i = self.__index
        b = i % 10

        # Get opponent's level 
        self.__levelO = (b if b > 5 else 5) if i > 6 else b

        # Get opponent's ring sign(factor X)
        self.__ringSignO = self.__eventCode % 10

        # Get event type 
        event = int(str(self.__eventCode)[0:1])

        return (event, self.__levelO, self.__ringSignO)        

