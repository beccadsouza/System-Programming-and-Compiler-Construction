from collections import defaultdict
grammar,grammar2,first,visited,epsi = {'S':['ABc','d'],'A':['a','E'],'B':['b','E']},defaultdict(list),defaultdict(list),[],[]
for k,v in grammar.items():print(k," -> "," | ".join(v),"\n")
def get_first_of(nt,temp):
	if nt in visited:temp += first[nt]
	else:[get_first(x,temp) for x in grammar[nt]]
def get_first(production,temp):
	if production[0] in grammar.keys(): get_first_of(production[0],temp)
	elif production[0]=='E': temp.append("E")
	else: temp.append(production[0])
def refine(epsil,produc):
	perm = ["0"*(len("0"*sum([1 for i in produc if i in epsil]))-len("{0:b}".format(i))) + "{0:b}".format(i) for i in range(sum([1 for i in produc if i in epsil])+1)]
	temp = []
	for x in perm:
		t,ind = "",0
		for ch in produc:
			if ch not in epsil:t+=ch
			else:
				if x[ind]=='1':t+= ch
				ind += 1
		temp.append(t)
	return temp
[epsi.append(k) for k,v in grammar.items() if "E" in v]
for k,v in grammar.items():
	for q in v: grammar2[k] += refine(epsi,q)
	grammar[k] += grammar2[k]
for k,v in grammar.items():
	[get_first(x,first[k]) for x in v]
	if 'E' not in v: first[k] = set(filter(lambda a: a != 'E', first[k]))
	visited.append(k)
for k,v in first.items():print("First({0})".format(k)," : {",", ".join(set(v)),"}","\n")
