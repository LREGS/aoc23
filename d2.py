import re

tester = {"red":12, 
          "green":13, 
          "blue":14
                    }

cubes = "red|green|blue"


#regex should match whitepsace digit whitespace word end of word boundary 
expression =  re.compile(r'(\d+)\s+(%s)' % cubes)

games = []
with open('d2_data.txt') as file:
    success_tracker = []
    for line in file:
        m = {"red":0,"green":0,"blue":0}
        for quantity, colour in expression.findall(line):
            quantity = int(quantity)
            

            if quantity > m[colour]:
                m[colour] = quantity 

        games.append(m)

#use list comprehensions more plsssssssssssssssssssssssssssssssssssssssss
vals = []
def powerCubes(cubes):
    for cube in cubes:
        tm = []
        for value in cube.values():
            tm.append(value)
        vals.append(tm)

powerCubes(games)

toSum = []
def totals(val):
    for val in vals:
        result = 1
        for v in val:
            print(v)
            result = result * v

        toSum.append(result)

totals(vals)
print(toSum)
print(sum(toSum))

# print(vals)
# print(games)
possibleGames = []
for index, game in enumerate(games):
    if "impossible" not in game:
        possibleGames.append(index + 1)

# print(possibleGames)

# print(sum(possibleGames))

            
