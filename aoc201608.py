import re
import operator

filename = 'aoc201608_input.txt'
# filename = 'testinput.txt'
f = open(filename,"r")

#read lines into one string
data = [x.strip() for x in f.readlines()]

# build rectangles or initital grid
def buildrect(x,y,lightson = 0):
    grid = {}
    state = ''
    if lightson == 1:
        state = '#'
    else:
        state = '.'
    for i in range(x):
        for j in range(y):
            grid[(i,j)] = state
    return grid

# return the current grid
def curgrid(dict,linelength):
    lightkeys = sorted(dict,key = operator.itemgetter(1,0))
    lightgrid = ''
    for key in lightkeys:
        if key in lights:
            lightgrid += lights[key]
    regex = "(.{" + str(linelength) + "})"
    output = re.sub(regex,"\\1\n",lightgrid, re.DOTALL)
    return output

# set grid size
x = 50
y = 6

# build initital grid
lights = buildrect(x,y)

#loop through instructions
for i in data:
    rect = re.match(r'(rect)\s(\d+)x(\d+)',i)
    rotate = re.match(r'(rotate.*)\s[x|y]=(\d+)\sby\s(\d+)',i)

    if rect is None:
        op = rotate
    else:
        op = rect
    #handle rectangle instructions
    if op.group(1) =='rect':
        newrect = buildrect(int(rect.group(2)),int(rect.group(3)),1)
        lights.update(newrect)
    #handle rot column instructions
    elif op.group(1) == 'rotate column':
        newgrid = {}
        # loop through light keys
        for key in lights:
            matchval = '\(' + op.group(2) + '\,\s\d+\)'
            # if key x matches instruction x then create shifted key/value
            if re.match(matchval,str(key)):
                newy = (key[1] + int(op.group(3))) % y
                newgrid[(key[0],newy)] = lights[key]
        lights.update(newgrid)

    elif op.group(1) == 'rotate row':
        newgrid = {}
        # loop through light keys
        for key in lights:
            matchval = '\(\d+\,\s' + op.group(2) + '\)'
            # if key x matches instruction x then create shifted key/value
            if re.match(matchval,str(key)):
                newx = (key[0] + int(op.group(3))) % x
                newgrid[(newx,key[1])] = lights[key]
        lights.update(newgrid)

    # print(i)
    # print(curgrid(lights,x))

#part1
print(len(re.findall('#',curgrid(lights,x))))
#part2
print(curgrid(lights,x))
