'''
cd '.\Python\TevisPrograms\Code Wars'
python
import cw14 as cw14
cw14.next_bigger(1243)
'''
class NextHighestAnagram(object):

    def go(self, n):
        n_list = list(str(n))
        print n_list
        print "is_sorted_original:", self.is_sorted_original(n_list)

        if (self.is_sorted_original(n_list)):
            return -1

        pointer1 = 1
        pointer2 = 2

        print "is_pointer1_at_lowest_digit:", self.is_pointer1_at_lowest_digit(pointer1)
        if self.is_pointer1_at_lowest_digit(pointer1):
            pass

    def is_sorted_original(self,n_list):
        if (sorted(n_list) == n_list):
            return True
        else:
            return False

    def is_pointer1_at_lowest_digit(self, pointer1):
        return pointer1 == 1

    def is_next_digit_lesser_value__pointer2(self):
        pass

    def is_pointer2_on_highest_digit(self):
        pass

    def move_pointer2_up_one_digit(self):
        pass

    def move_pointer1_up_one_digit__pointer2_one_higher(self):
        pass

    def swap_split_sort_combine(self):
        pass





def next_bigger(n):
    nha = NextHighestAnagram()
    return nha.go(n)
