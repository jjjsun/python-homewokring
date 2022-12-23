import math

with open("MP09Data1.txt") as f:
    line = f.readline()
    line = line[:]
with open("MP09Data2.txt") as f:
    line = f.readline()
    line = line[:]
line = str(line)
line.sort(reverse=True)
print("\nc.sort(reverse=True)")
print(line)
