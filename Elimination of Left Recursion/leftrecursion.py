# Created by Rebecca D'souza on 7-2-19
grammar,grammar2 = {},{}
while True:
	n = int(input("[1] Add a non terminal. [2] Add a production rule. [3] Check for left recursion\n"))
	if n == 1:
		nonterminal = input("Enter a non terminal : ")
		grammar[nonterminal] = []
	if n == 2:
		try :
			nonterminal = input("Enter the non terminal  : ")
			production = input("Enter the production : ")
			grammar[nonterminal].append(production)
		except KeyError:print("Non Terminal isn't present in the grammar\n")
	if n == 3:break
print("Entered grammar : ")
for k,v in grammar.items():	print(k," -> "," | ".join(v),"\n")
# Remove indirect left recursion by substitution
visited, temp = [],[]
for k,v in grammar.items():
	old = v
	while True:
		temp = []
		for val in grammar[k]:
			if val[0] in visited:temp += [x+val[1:] for x in grammar[val[0]]]
			else: temp.append(val)
		if all([False if x[0] in visited else True for x in temp]) or any([True if x[0]==k else False for x in temp]):
			grammar[k] = temp
			break
		grammar[k] = temp
	if not any([True if x[0]==k else False for x in grammar[k]]): grammar[k] = old
	visited.append(k)
print("Substituted grammar : ")
for k,v in grammar.items():	print(k," -> "," | ".join(v),"\n")
# Remove direct left recursion
for k in grammar.keys():
	present = False
	for v in grammar[k]:
		if v[0] == k:
			print("Left recursion present in production of {0}".format(k))
			present = True
			break
	if present:
		temp, grammar2[k+"\'"] = [],[]
		for v in grammar[k]:
			if v[0]==k:grammar2[k+"\'"].append(v[1:]+k+"\'")
			else:temp.append(v+k+"\'")
		grammar2[k+"\'"].append("E")
		grammar[k] = temp
print("Grammar after elimination of recursion : ")
for k,v in {**grammar,**grammar2}.items():print(k," -> "," | ".join(v),"\n")
