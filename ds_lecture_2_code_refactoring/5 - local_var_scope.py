program_name = 'python course'


def show_message(name: str):
    program_name = 'ml course'
    return f'Hey {name}, you had better learn {program_name}'


if __name__ == '__main__':
    print(show_message('aatest'))
    #Hey aatest, you had better learn ml course
    print(program_name)
    # python course
    print(name)
    # NameError: name 'name' is not defined
