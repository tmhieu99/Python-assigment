from os import * 

def readTextFile(filePath):
    msg = "" 
    if not os.path.isfile(filePath):
        raise FileNotFoundError

    with open(filePath, 'r') as file:
        msg = file.read()

    return msg

# Write if file doesn't exist
def writeTextFile(path, content):
    if not os.path.isfile(path):
        f = open(path, 'w+')
        f.write('')

    with open(path, 'a') as file: 
        file.write(data + '\n')
         
