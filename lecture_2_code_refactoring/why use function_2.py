# problems
#     reusability
#     modularity
#     scope

def get_lines_count(file_name: str) -> int:
    """ Getting total lines of file """
    total = 0
    with open(file_name, 'r') as f:
        for _ in f.readlines():
            total += 1
    return total


def print_lines_count(file_name: str):
    """ Just print lines count """
    print(f'file {file_name} has {get_lines_count(file_name)} lines')


if __name__ == '__main__':
    print_lines_count(file_name='show_must_go_on.txt')
    print_lines_count(file_name='yesterday.txt')

