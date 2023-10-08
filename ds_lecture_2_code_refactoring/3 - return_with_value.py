def return_with_value(any_number: int):
    print('The specified number is', any_number)
    return any_number


if __name__ == '__main__':
    result = return_with_value(1024)
    # The specified number is 1024

    print(result)
    # 1024

