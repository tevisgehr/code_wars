s = "This is an-example of a sentence."
alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
transform_map = {}
result = ""
s2 = s
for c in s2:
    if c.lower() not in alphabet:
        s2 = s2.replace(c, " "+c+" ")

words_lst = s2.split()
print "WORDS LIST: ", words_lst

for x in words_lst:
    if len(x) > 3:
        transform_map[x] = x[0]+str(len(x)-2)+x[len(x)-1]
print "TRANSFORM MAP:", transform_map

for x in transform_map.keys():
    s = s.replace(x, transform_map[x])

print s


def abbreviate(s):
    alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    transform_map = {}
    result = ""
    s2 = s
    for c in s2:
        if c.lower() not in alphabet:
            s2 = s2.replace(c, " "+c+" ")

    words_lst = s2.split()
    print "WORDS LIST: ", words_lst

    for x in words_lst:
        if len(x) > 3:
            transform_map[x] = x[0]+str(len(x)-2)+x[len(x)-1]
    print "TRANSFORM MAP:", transform_map

    for x in transform_map.keys():
        s = s.replace(x, transform_map[x])

    return s
