yee = True
while yee:
    print("\n")
    print("No capitals! No spaces!")
    keyword = input("Enter keyword: ")
    encode = input("Enter stuff to encode: ")
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    keyword_length = int(len(keyword))
    keyword_array = []

    encode_length = int(len(encode))
    encode_array = []

    alphperspec = []
    final_array = []
    zf = 0

    for i in range(0,encode_length):
        keyword_array.append(keyword[i%keyword_length])
    for i in range(0,encode_length):
        encode_array.append(encode[i])

    for i in range(0,encode_length):
        for b in range(0,26):
            if keyword_array[i] == alphabet[b]:
                z = b
        for b in range(0,26):
            if encode_array[i] == alphabet[b]:
                y = b

        for c in range(0,26):
            if z+c<26:
                alphperspec.append(alphabet[z+c])
            else:
                alphperspec.append(alphabet[(z+c)-26])

        for d in range(0,26):
            if zf!=alphabet.index(alphabet[y]):
                if zf!=25:
                    zf = zf + 1;
                else:
                    zf = 0;
                    
        final_array.append(alphperspec[zf])
        alphperspec.clear()
    print("".join(final_array))
    
    print("\n")
    yeet = input("Press enter to continue, type and press enter to cancel : ")
    if yeet != "":
        yee = False
