if __name__ == '__main__':
    file_name = 'show_must_go_on.txt'
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            total += 1
    print(f'file {file_name} has {total} lines')


    file_name = 'yesterday.txt'
    total = 0
    with open(file_name, 'r') as f:
        for line in f.readlines():
            total += 1
    print(f'file {file_name} has {total} lines')
