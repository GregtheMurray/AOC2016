# 117 is too High
import re
filename = 'aoc201607_input.txt'
# filename = 'testinput.txt'
f = open(filename,"r")

#read lines into one string
data = [x.strip() for x in f.readlines()]
# print(data)
Total = 0
part2Total = 0
for i in data:
    # part2check = len(re.findall(r'.*(\w)(\w)(\1).*\[.*\2\1\2.*\].*',i)) + len(re.findall(r'.*\[.*(\w)(\w)(\1).*\].*\2\1\2.*',i))
    i = re.split('[\[|\]]',i)
    TLS = 0
    NotTLS = 0
    for j in list(enumerate(i)):
        check1 = re.findall(r'.*(\w)(\w)\2\1.*',j[1])
        check2 = re.findall(r'.*(\w)\1{3}.*',j[1])
        # if len(check2) == 1:
        #     print(len(check1),len(check2), j)
        if j[0] % 2 == 0:
            if len(check1) > 0:
                TLS += 1
            elif len(check2) > 0:
                NotTLS += 1
        if j[0] % 2 == 1:
            if len(check1) > 0:
                NotTLS += 1
    if TLS == 1 and NotTLS == 0:
        Total += 1
        # print(TLS, NotTLS, i)
print(Total)
