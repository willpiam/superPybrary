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


#bubble sort

def bubble(array):
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
