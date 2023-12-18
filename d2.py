import re

tester = {"red":12, 
          "green":13, 
          "blue":14
                    }

cubes = "red|green|blue"


#regex should match whitepsace digit whitespace word end of word boundary 
expression =  re.compile(r'\d\s(?:%s)\b' % cubes)

with open('d2_data.txt') as file:
    success_tracker = []
    for line in file:
        #Each set within a game
        sets = line.split(';') 
        print(sets)
        for cube in expression.findall(line):
            print(cube)

def checkPossibility(set):
    return