def bubble(array):
    try:
        lnth = len(array)
        temp = 0
        for i in range (0,lnth):
            for k in range (0,lnth-1):
                if (array[k] > array[k+1]):
                    temp = array[k]
                    array[k] = array[k+1]
                    array[k+1] = temp
    except ValueError:
        print ("your list is bad. ¯\_(ツ)_/¯")
    return array

def fileLen(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
        return i +1
    
def readFile(fileName):
    file = open(fileName, "r")
    array = []
    i = 0
    for i in range (0, fileLen(fileName)):
        array.append(file.readline())
        array[i] = array[i].rstrip()
    return array

def writeArray(fileName, array):
    file = open(fileName, "w")
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()

def varToFile(fileName, var):
    try:
        file = open(fileName, "w")
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")
        
def appFile(fileName, var):
    try:
        file = open(fileName, "a")
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")
   
def appArrayToFile(fileName, array):
    file = open(fileName, "a")
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()  
    
        
