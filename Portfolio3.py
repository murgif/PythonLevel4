#!/usr/bin/env python3

from sys import argv

import random

def student_id(line_1):
    return line_1[:8]


def surname(line_1):
    return line_1[9:].split(',')[0]


def filter(line):
    filtered = ''.join(char for char in line if char.isalpha())
    return filtered

def firstname(line_1):
    return [l[0] for l in line_1.split()][2:]

def domain(domain = "poppleton.ac.uk"):
    return '@' + domain

if __name__ == '__main__':
    try:
        if len(argv) == 1:
            print("Error: Missing command line argument")
        else:
            with open(argv[1], 'r') as input, open(argv[2], "w") as output:
                for line in input.readlines():
                    x = random.randint(1000, 9999)
                    first_name = '.'.join(map(str, firstname(line))) + '.'
                    a = [first_name.lower(), (filter(surname(line)).lower()), x, (domain())]
                    b = ''.join(map(str, a))
                    d = (student_id(line), b)
                    output.write(d[0] + " " + d[1] + "\n")
    except FileNotFoundError:
        print(f"Error cannot open \"{argv[1]}\", sorry about that")



