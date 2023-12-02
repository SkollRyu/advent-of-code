import re

with open("test.txt") as fin:
    data = fin.readlines()

res = 0
checker = {"red": 12, "blue": 14, "green": 13}
for gameid, line in enumerate(data):
    pattern = re.compile(r'Game \d*: ')
    line = re.sub(pattern, "", line)
    subsets = line.split(";")
    isValid = True
    for subset in subsets:
        colors_pair = subset.split(",")
        for color in colors_pair:
            num_list = re.findall("\d", color)
            num = int("".join(num_list))
            color_list = re.findall("[^\d\s]", color)
            color = "".join(color_list)
            if num > checker[color]:
                isValid = False
    if isValid:
        res += gameid+1

print(res)
