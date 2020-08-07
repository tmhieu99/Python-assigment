from event import Event
from knight import Knight
from utils import * 

class Controller: 

    knightList = tuple()

    def __init__(self, fileName):
        self.knightList = self.getKnightAttribute(fileName)

    def getKnightAttribute(self, fileName):
        # Get file content  
        content = readTextFile("./" + fileName)

        # Get each line
        data = content.split("\n")

        firstLine = data[0]

        # Get knight attribute 
        attribute = firstLine.split(" ")
        knightHP  = attribute[0]
        knightLv  = attribute[1]
        knightRingSign = attribute[2]

        # Get journey event
        journeyList = list()
        for index in range(1, len(data)):
            journeyList += data[index].split(" ")

        # Remove misc 
        while '' in journeyList:
            for i in journeyList:
                if i == '':
                    journeyList.remove(i)

        print(knightHP + " " + knightLv + "" + knightRingSign)
        print(journeyList)

        return (knightHP, knightLv, knightRingSign, journeyList)

    def battle(self): 
        knight = Knight(self.knightList[0], self.knightList[1], self.knightList[2], self.knightList[3])

        knightRingSign = knight.getRingSign()

        index = 1 

        for journey in knight.getJourneyList():
            knightHP = knight.getKnightHP()

            if knightHP <= 0:
                break
            indexJourney = index 

            index += 1

            eventObj = Event(journey, indexJourney)

            eventTup = eventObj.checkEventCode()

            # Get event data 
            event = eventTup[0]

            if event == 0: 
                print("The knight has finished the competition")
                break
            elif event == -1: 
                continue 
        
            knightRingSign, knightHP = self.battleCase(event, knightHP, knight.getKnightMaxHP(), knight.getKnightLv(), knightRingSign, eventObj.getLevelO(), eventObj.getRingSignO())
            knight.setKnightHP(knightHP)

            print("Knight get ring sign:" + knight.getRingSign())
            ringSignList = [str(x) for x in knightRingSign]
            ringSignList = "".join(ringSignList)
            print("ringSignList:" + ringSignList)

            return ringSignList, knight.getKnightHP()

    def getDamage(self, event, levelO):
        baseDmg = {
            1 : 0.8,
            2 : 1.2,
            3 : 4.1,
            4 : 7.9,
            5 : 6.5,
            6 : 8.7,
            9 : 0.1
        }

        damage = round(baseDmg.get(event)* levelO* 10)

        print("Damage: " + str(baseDmg.get(event)) + "/" + str(levelO) + "/" + "10 = " + str(damage))
        return damage
    
    def battleCase(self, event, knightHp, knightMaxHp, knightLevel, knightRingSignList, levelO, ringSignO):
        # The knight encounter a beautiful half-elf princess of Rivendell, Arwen.
        if event == 7:
            return self.event7_EncounterArwen(knightRingSignList, ringSignO), knightHp
        # Encounter Galadriel, the elven co-ruler of Lothlórien.
        elif event == 8:
            return self.event8_EncounterGaladriel(knightRingSignList, knightHp, knightMaxHp )

        # The knight win the battle
        if knightLevel > levelO:
            knightRingSignList.append(ringSignO)
            # the knight defeats Saruman
            if event == 9:
                knightRingSignList = self.event9_EncounterSaruman(knightRingSignList, winFlag =  True)
        # The knight lose the battle
        elif knightLevel < levelO:
            # the knight loses to Gollum
            if event == 4:
                knightRingSignList = self.event4_EncounterGollum(knightRingSignList, ringSignO)
            #  the knight loses to Lurtz
            elif event == 5:
                knightRingSignList = self.event5_EncounterLurtz(knightRingSignList)
            # the knight loses Saruman
            elif event == 9:
                knightRingSignList = self.event9_EncounterSaruman(knightRingSignList, ringSignO, winFlag = False)
            # Get damage 
            damage = self.getDamage(event, levelO)
            # Recalculating the knight hp

            knightHp = int(knightHp - damage)
            
            # If the knight loses the battle
            if knightHp <= 0:
                knightRingSignList = []
                return knightRingSignList, knightHp
        # The battle is tie
        else: 
            return knightRingSignList, knightHp
        # print("knightHP : " + str(knightHp))
        return knightRingSignList, knightHp

        def event1_FightingUruk(self):
            pass

    def event2_EncounterRingwraiths(self):
        pass

    def event3_EncounterStrider(self):
        pass

    
    def event4_EncounterGollum(self, knightRingSignList, ringSignO):
        foundIndex = -1

        for index in range(0, len(knightRingSignList)):
            if knightRingSignList[index] == ringSignO:
                foundIndex = index
        
        if foundIndex != -1:
            knightRingSignList.pop(foundIndex)
        
        return knightRingSignList
        
    def event5_EncounterLurtz(self, knightRingSignList):
        
        return knightRingSignList[3::]

    def event6_EncounterGimli(self):
        pass

    
    def event7_EncounterArwen(self, knightRingSignList, ringSignO):
        index = 1
        
        try:
            tempRingSignO = knightRingSignList[-index] + ringSignO
        
        except IndexError:
            
            return knightRingSignList
        
        if tempRingSignO < 10:
            knightRingSignList[-1] = tempRingSignO

        while tempRingSignO > 9:
            newValue = int((str(tempRingSignO)[-1]))
            
            knightRingSignList[-index] = newValue

            walker = index + 1
            
            # If the index is out of range
            if walker > len(knightRingSignList):
                knightRingSignList = [0] + knightRingSignList
            else:
                knightRingSignList[-walker] = knightRingSignList[-walker] + 1
                
                tempRingSignO = knightRingSignList[-walker]

                index += 1
        
        return knightRingSignList

    def event8_EncounterGaladriel(self, knightRingSignList, knightHp, knightMaxHp ):
        if knightHp != knightMaxHp:
            # If ring sign list is empty => Do not trade
            if knightRingSignList == []:
                return knightRingSignList, knightHp
            knightRingSignList = knightRingSignList[:-1]
            knightHp = knightMaxHp

        return knightRingSignList, knightHp

    def event9_EncounterSaruman(self, knightRingSignList, *ringSignO , winFlag):
        if winFlag is True:
            return knightRingSignList[::-1]
        else :

            # Get the index of element with has the same value with Saruman ringsign
            for x in knightRingSignList:
                if x == ringSignO:
                    knightRingSignList.remove(x)

            return knightRingSignList