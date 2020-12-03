import os
import sys

filepath = os.path.dirname(os.path.abspath(__file__)) 
filename = r'puzzle-input.txt'

def readInput(filename):
    # Check the existence of input
    if os.path.isfile(filename):
        f = open(filename, 'r')
        return f.readlines()
    else:
        print 'File {} not found'.format(filename)
        sys.exit()

def countTreesOnSlope(slopeMap, right, down):
    trees = 0
    col = 0
    
    mapCycle = len(slopeMap[1])

    print 'Checking slope by going right {} {} and down {} {}'.format(right, 'time' if right is 1 else 'times', down, 'time' if down is 1 else 'times')
    for row in xrange(0, len(slopeMap), down):
        if slopeMap[row][col] == '#':
            trees += 1
        col = (col + right) % mapCycle

    return trees

def main():
    trees = 1

    # Right : Down
    slopes = [ 
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]

    rawSlope = readInput(filename)

    # Clear '\n' at the end of the line
    slopeMap = [row.rstrip() for row in rawSlope]

    for slope in slopes:
        trees *= countTreesOnSlope(slopeMap, slope[0], slope[1])

    print 'Product of trees found for all cases is {}'.format(trees)

if __name__ == '__main__':
    os.chdir(filepath)
    main()