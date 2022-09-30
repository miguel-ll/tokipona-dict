f1 = open("tlist.txt","r")
di = {}
for i in f1:
	z = i.split(" - ")
	di[z[0]] = z[1]
f1.close()

print("[1] Search for word or letter [toki pona - english]\n[2] Search by a general term in word [toki pona - english]\n")
n = int(input("Please choose an option: "))
while not (n == 1 or n == 2):
	n = input("Invalid option. Try again: ")

# Search type 1: prints the meaning of a word that starts with a specific term wd.
def search1(wd):
    global di
    li = [v for k,v in di.items() if k.startswith(wd)]
    li2 = [k for k,v in di.items() if k.startswith(wd)]
    for x in range(len(li2)):
	    print(li2[x] + ": " + li[x])
	
# Search type 2: prints the meaning of a word which has the term wd anywhere in it.
def search2(wd):
	 global di
	 l1 = [v for k,v in di.items() if wd in k]
	 l2 = [k for k,v in di.items() if wd in k]
	 for z in range(len(l2)):
	 	print(l2[z] + ": " + l1[z])
		
def tokiponize(phr):
	a = phr.replace("b","p")
	b = a.replace("c","k")
	c = b.replace("d","t")
	d = c.replace("f","j")
	e = d.replace("g","j")
	f = e.replace("h","")
	g = f.replace("q","k")
	h = g.replace("r","l")
	i = h.replace("v","u")
	j = i.replace("x","ks")
	k = j.replace("y","i")
	l = k.replace("z","ts")
	return l
	 	
if n == 1:
	wd = input("Enter a word/letter: ")
	search1(wd)
if n == 2:
	wd = input("Enter a term: ")
	search2(wd)
	
