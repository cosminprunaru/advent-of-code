import os
import sys
import string

filepath = os.path.dirname(os.path.abspath(__file__)) 
filename = r'puzzle-input.txt'

class BagContent:
    def __init__(self, color, number):
        self.color = color
        self.number = number

    def __repr__(self):
        return self.color + ' => ' + self.number

def readInput(filename):
    # Check the existence of input
    if os.path.isfile(filename):
        f = open(filename, 'r')
        return f.readlines()
    else:
        print 'File {} not found'.format(filename)
        sys.exit()

def recursiveGoldCheck(bag, bagsDict):
    if 'shiny gold' in [item.color for item in bagsDict[bag]]:
        return True
    elif bagsDict[bag] == []:
        return False
    else:
        for innerBag in bagsDict[bag]:
            if recursiveGoldCheck(innerBag.color, bagsDict):
                return True
        return False

def getBagCapacity(bag, bagsDict):
    if bagsDict[bag] == []:
        return 0
    
    count = 0
    for innerBag in bagsDict[bag]:
        count += int(innerBag.number) + int(innerBag.number) * getBagCapacity(innerBag.color, bagsDict)
    return count

def getShinyGoldCapacity(bagsDict):
    return getBagCapacity('shiny gold', bagsDict)

def createBagsDictionary(bags):
    bagsDict = {}
    for line in bags:
        bag = [a.strip(',.\n ') for a in line.split('contain')]
        children = [ BagContent(a.strip().split(' ', 1)[1][:-5 if int(a.strip()[0]) > 1 else -4], a.strip()[0]) for a in bag[-1].split(',') if 'no other bags' not in a]
        
        bagsDict[bag[0].replace(' bags', '')] = children

    return bagsDict

def getShinyGoldBagHoldersPart1(bags):
    bagsDict = createBagsDictionary(bags)

    count = 0
    for bag, _ in bagsDict.items():
        if recursiveGoldCheck(bag, bagsDict):
            count += 1

    print 'Shiny gold bag can be fitted inside {} other bags'.format(count)  

def getShinyGoldBagContentsPart2(bags):
    bagsDict = createBagsDictionary(bags)
    print 'Shiny gold capacity is {} bags'.format(getShinyGoldCapacity(bagsDict))

def main(task):
    bags = readInput(filename)
    if task == 1:
        getShinyGoldBagHoldersPart1(bags)
    else:
        getShinyGoldBagContentsPart2(bags)  

if __name__ == '__main__':
    os.chdir(filepath)
    try:
        task = int(raw_input('Enter number of task to be solved for day 7 Advent of Code: '))
        if task != 1 and task != 2:
            print 'Nope, you have to provide me with either Task 1 or Task 2'
            sys.exit()

        main(task)        
    except ValueError:
        print 'Nope, you have to provide me with either Task 1 or Task 2'