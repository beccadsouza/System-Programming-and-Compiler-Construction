postfix = input("Enter postfix expression : ").replace(' ','')
result = input("Enter resultant variable : ")
temp,string,stack,operators = {},[],[_ for _ in postfix],['+','-','*','/']
count = 1
while len(stack)!=0:
    if stack[0] in operators:
        temp['t'+str(count)] = (stack[0],string[0],string[1])
        stack[0] = 't'+str(count)
        string = []
        count += 1
    else:
        string.append(stack[0])
        stack = stack[1:]

print('\n','THREE ADDRESS CODES'.center(15,' '))
for k,v in temp.items(): print(k.center(3,' '),'='.center(3,' '),v[1].center(3,' '),v[0].center(3,' '),v[2].center(3,' '))
print(result.center(3,' '), '='.center(3,' '), 't{0}'.format(count-1).center(3,' '))


temp[result] = ('=','t'+str(count-1),'---')
print("\n","QUADRUPLE TABLE".center(20,' '))
print('op'.center(3,' '),'arg1'.center(5,' '),'arg2'.center(5,' '),'result'.center(7,' '))
for k,v in temp.items(): print(v[0].center(3,' '),v[1].center(5,' '),v[2].center(5,' '),k.center(7,' '))
