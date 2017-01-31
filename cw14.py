'''
cd '.\Python\TevisPrograms\Code Wars'
python
import cw14 as cw14
cw14.next_bigger(1234567890)
'''
class NextHighestAnagram(object):

    def go(self, n):
        n_list = list(str(n))
        n_list.reverse()

        if (self.is_sorted_original(n_list)):
            return -1

        pointer1 = 0
        pointer2 = 1
        return self.main_loop(n_list, pointer1, pointer2)

    def main_loop(self, n_list, pointer1, pointer2):
        while(True):
            if self.is_next_digit_lesser_value(n_list, pointer1, pointer2):
                result = self.swap_split_sort_combine(n_list, pointer1, pointer2)
                return result
            secondary_loop_output = self.secondary_loop(n_list, pointer1, pointer2)
            if (secondary_loop_output != 0):
                return secondary_loop_output
            if self.is_pointer2_on_highest_digit(n_list, pointer2):
                pointer1, pointer2 = self.move_pointer1_up_one_digit__pointer2_one_higher(pointer1)
                return self.main_loop(n_list, pointer1, pointer2)
            pointer2 = self.move_pointer2_up_one_digit(pointer2)


    def secondary_loop(self, n_list, pointera, pointerb):
        pointer3 = pointera + 1
        while (pointer3 < pointerb):
            if self.is_next_digit_lesser_value(n_list, pointer3, pointerb):
                return self.swap_split_sort_combine(n_list, pointer3, pointerb)
            pointer3 += 1
        return 0

    def is_sorted_original(self,n_list):
        if (sorted(n_list) == n_list):
            return True
        else:
            return False

    def is_next_digit_lesser_value(self, n_list, pointer1, pointer2):
        return n_list[pointer2] < n_list[pointer1]

    def is_pointer2_on_highest_digit(self, n_list, pointer2):
        return pointer2 == len(n_list)-1

    def move_pointer2_up_one_digit(self, pointer2):
        return pointer2 + 1

    def move_pointer1_up_one_digit__pointer2_one_higher(self, pointer1):
        return pointer1 + 1, pointer1 + 2

    def swap_split_sort_combine(self, n_list, pointer1, pointer2):
        n_list[pointer1],n_list[pointer2]=n_list[pointer2],n_list[pointer1]
        lower_digits_list = n_list[:pointer2]
        lower_digits_list.sort()
        lower_digits_list.reverse()
        return_list = lower_digits_list + n_list[pointer2:]
        return_list.reverse()
        return int(''.join(return_list))





def next_bigger(n):
    nha = NextHighestAnagram()
    result = nha.go(n)
    print "n:",n
    print "result:",result
    return result
