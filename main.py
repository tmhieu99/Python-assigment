
from functools import reduce
from controller import Controller
import sys
import os 

# Parameter for the number of input files.
NO_OF_TEST_CASE = 22

def writeTextFile(path, data):
    if not os.path.isfile(path):
        f = open(path, 'w+')
        f.write('')
    with open(path, 'a') as file:
        file.write(data + '\n')

def knight_journey(filename, case): 

    controller = Controller(filename)

    result = controller.battle()

    # Log outputs into 1 file.
    if result[0] == "": #Lose case
        writeTextFile("solution.txt"," ")
    else:
        writeTextFile("solution.txt",str(result[0]))



if __name__ == "__main__":

    for index in range(1, NO_OF_TEST_CASE):

        knight_journey("input/input (" + str(index) + ").txt", index)        
        

    