import os
from functools import reduce 
from knight import Knight
from event import Event



class Controller:

    knightTuple = tuple()

    def __init__(self, fileName):
        self.knightTuple = self.getData(fileName)

    def readTextFile(self, fileName):

        content = ""
    
        if not os.path.isfile(fileName):
            raise FileNotFoundError
        with open(fileName, 'r') as file:
            content = file.read()

        return content

    def getData(self, fileName):
        
        # Get data from input files
        dataFromFile = self.readTextFile("./" + fileName)

        # Get each lines
        data = dataFromFile.split("\n")

        # Get first line
        dataFirstLine = data[0]

        # Get knight attribute in first line
        splitDataFirstLine = dataFirstLine.split(" ")
        knightHp = splitDataFirstLine[0]
        knightLevel = splitDataFirstLine[1]
        knightRingSign = splitDataFirstLine[2]

        # Get journey list
        journeyList = list()
        for index in range(1, len(data)):
            journeyList += data[index].split(" ")

        #print("event length " + str(len(journeyList)))

        while '' in journeyList:
            for x in journeyList:
                if x == '':
                    journeyList.remove(x)
        #print("event length " + str(len(journeyList)))
            
        return (knightHp, knightLevel, knightRingSign, journeyList)

    def battle(self):
        
        # Set knight attribute
        knight = Knight(self.knightTuple[0], self.knightTuple[1], self.knightTuple[2], self.knightTuple[3])

        knightRingSignList = knight.getRingSignList()

        index = 1

        for journey in knight.getJourneyList():
            
            knightHp = knight.getKnightHP()

            # If knight Hp <= 0 => Lose the game
            if knightHp <= 0 : 
                print("Knight lose")
                break

            # Get journey index 
            indexJourney = index

            index += 1

            # print(str(journey) + " " + str(indexJourney))
            eventObj = Event(journey, indexJourney)

            eventTuple = eventObj.checkEventCode()

            event = eventTuple[0]

            if event == 0:
                print("Knight win")
                break
            elif event == -1:
                continue

            knightRingSignList, knightHp = self.battleCase(event, knightHp, knight.getKnightMaxHp(), knight.getKnightLevel(), knightRingSignList, eventObj.getLevelO(), eventObj.getRingSignO())
            
            knight.setKnightHp(knightHp)

        # print(knight.getRingSignList())
        stringRingSignList = [str(x) for x in knightRingSignList]
        stringRingSignList = "".join(stringRingSignList)

        return stringRingSignList, knight.getKnightHP()
    
    def battleCase(self, event, knightHp, knightMaxHp, knightLevel, knightRingSignList, levelO, ringSignO):

        # 2 No battle cases
        if event == 7:
            return self.event7_Arwen(knightRingSignList, ringSignO), knightHp

        elif event == 8:
            return self.event8_Galadriel(knightRingSignList, knightHp, knightMaxHp )

        # Battle cases
        if knightLevel > levelO:
            knightRingSignList.append(ringSignO)
            if event == 9:
                knightRingSignList = self.event9_Saruman(knightRingSignList, win =  True)

        elif knightLevel < levelO:
            if event == 4:
                knightRingSignList = self.event4_Gollum(knightRingSignList, ringSignO)

            elif event == 5:
                knightRingSignList = self.event5_Lurtz(knightRingSignList)

            elif event == 9:
                knightRingSignList = self.event9_Saruman(knightRingSignList, ringSignO, win = False)

            damage = self.getdamage(event, levelO)
            
            # Calculate HP left
            knightHp = int(knightHp - damage)
            #print(knightHp)
            
            # If out of Hp => Lose 
            if knightHp <= 0:
                knightRingSignList = []
                return knightRingSignList, knightHp
        else: 
            return knightRingSignList, knightHp

        return knightRingSignList, knightHp
    
    '''
    No special actions
    '''
    def event1_Uruk(self):
        pass

    def event2_Ringwraiths(self):
        pass

    def event3_Strider(self):
        pass

    def event6_Gimli(self):
        pass

    '''
    If the knight loses to Gollum, Gollum will take the last ringsign with its same number
    from the knight's EC. If no such ringsign exists in the knight's EC list, Gollum will do nothing (the
    knight still loses HP)
    '''
    def event4_Gollum(self, knightRingSignList, ringSignO):
        foundIndex = -1

        for index in range(0, len(knightRingSignList)):

            if knightRingSignList[index] == ringSignO:
                foundIndex = index
        
        if foundIndex != -1:
            knightRingSignList.pop(foundIndex)
        
        return knightRingSignList
        
    '''
    If the knight loses to Lurtz, the knight will be robbed of first three ringsigns of his EC
    list.
    '''
    def event5_Lurtz(self, knightRingSignList):
        
        return knightRingSignList[3::]

    
    
    '''
    If the knight meets Arwen (the event code is 7X), she will take all the knight's
    ringsigns and grant the knight a different Elrond’s Code so that the new the Elrond’s Code of the
    knight will be greater than the old properly X units.
    '''
    def event7_Arwen(self, knightRingSignList, ringSignO):
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

            tempIndex = index + 1
            
            # If index overflow => create new list by adding old list with [0]
            if tempIndex > len(knightRingSignList):
                knightRingSignList = [0] + knightRingSignList

            else:
                knightRingSignList[-tempIndex] = knightRingSignList[-tempIndex] + 1
                
                tempRingSignO = knightRingSignList[-tempIndex]

                index += 1
        
        return knightRingSignList

    '''
    When the knight meets
    Galadriel, the knight will trade the last rignsign in his Elrond’s Code to restore his HP to maxHP.
    If the knight’s HP is equal to maxHP, the knight will not do the trade.
    '''
    def event8_Galadriel(self, knightRingSignList, knightHp, knightMaxHp ):

        if knightHp != knightMaxHp:

            if knightRingSignList == []:
                return knightRingSignList, knightHp

            knightRingSignList = knightRingSignList[:-1]
            knightHp = knightMaxHp

        return knightRingSignList, knightHp
            
    '''
    If the knight defeats and takes ringsign from Saruman, Saruman will reverse the order
    of the knight's EC list. On the other hand, if the knight loses Saruman, Saruman would snatch all
    the ringsigns with the same number on the ringsign of Saruman
    '''
    def event9_Saruman(self, knightRingSignList, *ringSignO , win):

        if win is True:
            return knightRingSignList[::-1]

        else :

            for x in knightRingSignList:
                if x == ringSignO:
                    knightRingSignList.remove(x)

            return knightRingSignList
    
    def getdamage(self, event, levelO):

        # Define damage dict 
        baseDamage = {
            1 : 0.8,
            2 : 1.2,
            3 : 4.1,
            4 : 7.9, 
            5 : 6.5,
            6 : 8.7,
            9 : 0.1
        }
        
        damage = round(baseDamage.get(event)* levelO* 10)

        #print("DAMAGE : " + str(baseDamage.get(event)) + " * " + str(levelO) + " * "+ "10 = " + str(damage))

        return damage

    
        
    
    
            

            

            

        