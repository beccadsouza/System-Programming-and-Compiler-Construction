file = open('assembly.c', 'r')
lines = file.readlines()
instructions = []

for line in lines:
    line = line.replace('\n', '').split(' ')
    if '' in line:
        line = list(filter(lambda x: x != '', line))
    # print(line)
    instructions.append(line)

MNT = {}
MDT = {}
ALA = {}

index_count = 0
keep_track = False

for instruction in instructions:
    if len(instruction) == 3:
        if instruction[1] == 'MACRO':
            MNT[instruction[0]] = index_count
            ALA[instruction[0]] = instruction[2]
            keep_track = True
        else:
            keep_track = False
    elif len(instruction) == 2:
        if keep_track:
            MDT[index_count] = instruction[0]+' '+instruction[1]
            index_count += 1
    else:
        if keep_track and instruction[0] == 'MEND':
            MDT[index_count] = instruction[0]
            index_count += 1
            keep_track = False

for k, v in MNT.items(): print(k, v)
for k, v in MDT.items(): print(k, v)
for k, v in ALA.items(): print(k, v)
