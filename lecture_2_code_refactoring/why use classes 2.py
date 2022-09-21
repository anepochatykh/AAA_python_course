class TextHandler:
    """ Encapsulate filename """
    def __init__(self, file_name):
        self.file_name = file_name
        self._count_lines()

    def _count_lines(self):
        total = 0
        with open(self.file_name, 'r') as f:
            for _ in f.readlines():
                total += 1
        self.total_lines = total

    def pprint(self):
        print(f'file {self.file_name} has {self.total_lines} lines')


# # count total numbers using python
if __name__ == '__main__':
    TextHandler(file_name='show_must_go_on.txt').pprint()
    TextHandler(file_name='yesterday.txt').pprint()

