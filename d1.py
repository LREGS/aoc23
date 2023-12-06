import re
"""I think we can take each string and seperate it into str/ints and then 
just use the first and last element if len > 1 
"""

"""Could you have just gone through each string and took the first and last int with regex?"""
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


huh = []
for l in vals:
    for v in l:
        if v in d.keys():
            target = l.index(v)
            # print(l[target],v, target,d[v])
            l[target] = d[v]   

total = 0
for val in vals:

    if len(val) <= 1:
        code = (str(val[0]) + str(val[0]))
        total = total + int(code)

    else:
        code = (str(val[0]) + str(val[-1]))
        total = total + int(code)
print(total)
    
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