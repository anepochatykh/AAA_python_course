def return_without_value(bad_number: int):
    print('The bad number is', bad_number)
    return


if __name__ == '__main__':
    result = return_without_value(100500)
    # The bad number is 100500

    print(result)
    # None
