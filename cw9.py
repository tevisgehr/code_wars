d = {"a": 1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
num_lst = []
text = "The sunset sets at twelve o' clock."


txt_lst = list(text.lower())

for x in txt_lst:
    if x in d:
        num_lst.append(d[x])

print " ".join(str(x) for x in num_lst)






def alphabet_position(text):
    d = {"a": 1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
    num_lst = []
    text = "The sunset sets at twelve o' clock."


    txt_lst = list(text.lower())

    for x in txt_lst:
        if x in d:
            num_lst.append(d[x])

    return " ".join(str(x) for x in num_lst)
