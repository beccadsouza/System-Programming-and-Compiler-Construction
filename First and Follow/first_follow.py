from collections import defaultdict
grammar, grammar2, first, follow, visited, epsi = {}, defaultdict(list), defaultdict(list), defaultdict(list), [], []
while True:
	n = int(input("[1] Add a non terminal. [2] Add a production rule. [3] Compute First & Follow\n"))
	if n == 1:
		nonterminal = input("Enter a non terminal : ")
		grammar[nonterminal] = []
	if n == 2:
		try:
			nonterminal = input("Enter the non terminal  : ")
			production_ = input("Enter the production : ")
			grammar[nonterminal].append(production_)
		except KeyError:
			print("Non Terminal isn't present in the grammar\n")
	if n == 3: break
for k, v in grammar.items(): print(k, " -> ", " | ".join(v), "\n")
original = dict(grammar)
def get_first_of( nt, temp ):
	if nt in visited:temp += first[nt]
	else:[get_first(x, temp) for x in grammar[nt]]
def get_first( production, temp ):
	if production[0] in grammar.keys():get_first_of(production[0], temp)
	elif production[0] == 'E':temp.append("E")
	else:temp.append(production[0])
def refine( epsil, produc ):
	perm = ["0" * (len("0" * sum([1 for i in produc if i in epsil])) - len("{0:b}".format(i))) + "{0:b}".format(i) for i
			in range(sum([1 for i in produc if i in epsil]) + 1)]
	temp = []
	if produc != 'E':
		for x in perm:
			t, ind = "", 0
			for ch in produc:
				if ch not in epsil:t += ch
				else:
					if x[ind] == '1': t += ch
					ind += 1
			if len(t) != 0:temp.append(t)
			else:temp.append('E')
	return temp
[epsi.append(k) for k, v in grammar.items() if "E" in v]
repeat = True
while repeat:
	repeat = False
	for k, v in grammar.items():
		for q in v:
			grammar2[k] += refine(epsi, q)
			if 'E' in grammar2[k] and 'E' not in v:
				epsi.append(k)
				repeat = True
		grammar[k] += grammar2[k]
		grammar[k] = list(set(grammar[k]))
for k, v in grammar.items():
	[get_first(x, first[k]) for x in v]
	if 'E' not in v:first[k] = set(filter(lambda a: a != 'E', first[k]))
	else:first[k] = set(first[k])
	visited.append(k)
print("First Sets : ")
for k, v in first.items(): print("First({0})".format(k), " : {", ", ".join(set(v)), "}", "\n")
epsi, productions = list(set(epsi)), list(grammar.keys())
follow[productions[0]] = ['$']
for x in productions:
	for k, v in original.items():
		for value in v:
			if x in value:
				if value.index(x) == len(value) - 1:follow[x] += follow[k]
				else:
					reb = []
					[reb.append(get_first(q, reb)) for q in refine(epsi, value[value.index(x) + 1:])]
					reb = list(set(reb))
					reb.remove(None)
					if 'E' in reb:
						follow[x] += follow[k]
						reb.remove('E')
					follow[x] += reb
print("Follow Sets : ")
for k, v in follow.items(): print("Follow({0})".format(k), " : {", ", ".join(set(v)), "}", "\n")
