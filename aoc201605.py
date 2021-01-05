import hashlib
import re

testinput = 'abc'
input = 'cxdnnyjw'

def part1solve(input):
    counter = 1
    password = ''
    while len(password) < 8:
        index = input + str(counter)
        hash = hashlib.md5(index.encode())
        hash = hash.hexdigest()

        if hash[:5] =='00000':
            password += hash[5]
            print(counter, password, hash)
        counter += 1
    return password

# print(part1solve(input))


# def part2solve(input):
counter = 1
password = ''
dict = {}
while len(dict) < 8:
    index = input + str(counter)
    hash = hashlib.md5(index.encode())
    hash = hash.hexdigest()

    if hash[:5] =='00000' and isinstance(hash[5],int) and hash[5] not in dict:
        dict[int(hash[5])] = hash[6]
        print(counter, password, hash)
    if counter % 10000 == 0:
        print(counter)
    counter += 1
    # return password
