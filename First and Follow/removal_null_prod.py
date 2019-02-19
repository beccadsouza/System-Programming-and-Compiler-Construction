grammar = {'S':['ABAc'],'A':['a','E'],'B':['b','E']}
grammar2 = {}
epsi = []

def refine(epsil,produc):
	count = sum([1 for i in produc if i in epsil])
	maxl = len("0"*count)
	perm = ["0"*(maxl-len("{0:b}".format(i))) + "{0:b}".format(i) for i in range(count+1)]
	
	temp = []
	
	for x in perm:
		t = ""
		ind = 0
		
		for ch in produc:
			if ch not in epsil:t+=ch
			else:
				if x[ind]=='1':
					t+= ch
				ind += 1
		temp.append(t)
	return temp
					
		
for k,v in grammar.items():
	if "E" in v:
		epsi.append(k)


for k,v in grammar.items():
	grammar2[k] = []
	for q in v:
		grammar2[k] += refine(epsi,q)

for k in grammar2:
	grammar[k] += grammar2[k]

for k,v in grammar.items():print(k," -> "," | ".join(v),"\n")
