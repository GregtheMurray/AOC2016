
from collections import Counter
import operator
filename = 'aoc201606_input.txt'
# filename = 'testinput.txt'
f = open(filename,"r")

#read lines into one string
data = f.read().replace('\n','')

def solveday06(data,range_,minmax = 0):
    output = ''
    # loop for length of the substring/password
    for i in range(range_):
        chars = ''
        #loop through each character in string
        for e in list(enumerate(data)):
            # keep the nth (range loop) postion for each password
            if e[0] % range_ == i:
                chars += e[1]
        #count character instances
        count = Counter(chars)
        #get min or max instance based on input
        if minmax == 1:
            letter = min(count.items(), key=operator.itemgetter(1))[0]
        else:
            letter = max(count.items(), key=operator.itemgetter(1))[0]
        output += letter
    return output
print(solveday06(data,8))
print(solveday06(data,8,1))
