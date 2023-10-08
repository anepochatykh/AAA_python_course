program_name = 'python course'

def show_message(name: str):
    global program_name
    program_name = 'ml course'
    print('name', name)
    return f'Hey {name}, you had better learn {program_name}'


if __name__ == '__main__':
    print(f'Before change : {program_name}')

    print(show_message('aatest'))
    #Hey aatest, you had better learn ml course

    print(f'After change : {program_name}')
    # python course

    # print(name)
    # NameError: name 'name' is not defined
