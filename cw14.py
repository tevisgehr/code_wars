'''
cd '.\Python\TevisPrograms\Code Wars'
python
import cw14 as cw14
cw14.next_bigger(5451)
'''
class NextHighestAnagram(object):

    def go(self, n):
        n_list = list(str(n))
        print n_list

        #reversing for ease of indexing ('0' digit is leftmost)
        n_list.reverse()
        print "is_sorted_original:", self.is_sorted_original(n_list)

        if (self.is_sorted_original(n_list)):
            return -1

        #pointers signify which digit (list index) is currently being examined
        pointer1 = 0
        pointer2 = 1
        self.main_loop(n_list, pointer1, pointer2)

    def main_loop(self, n_list, pointer1, pointer2):
        while(True):
            print "is_next_digit_lesser_value__pointer2:", self.is_next_digit_lesser_value__pointer2(n_list, pointer1, pointer2)
            if self.is_next_digit_lesser_value__pointer2(n_list, pointer1, pointer2):
                self.swap_split_sort_combine(n_list, pointer1, pointer2)

            print "is_pointer2_on_highest_digit:", self.is_pointer2_on_highest_digit(n_list, pointer2)
            if self.is_pointer2_on_highest_digit(n_list, pointer2):
                print "move_pointer1_up_one_digit__pointer2_one_higher(output):", self.move_pointer1_up_one_digit__pointer2_one_higher(pointer1)
                pointer1, pointer2 = self.move_pointer1_up_one_digit__pointer2_one_higher(pointer1)
                self.main_loop(n_list, pointer1, pointer2)

            print "move_pointer2_up_one_digit(output):", self.move_pointer2_up_one_digit(pointer2)
            pointer2 = self.move_pointer2_up_one_digit(pointer2)



    def is_sorted_original(self,n_list):
        if (sorted(n_list) == n_list):
            return True
        else:
            return False

    def is_next_digit_lesser_value__pointer2(self, n_list, pointer1, pointer2):
        return n_list[pointer2] < n_list[pointer1]

    def is_pointer2_on_highest_digit(self, n_list, pointer2):
        print "len(n_list): ",len(n_list)-1
        print "pointer2: ",pointer2
        return pointer2 == len(n_list)-1

    def move_pointer2_up_one_digit(self, pointer2):
        return pointer2 + 1

    def move_pointer1_up_one_digit__pointer2_one_higher(self, pointer1):
        return pointer1 + 1, pointer1 + 2

    def swap_split_sort_combine(self, n_list, pointer1, pointer2):
        print "swap_split_sort_combine"
        print n_list, pointer1, pointer2

        #dont forget to n_list.reverse()
        exit()




def next_bigger(n):
    nha = NextHighestAnagram()
    return nha.go(n)
