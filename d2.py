import re

tester = {"red":12, 
          "green":13, 
          "blue":14
                    }

cubes = "red|green|blue"


#regex should match whitepsace digit whitespace word end of word boundary 
expression =  re.compile(r'\d\s(?:%s)\b' % cubes)

games = []
with open('d2_data.txt') as file:
    success_tracker = []
    for line in file:
        game =[]
        sets = line.split(';') 
        for cube in expression.findall(line):
            colour = cube.split(" ")
            print(colour)
            if colour[1] == "red" and int(colour[0]) > 12:
                print(tester["red"])
            elif colour[1] == "green" and int(colour[0]) > 13:
                print("impossible")
            elif colour[1] == "blue" and int(colour[0]) > 14:
                print("impossible")



def checkPossibility(set):
    return