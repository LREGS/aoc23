import re

nums = "one|two|three|four|five|six|seven|eight|nine"
nums_re = re.compile((r'(?=(\d|%s))'% nums))
nums = nums.split('|')

with open('d1_data.txt') as file:

    total = 0
    for line in file:
        print(line)
        digits = []
        for num in nums_re.findall(line):
            if num in nums:
                num = str(nums.index(num) + 1)
            digits.append(num)
        total += int(digits[0] + digits[-1])
    print(total)
