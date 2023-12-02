import re
from collections import defaultdict

with open("test.txt") as fin:
    data = fin.readlines()

res = []
for gameid, line in enumerate(data):
    pattern = re.compile(r'Game \d*: ')
    line = re.sub(pattern, "", line)
    subsets = line.split(";")
    RGB = defaultdict(int)
    for subset in subsets:
        colors_pair = subset.split(",")
        for color in colors_pair:
            num_list = re.findall("\d", color)
            num = int("".join(num_list))
            color_list = re.findall("[^\d\s]", color)
            color = "".join(color_list)
            if num > RGB[color]:
                RGB[color] = num

    prod = 1
    for count in RGB.values():
        prod *= count

    res.append(prod)

print(sum(res))
