file = open('fig2_1.asm')
instructions, symbols, symbol_table = [],{},{}
for line in file.readlines():
    if line[0]!='.':
        line = line.replace('\n','').split(' ')
        instructions.append(list(filter(lambda x : x!='', line)))
        if len(instructions[-1]) == 3: symbols[instructions[-1][0]] = False
variable = {'WORD':3,'BYTE':1}
buffer = {'RESB':1,'RESW':3}
for instruction in instructions:
    if len(instruction) == 1:continue
    elif len(instruction) == 2:
        if symbols[instruction[1]]:continue
        else:symbol_table[instruction[1]] = [instruction[1],None,None]
    else:
        if symbols[instruction[0]]:continue
        else:
            if instruction[1] in variable.keys(): symbol_table[instruction[0]] = [instruction[0],variable[instruction[1]],instruction[2]]
            elif instruction[1] in buffer.keys(): symbol_table[instruction[0]] = [instruction[0],buffer[instruction[1]]*int(instruction[2]),'--']
            else: symbol_table[instruction[0]] = [instruction[0],3,'--']
            symbols[instruction[0]] = True
            if instruction[2] in symbols.keys() and symbols[instruction[2]]==False: symbol_table[instruction[2]] = [instruction[2],None,None]
for symbol in symbol_table.values():
    print("{0}".format(symbol[0]).ljust(10),"{0}".format(symbol[1]).ljust(5),"{0}".format(symbol[2]).ljust(5))
