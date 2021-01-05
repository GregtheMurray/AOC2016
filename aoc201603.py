
filename = 'aoc201602_input.txt'

f = open(filename,"r")
data = [data.strip() for data in f.readlines()]
print(data)

# Pad for Part 1
# 123
# 456
# 789

# Pad Dictionary
pad = {(0,0):"7", (0,1):"4", (0,2):"1", (1,0):"8", (1,1):"5", (1,2):"2", (2,0):"9", (2,1):"6", (2,2):"3"}

output =''

x = 1
y = 1

for line in data:

    for op in line:
        if op == 'R' and x < 2:
            x += 1
        elif op == 'L' and x > 0:
            x -= 1
        elif op == 'U' and y < 2:
            y += 1
        elif op == 'D' and y > 0:
            y-= 1
    coord = (x,y)
    print(coord,pad.get(coord))
    output += str(pad.get(coord))
print(output)



#  1
# 234
#56789
# ABC
#  D

sampledata = """ULL
RRDDD
LURDL
UUUUD"""

sample = sampledata.splitlines()

newpad = {(2,0):"D",(1,1):"A",(2,1):"B",(3,1):"C",(0,2):"5",(1,2):"6",(2,2):"7",(3,2):"8",(4,2):"9",(1,3):"2",(2,3):"3",(3,3):"4",(2,4):"1"}

x = 0
y = 2
code = ""
for i in data:
    for letter in i:
        newx = x
        newy = y
        if letter == 'R':
            newx += 1
        elif letter == 'L':
            newx -= 1
        elif letter == 'U':
            newy += 1
        elif letter == 'D':
            newy -= 1
        newxy = (newx,newy)
        if newpad.get(newxy) != None:
            x = newx
            y = newy
    code += newpad.get((x,y))
print(code)
