import os

def inpo(inp):
    with open('input.txt','w') as f:
        f.write(inp)

def clear():
    f = open("input.txt", "w")
    f.truncate()
    f.close()
