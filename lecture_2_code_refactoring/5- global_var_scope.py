program_name = 'python course'


def show_login(role: str) -> str:
    return f'Logged in to {program_name} as a {role}'


if __name__ == '__main__':
    print(show_login('student'))
    #Logged in to python course as a student
