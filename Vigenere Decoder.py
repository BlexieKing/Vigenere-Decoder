z = 0
y = 0
h = 0
zf = 0
final = []
alphperspec = []
found = "no"
keyword= input("Enter keyword: ")
decode = input("Enter stuff to decode: ")
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
keycorres = []
keysplit = []
keydec = []
length = int(len(keyword))
lengthdec = int(len(decode))

for i in range (0,lengthdec):
    keycorres.append(keyword[i%length])
for i in range (0,length):
    keysplit.append(keyword[i])
for i in range (0,lengthdec):
    keydec.append(decode[i])
for i in range(0,lengthdec):
    #keycorres[i] #Letter of key - Find on alphabet (Z)
    for b in range(0,26):
        if keycorres[i] == alphabet[b]:
            z = b #18 first
    for b in range(0,26):
        if keydec[i] == alphabet[b]:
            y = b #22 first
    h = z #18, index of first letter of key

    for i in range(0,26):
        if z+i<26:
            alphperspec.append(alphabet[z+i])
        else:
            alphperspec.append(alphabet[(z+i)-26])
    for b in range(0,26):
        if zf != alphperspec.index(alphabet[y]):
            if zf==25:
                zf = 0;
            else:
                zf = zf + 1;   
    final.append(alphabet[zf])
    alphperspec.clear()
print(final)
        
    #keydec[i] #Letter of stuff to decode (Y)
