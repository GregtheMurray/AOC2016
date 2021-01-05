
from collections import Counter
import re
filename = 'aoc201604_input.txt'
f = open(filename,"r")

data = [x.strip() for x in f.readlines()]
#Part 1
total = 0

for i in data:
    i = re.match(r'([a-z-]+)(\d+)\[([a-z]+)\]',i)
    lettercount = Counter(i.group(1).replace('-',''))

    #sorts ascending by dict value (hence the negative to return descending) then dict key
    sortlist = [v[0] for v in sorted(lettercount.items(), key= lambda kv: (-kv[1], kv[0]))]
    checksum = ''.join(sortlist[:5])
    #print(checksum,i.group(3),i.group(2))

    output = ''
    if checksum == i.group(3):
        total += int(i.group(2))
    #Part 2
        move = (int(i.group(2)) % 26)
        for letter in i.group(1):
            if letter == '-':
                output += ' '
            else:
                code = ord(letter)
                # 0X61 is hex and returns an int value for the position of the letter in ascii
                # code - 0x61 nomralizes the character position
                # + move, accounts for the move
                # mod 26 accounts for moves that result in a wrap/ go over the top
                # + 0x61 positions letter back into the a-z range
                newcode = ((code - 0x61 + move) % 26) + 0x61
                newcode = chr(newcode)
                output += newcode

        if re.search('[Nn]orth',output):
            print(output, i.group(2))
print(total)
