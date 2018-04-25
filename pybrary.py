"""
Date: 23042018
Programer: Willpiam
Description:

A library to do a tone of stuff. This way when I have tasks at school I don't have
to write code I already have.

Jokes will liely be made throughout the program in the form of comments

functions will be grouped into catagories (ie sorts, writing / readings)

"""

#-----------sorting algorithums


def bubble(array):#bubble sort
    try:#using try we can make sure the list is viable
        lnth = len(array)#gets length of array
        temp = 0#declaring our tempary varable (needed for sort)
        for i in range (0,lnth):
            for k in range (0,lnth-1):
                if (array[k] > array[k+1]):
                    temp = array[k]
                    array[k] = array[k+1]
                    array[k+1] = temp
    except ValueError:
        print ("your list is bad. ¯\_(ツ)_/¯")

    return array

#----------------file related functions

def fileLen(fileName):#gets length of file
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
        return i +1
    #lifted from: https://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python#1019572
    
    
def readFile(fileName):
    file = open(fileName, "r")
    array = []
    i = 0
    for i in range (0, fileLen(fileName)):
        array.append(file.readline())
        array[i] = array[i].rstrip()
    return array

def writeArray(fileName, array):#takes a filename and an array and writes each element of the array to the file (it may create a
    file = open(fileName, "w")#opens file with append premission
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()

def varToFile(fileName, var):#writes to file
    try:
        file = open(fileName, "w")#opens file with write premission
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")
        
def appFile(fileName, var):#appends to file
    try:
        file = open(fileName, "a")#opens file with append premission
        file.write(str(var)+"\n")
        file.close()
    except:
        print ("something went wrong with function---> varToFile")
   
def appArrayToFile(fileName, array):#takes a filename and an array and writes each element of the array to the file (it may create a
    file = open(fileName, "a")#opens file with append premission
    for i in range (0, len(array)):
        file.write(str(array[i])+"\n")
    file.close()  
    
    
        
