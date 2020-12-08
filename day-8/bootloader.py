import os
import sys
import string

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

def checkLoop(code):
    acc = 0
    rip = 0
    visited = [False] * len(code)

    while rip != (len(code) - 1):
        code[rip].rstrip()

        rax = code[rip].split()[0]
        operator = code[rip].split()[1][0]
        number = int(code[rip].split()[1][1:])

        visited[rip] = True

        if rax == 'jmp':
            if operator == '+':
                rip += number
            else:
                rip -= number
        elif rax == 'acc':
            if operator == '+':
                acc += number
            else:
                acc -= number
            rip += 1
        elif rax == 'nop':
            rip += 1

        if visited[rip]:
            return False, acc
    return True, acc

def compileBootAndFixLoop(code):
    for i in xrange(len(code)):
        try_code = code[:] # real copy in Python
        try_code[i].rstrip()

        rax = try_code[i].split()[0]
        if rax == 'jmp':
            try_code[i] = try_code[i].replace('jmp', 'nop')
        elif rax == 'nop':
            try_code[i] = try_code[i].replace('nop', 'jmp')
        else:
            continue
        
        ok, acc = checkLoop(try_code) 
        if ok:
            return 'Code fixed, acc is {}'.format(acc)
            
def main(task):
    code = readInput(filename)
    if task == 1:
        _, acc = checkLoop(code) 
        print acc
    else:
        print compileBootAndFixLoop(code)

if __name__ == '__main__':
    os.chdir(filepath)
    try:
        task = int(raw_input('Enter number of task to be solved for day 8 Advent of Code: '))
        if task != 1 and task != 2:
            print 'Nope, you have to provide me with either Task 1 or Task 2'
            sys.exit()

        main(task)        
    except ValueError:
        print 'Nope, you have to provide me with either Task 1 or Task 2'