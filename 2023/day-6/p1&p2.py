import math

with open("test.txt") as f:
    data = f.read()
    lines = data.strip().split("\n")

times = None
distance = None
times = lines[0].split()
distances = lines[1].split()

print(times, distance)

def isBetter(secondsToHold, time, distance):
    if (time - secondsToHold) * secondsToHold > distance:
        return True

res = []

for i in range(len(times)):
    time = int(times[i])
    distance = int(distances[i])
    # find the lowest and highest possible
    # lowest = first F the possible
    # highest = first F the impossible
    l, r = 0, time - 1

    # lowest 
    while l < r:
        mid = (l+r) // 2
        if isBetter(mid, time, distance):
            r = mid
        else:
            l = mid + 1

    lowest = l

    l, r = 0, time - 1
    
    # highest 
    while l < r:
        mid = (l+r) // 2
        if isBetter(mid, time, distance):
            l = mid + 1
        else:
            r = mid

    highest = l - 1

    res.append((highest - lowest + 1))
    
print(math.prod(res))
