import os
# parse table
parse_table = {
    ("E","("):["T","E'"],
    ("E","id"):["T","E'"],
    ("E'","+"):["+","T","E'"],
    ("E'",")"):["#"],
    ("E'","$"):["#"],
    ("T","("):["F","T'"],
    ("T","id"):["F","T'"],
    ("T'","+"):["#"],
    ("T'","*"):["*","F","T'"],
    ("T'",")"):["#"],
    ("T'","$"):["#"],
    ("F","("):["(","#",")"],
    ("F","id"):["id"],
}
# inputting string
string = input("Enter input string from chars [ id , + , * ] separating each char by white space : ").split(" ") + ["$"]
# creating stack
stack = ["E","$"]
# printing stack operations
print("STACK".center(15,' '),"INPUT".center(15,' '),"MATCHED".center(15,' '),"ACTION".center(15,' '))
print("".ljust(15,'-'),"".rjust(15,'-'),"".center(15,'-'),"".center(15,'-'))
print(" "*5+"".join(stack[::-1]).ljust(10,' '),"".join(string).rjust(12,' ')+" "*3,"".center(15,' '),"".center(15,' '))
while len(stack)>1:
# found a match
    if stack[0] == string[0]:
        x = stack[0]
        stack, string = stack[1:], string[1:]
        print(" "*5+"".join(stack[::-1]).ljust(10,' '),"".join(string).rjust(12,' ')+" "*3,x.center(15,' '),"Matched {0}".format(x).center(15,' '))
    else:
# checking for substitution
        try:
            x, y = stack[0], parse_table[(stack[0],string[0])]
            stack = parse_table[(stack[0],string[0])] + stack[1:]
            if stack[0] == '#':stack = stack[1:]
            print(" "*5+"".join(stack[::-1]).ljust(10,' '),"".join(string).rjust(12,' ')+" "*3,"".center(15,' '),"{0} -> {1}".format(x,"".join(y)).center(15,' '))
        except:
            os.system('clear')
            print("Given string cannot be parsed by this parser. String does not belong to this grammar ")
            break
