infix = input("Enter infix expression : ").replace(' ','')
result = input("Enter resultant variable : ")
temp,string,operators = {},[],['+','-','*','/']
count,cp = 1,0

for i in range(len(infix)):
    if infix[i] in operators:
        string.append(infix[cp:i])
        string.append(infix[i])
        cp = i+1

string.append(infix[cp:])

for i in range(len(string)):
    if '[' in string[i]:

        temp['t'+str(count)] = ('*',string[i][string[i].index('[')+1],'8')
        count += 1
        temp['t'+str(count)] = ('[]',string[i][:string[i].index('[')],'t'+str(count-1))
        string[i] = 't'+str(count)
        count += 1


while len(string)!=1:

    temp['t'+str(count)] = (string[1],string[0],string[2])
    string = string[3:]
    string = ['t'+str(count)] + string
    count += 1

print('\n','THREE ADDRESS CODES'.center(15,' '))
for k,v in temp.items():
    if v[0]!='[]':
        print(k.center(3,' '),'='.center(3,' '),v[1].center(3,' '),v[0].center(3,' '),v[2])
    else :
        print(k.center(3,' '),'='.center(3,' '),v[1].center(3,' '),'['+v[2]+']')
print(result.center(3,' '), '='.center(3,' '), 't{0}'.format(count-1).center(3,' '))

temp[result] = ('=','t'+str(count-1),'---')
print("\n","QUADRUPLE TABLE".center(20,' '))
print('op'.center(3,' '),'arg1'.center(5,' '),'arg2'.center(5,' '),'result'.center(7,' '))
for k,v in temp.items(): print(v[0].center(3,' '),v[1].center(5,' '),v[2].center(5,' '),k.center(7,' '))
