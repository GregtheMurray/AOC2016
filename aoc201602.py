
filename = 'aoc201603_input.txt'
f = open(filename,"r")

#Part 1
count = 0
prevmod = 0
for x in f.readlines():
     x = x.split()
     x = [int(i) for i in x]
     x.sort()
     if int(x[0]) + int(x[1]) > int(x[2]):

         count += 1


print(count)


#Part 2

part2counter = 0
# Put all grouping lists into a single list
raw_nums = [[int(s) for s in line.split()] for line in open(filename)]

masterlist = []

# get groupings of 3 for each positon iterating through raw_nums 3 lists at a time 
for i in range(0,len(raw_nums), 3):
    masterlist.append([raw_nums[i][0],raw_nums[i+1][0],raw_nums[i+2][0]])
    masterlist.append([raw_nums[i][1],raw_nums[i+1][1],raw_nums[i+2][1]])
    masterlist.append([raw_nums[i][2],raw_nums[i+1][2],raw_nums[i+2][2]])

for i in masterlist:
    i.sort()
    if i[0] + i[1] > i[2]:
        part2counter += 1

print(part2counter)
