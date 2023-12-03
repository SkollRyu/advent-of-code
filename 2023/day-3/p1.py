with open("test.txt") as f:
    data = f.read()
    lines = data.strip().split("\n")

r = len(lines)
c = len(lines[0])

def isSymbol(x,y):
    if not (0 <= x < r and 0 <= y < c):
        return False

    return lines[x][y] != "." and not lines[x][y].isdigit()

res = 0

for i, line in enumerate(lines):
    # look for number from left to right
    start = 0 
    j = 0
    while j < c:
        start = j
        num = ""
        while j < c and line[j].isdigit():
            num += line[j]
            j += 1

        # move to next j, until find the digit
        if num == "":
            j += 1
            continue

        num = int(num)

        # left and right of the number
        if isSymbol(i, start-1) or isSymbol(i,j):
            res += num
            continue

        # top and botton five
        for k in range(start-1, j+1):
            if isSymbol(i-1, k) or isSymbol(i+1, k):
                res += num
                break
print(res)
        
