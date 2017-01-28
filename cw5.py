#KATA: Format a string of names like 'Bart, Lisa & Maggie'.

import unittest



class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_5_names(self):
        #self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]), 'Bart, Lisa, Maggie, Homer & Marge', "Must work with many names")
        #self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}]), 'Bart, Lisa & Maggie', "Must work with many names")
        #self.assertEqual(namelist([{'name': 'Bart'},{'name': 'Lisa'}]), 'Bart & Lisa', "Must work with two names")
        self.assertEqual(namelist([{'name': 'Bart'}]), 'Bart', "Wrong output for a single name")
        #self.assertEqual(namelist([]), '', "Must work with no names")


def namelist(names):
    names_lst = []

    for x in names:
        names_lst.append(x['name'])

    name_str = ''

    if len(names_lst) > 1:
        last = names_lst.pop(-1)

        for x in names_lst:
            name_str = name_str + x
            name_str = name_str + ", "
        name_str = name_str[:-2]
        name_str = name_str + " & "
        name_str = name_str + last
    elif len(names_lst) > 0:
        name_str = str(names_lst[0])

    name_str= str(name_str)
    print "Name String: (" , name_str, ")"
    print "Length: ", len(name_str)
    print "Names list: (" , names_lst, ")"
    return name_str


if __name__ == '__main__':
    unittest.main()
