class NextHighestAnagram(object):

    def go(self, n):
        n_list = list(str(n))
        print n_list
        if (self.is_sorted_original()):
            print "is_sorted_original:", self.is_sorted_original()

    def is_sorted_original(self):
        if (sorted(n_list) == n_list):
            return True
        else:
            return False

    def is_pointer1_at_lowest_digit(self):
        pass

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
    nha.go(n)
