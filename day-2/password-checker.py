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

def isPasswordValid(constraints, letter, password, task):
    if task == 1:
        return validateLetterOccurence(constraints, letter, password)
    else:
        return validatePositions(constraints, letter, password)

# Letter occurence in password min-max times
def validateLetterOccurence(min_max_occ, letter, password):
    occ = password.count(letter)
    min_occ = int(min_max_occ[0])
    max_occ = int(min_max_occ[1])

    if occ >= min_occ and occ <= max_occ:
        return True
    return False

# Letter positons are fixed, indexing starting at 1, exactly one occurence on one of the positions
def validatePositions(positions, letter, password):
    l1 = password[int(positions[0]) - 1]
    l2 = password[int(positions[1]) - 1]

    if (l1 == letter and l2 != letter) or (l1 != letter and l2 == letter):
        return True
    return False

def main(task):
    validPasswords = 0

    data = readInput(filename)

    for line in data:
        info = line.split()

        # Gather requiered data
        min_max_occ = info[0].split('-')
        letter = info[1][:-1]
        password = info[2]

        if isPasswordValid(min_max_occ, letter, password, task):
            validPasswords += 1

    print "Valid passwords: {}".format(validPasswords)

if __name__ == '__main__':
    os.chdir(filepath)
    
    try:
        task = int(raw_input("Enter number of task to be solved for day 2 Advent of Code: "))
        if task != 1 and task != 2:
            print("Nope, you have to provide me with either Task 1 or Task 2")
            sys.exit()

        main(task)
    except ValueError:
        print("Nope, you have to provide me with either Task 1 or Task 2")