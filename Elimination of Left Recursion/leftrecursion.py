grammar,grammar2,visited = {},{},[]
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
for k,v in grammar.items():	print(k," -> "," | ".join(v),"\n")
for k in grammar.keys():
	while True:
		temp = []
		for v in grammar[k]:
			if v[0] in visited:temp += [x+v[1:] for x in grammar[v[0]]]
			else: temp.append(v)
		if all([False if x[0] in visited else True for x in temp]):
			grammar[k] = temp
			break
		grammar[k] = temp
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
	visited.append(k)
print("Grammar after elimination of recursion : ")
for k,v in {**grammar,**grammar2}.items():print(k," -> "," | ".join(v),"\n")
