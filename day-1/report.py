import os
import sys

filepath = os.path.dirname(os.path.abspath(__file__))
filename = r'puzzle-input.txt'

t1_text = 'First number is {}, second number is {} and their product is {}'
t2_text = 'First number is {}, second number is {}, third number is {} and their product is {}'

def readInput(filename):
    # Check the existence of input
    if os.path.isfile(filename):
        f = open(filename, 'r')
        return f.readlines()
    else:
        print 'File {} not found'.format(filename)
        sys.exit()

def task1():
    report = readInput(filename)
    lines = len(report)

    for i in xrange(lines):
        for j in xrange(i + 1, lines):
            if int(report[i]) + int(report[j]) == 2020:
                print t1_text.format(int(report[i]), int(report[j]), int(report[i]) * int(report[j]))
                return

def task2():
    report = readInput(filename)
    lines = len(report)

    for i in xrange(lines):
        for j in xrange(i + 1, lines):
            for k in xrange(j + 1, lines):
                if int(report[i]) + int(report[j]) + int(report[k]) == 2020:
                    print t2_text.format(int(report[i]), int(report[j]), int(report[k]), int(report[i]) * int(report[j]) * int(report[k]))
                    return

def main(task):
    if task == 1:
        task1()
    else:
        task2()

if __name__ == '__main__':
    os.chdir(filepath)

    try:
        task = int(raw_input('Enter number of task to be solved for day 1 Advent of Code: '))
        if task != 1 and task != 2:
            print 'Nope, you have to provide me with either Task 1 or Task 2'
            sys.exit()

        main(task)        
    except ValueError:
        print 'Nope, you have to provide me with either Task 1 or Task 2'