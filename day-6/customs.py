import os
import sys
import string

filepath = os.path.dirname(os.path.abspath(__file__)) 
filename = r'puzzle-input.txt'

class Custom():
    def __init__(self, answers):
        self.answers = answers
    
    '''
    def __repr__(self):
        print self.answers
'''
class Group():
    def __init__(self):
        self.customs = []

    def addCustom(self, custom):
        self.customs.append(custom)

    def checkCustoms(self, anyF):
        letterCount = dict.fromkeys(string.ascii_lowercase, 0)
        for custom in self.customs:
            for letter in list(string.ascii_lowercase):
                if letter in custom.answers:
                    letterCount[letter] += 1 
        
        res = 0
        for _, occ in letterCount.items():
            if anyF:
                if occ != 0:
                    res += 1
            else:
                if occ == len(self.customs):
                    res += 1

        self.customs = []

        return res

def readInput(filename):
    # Check the existence of input
    if os.path.isfile(filename):
        f = open(filename, 'r')
        return f.readlines()
    else:
        print 'File {} not found'.format(filename)
        sys.exit()

def getCustomsCount(customs, flag):
    res = 0
    group = Group()
    for line in customs:
        if line != '\n':
            group.addCustom(Custom(line))
            if line is customs[-1]:
                res += group.checkCustoms(flag)
            continue

        res += group.checkCustoms(flag)

    return res

def main(task):
    customs = readInput(filename)
    print getCustomsCount(customs, task == 1)

if __name__ == '__main__':
    os.chdir(filepath)
    try:
        task = int(raw_input('Enter number of task to be solved for day 6 Advent of Code: '))
        if task != 1 and task != 2:
            print 'Nope, you have to provide me with either Task 1 or Task 2'
            sys.exit()

        main(task)        
    except ValueError:
        print 'Nope, you have to provide me with either Task 1 or Task 2'