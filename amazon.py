# Modules required for program functions
from math import ceil, floor
import re

# Initialize empty list variables and count variable 'x'
keys = []
values = []
numList = []
minList = []
maxList = []
avgList = []
sumList = []
pList = []
pSplit = []
x = 0


def minNum(minList):
    '''
    -   Function that takes in a list of integers, calculates 
        and returns the lowest number in the list.
    '''
    # Assign minlist value to 'numHold' variable and empty 
    # the minList variable.
    numHold = minList
    minList = []

    # For loop that calculates the min number for all items 
    # in a list and appends to the 'minList' variable.     
    for num in numHold:
        minList.append (min(num))

    # Return minList
    return(minList)

def maxNum(maxList):
    '''
    -   Function that takes in a list of integers, calculates 
        and returns the highest number in the list.
    '''
    # Assign maxlist value to 'numHold' variable and empty 
    # the maxList variable.
    numHold = maxList
    maxList = [] 

    # For loop that calculates the max number for all items 
    # in a list and appends to the 'maxList' variable.     
    for num in numHold:
       maxList.append (max(num)) 
    
    # Return maxlist
    return(maxList)

def avg(avgList):
    '''
    -   Function that takes in a list of integers, calculates 
        and returns the average number in the list.
    '''
    # Assign avgList value to 'numHold' variable and empty 
    # the avgList variable.
    numHold = avgList
    avgList = []

    # For loop that calculates the average number for all 
    # items in a list and appends to the 'avgList' variable.
    for item in numHold:
        avgList.append( sum(item) / len(item) ) 

    # Return avgList
    return(avgList)

def percentile(pList, pSplit):
    '''
    -   Function that takes in a list of integers, calculates
        and returns the [n]th percentile number in the list.
    '''
    # Assign pList value to 'numHold' variable and empty the 
    # pList variable. Initialize counter variable 'index'.
    numHold = pList
    pList = []
    index = 0
    
    # For loop that calculates the [n]th percentile number
    # for all items in a list and appends to the 
    # 'pList' variable.
    for item in numHold:
        x = ceil(((pSplit[index]/100) * len(numHold[index])) * 10)
        pList.append(floor(x / 10))
        index += 1
    return(pList)

def sumOf(sumList):
    '''
    -   Function that takes in a list of integers, calculates 
        and returns the sum of the list.
    '''
    sumList = [sum(sumList[0])]
    return(sumList)

# Read in input file and store as 'f'. 
with open('input.txt', 'r+', encoding = 'utf-8-sig') as f:
    
    # Store store lines in file as lists as
    # variable 'content'
    content = [re.split(':', x) for x in f.readlines()]

# For loop that splits data into key/strings and values/
# integers
for lists in content:
    keys += (lists[0].split(','))
    numList += (lists[1].strip()).split(':')
    values.append([int(num) for num in numList[x].split(',')])
    x += 1

# Enumerate the list variables and cast to dictionary 
# objects,
keys = dict(list(enumerate(keys, start = 1)))
values = dict(list(enumerate(values, start = 1)))

# Reset x counter to null
x = 0  

# For loop that that extracts the key and value items from
# the 'key' dictionary. If the condition matches, uses the 
# key to access 'values'dictionary item and assigns it to 
# unique list variables. Once respective functions run, 
# calls the functions and writes the values to output file 
# as required.
with open('output.txt', 'w') as f:  
    for key, value in keys.items():

        if 'min' in value:
            minList += [values[key]]
            f.write(f'The {value} of {minList[x]} is: {minNum(minList)[x]}')

        elif 'max' in value:
            maxList += [values[key]]
            f.write(f'\nThe max of {maxList[x]} is: {maxNum(maxList)[x]}')

        elif 'avg' in value:
            avgList += [values[key]]
            f.write(f'\nThe avg of {avgList[x]} is: {avg(avgList)[x]}')

        elif 'p' in value:
            pSplit.append(int((value.split('p'))[1]))
            pList += [values[key]]
            percentList = percentile(pList, pSplit)
            f.write(f'\nThe {pSplit[x]}th percentile of {pList[x]} is: {percentList[x]}')

        elif 'sum' in value:
            sumList += [values[key]]
            f.write(f'The sum of {sumList[x]} is: {sumOf(sumList)[x]}')
            x += 1