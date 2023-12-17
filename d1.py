import re


with open('d1_data.txt') as file:
    data = file.read()
    allCodes = data.split('\n')

# numbers = ["one", "two", "three", "four", "five", "six", "sever", "eight", "nine"]

# I want to evaluate against a dictionary, and replace the values with numbers if they're in keys 
d ={
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

seperatedCodes = [code for code in allCodes]

values = [code for code in seperatedCodes]

vals =[]
for code in values:
    nums = re.findall("one|1|two|2|three|3|four|4|five|5|six|6|seven|7|eight|8|nine|9", code)
    vals.append(nums)
"""maybe use slice and not regex - maybe like a for loop going over each char, and splitting it each time a
and adding it into a list - and then checking that list each iteration to see if the word has appeared or not 
so it would be lke o on one oner etc and you would get true for one. 

Still not sure if this fixes the oneight sitation though. 

Basically slice the string from the begining until a word or int it found, then once either a matching expression is found
or after an int is found then search the back of the string"""

# for val in values:
#     for i in range(len(val)):
#         first = slice(0,i)
#         print(val[first])
#         if val[first].isdigit():
#             print(val[first])
#             break
#         if val[first] in d.keys():
#             print(val[first])
#             break
#         else:
#             print('nothing')

for val in values:
    for key in d.keys():
        if key in val:
            print(val.index(key), key)

#maybe I need to slice at the number - so does the string before the number contain the string of one of the keys?
#or does the string after the number contain letters - but then what if there is two strings before?

# for l in vals:
#     for v in l:
#         if v in d.keys():
#             target = l.index(v)
#             # print(l[target],v, target,d[v])
#             l[target] = d[v]   

# total = 0
# for val in vals:

#     if len(val) <= 1:
#         code = (str(val[0]) + str(val[0]))
#         total = total + int(code)

#     else:
#         code = (str(val[0]) + str(val[-1]))
#         total = total + int(code)
    
#     if len(val) <= 1:
#         code = (str(val[0]) + str(val[0]))
#         total = total + int(code)
#     else:
#         code = str((val[0]) + str(val[-1]))
#         total = total + int(code)
# print(total)


             # for v in l:
    #     if v in d.keys():
    #         ti = l.index(v)
    #         indexs.append(ti)
    #         print(l,ti)
    #         l[ti] = d[v]
    #         # print(l[ti])
    #         # print(c[v])
    #         continue



# print(indexs)




# all_digits =[]
# for code in codes:
#     digits = []
#     for char in code:
#         if char.isdigit():
#             digits.append(char)
            
#     all_digits.append(digits)
# print(all_digits)


# total = 0
# for val in vals:

#     if len(val) <= 1:
#         code = str(val[0]) + str(val[0])
#         total = total + int(code)
#     else:
#         code = str((val[0]) + str(val[-1]))
#         total = total + int(code)