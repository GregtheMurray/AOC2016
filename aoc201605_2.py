import hashlib
import re

testinput = 'abc'
input = 'cxdnnyjw'

# def part2solve(input):
counter = 1
dict = {}
while len(dict) < 8:
    index = testinput + str(counter)
    hash = hashlib.md5(index.encode())
    hash = hash.hexdigest()

    if hash[:5] =='00000' and re.match(r'[01234567]',hash[5]) and str(hash[5]) not in dict:
            dict[str(hash[5])] = hash[6]
            print(counter, hash, dict)
    if counter % 10000 == 0:
        print(counter)
    counter += 1
        # return password
