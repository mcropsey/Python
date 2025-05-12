a = ['a', 'b', 'a', 'aaa', 1, 2, 1, 1]


class CheckCount(object):

    def __init__(self, data_list):
        self.data_list = data_list

    def get_count_keys(self):
        count_dict = {}
        for i in self.data_list:
            if i not in count_dict:
                count_dict[i] = 0
            count_dict[i] = count_dict[i] + 1
        return count_dict

    @staticmethod
    def print_count_values(count_dict):
        for key in count_dict:
            print(key, " - ", count_dict.get(key))


chk_count = CheckCount(a)
new_dict = chk_count.get_count_keys()
chk_count.print_count_values(new_dict)