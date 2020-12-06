import os
import re
import sys

filepath = os.path.dirname(os.path.abspath(__file__)) 
filename = r'puzzle-input.txt'

reqFields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

def validateYear(value, lower, upper):
    if len(value) != 4:
        return False

    try:
        if lower <= int(value) <= upper:
            return True
        else:
            return False
    except:
        return False

def validateBirthYear(value):
    return validateYear(value, 1920, 2002)

def validateIssueYear(value):
    return validateYear(value, 2010, 2020)

def validateExpirationYear(value):
    return validateYear(value, 2020, 2030)

def validateHeight(value):
    unit = value[-2:]
    if unit != 'cm' and unit != 'in':
        return False

    try:
        height = int(value[:-2])
        if unit == 'cm':
            return 150 <= height <= 193
        else: # inches
            return 59 <= height <= 76
    except:
        return False

def validateHairColor(value):
    return False if re.search(r'^\#[0-9a-f]{6}$', value) is None else True

def validateEyeColor(value):
    validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if value in validEyeColors:
        return True
    return False

def validatePassportID(value):
    return False if re.match(r'^\d{9}$', value) is None else True

def validateField(key, value):
    if key == 'byr':
        return validateBirthYear(value)
    elif key == 'iyr':
        return validateIssueYear(value)
    elif key == 'eyr':
        return validateExpirationYear(value)
    elif key == 'hgt':
        return validateHeight(value)
    elif key == 'hcl':
        return validateHairColor(value)
    elif key == 'ecl':
        return validateEyeColor(value)
    elif key == 'pid':
        return validatePassportID(value)
    elif key == 'cid':
        return False # optional
    else:
        print 'Unknown key provided: {}'.format(key)
        return False

def readInput(filename):
    # Check the existence of input
    if os.path.isfile(filename):
        f = open(filename, 'r')
        return f.readlines()
    else:
        print 'File {} not found'.format(filename)
        sys.exit()

def checkPassportsDummy(passports):
    validFields = 0
    validPassports = 0
    for line in passports:
        for reqF in reqFields:
            if reqF in line:
                validFields += 1
        
        # Finished lines for a passport, time to check validity and reset
        # 
        # Also, check the last line, as '\n' stop condition is not enough
        if line == '\n' or line == passports[-1]:
            if validFields == 7:
                validPassports += 1
            validFields = 0

    print "Valid passports: {}".format(validPassports)

def checkPassports(passports):
    validFields = 0
    validPassports = 0
    for line in passports:
        values = line.split()
        for value in values:
            field = value.split(':')
            if validateField(field[0], field[1]):
                validFields += 1
   
        # Finished lines for a passport, time to check validity and reset
        # 
        # Also, check the last line, as '\n' stop condition is not enough
        if line == '\n' or line == passports[-1]:
            if validFields == 7:
                validPassports += 1
            validFields = 0

    print "Valid passports: {}".format(validPassports)

def main():
    passports = readInput(filename)
    #checkPassportsDummy(passports)    
    checkPassports(passports)    

if __name__ == '__main__':
    os.chdir(filepath)
    main()