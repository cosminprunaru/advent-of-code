import os
import sys
import math

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

def checkTicket(ticket):
    minRow, minCol = 0, 0
    maxRow, maxCol = 127, 7

    for letter in ticket:
        if letter == 'F':
            maxRow = int((minRow + maxRow + 1) / 2) - 1
        elif letter == 'B':
            minRow = int((minRow + maxRow + 1) / 2)
        elif letter == 'R':
            minCol = int((minCol + maxCol + 1) / 2)
        elif letter == 'L':
            maxCol = int((minCol + maxCol + 1) / 2) - 1

    return minRow * 8 + minCol

def getSeatByGauss(seats):
    minSeat = seats[0] - 1
    maxSeat = seats[-1]
    gaussFront = minSeat * (minSeat + 1) / 2
    gaussTotal = maxSeat * (maxSeat + 1) / 2
    return gaussTotal - sum(seats) - gaussFront


def checkAllTickets(tickets):
    seats = []
    for ticket in tickets:
        seats.append(checkTicket(ticket.rstrip()))

    seats.sort()
    print 'Max seat ID is {}'.format(seats[-1])

    print 'My seat is {}'.format(getSeatByGauss(seats))

def main():
    tickets = readInput(filename)
    checkAllTickets(tickets)    

if __name__ == '__main__':
    os.chdir(filepath)
    main()