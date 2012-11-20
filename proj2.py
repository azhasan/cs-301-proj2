import sys
import itertools

def printT(t):
    for a in sorted(t):
        print a,t.get(a),"\n"

def parseIn():
    table = {}
    a = open('input.txt')
    x = map(float,a.readline().split())
    fx = map(float,a.readline().split())
    table = dict(itertools.izip(x,fx))
    printT(table)

        

if __name__ == '__main__':
    parseIn()
