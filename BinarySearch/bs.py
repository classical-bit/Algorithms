def b_search(array, target):
    mi = 0
    ma = len(array) - 1
    counter = 0
    while ma >= mi:
        counter = counter + 1
        guess = int((mi + ma)/2)

        if array[guess] == target:
            return {'position': guess, 'steps': counter}
        elif target < array[guess]:
            ma = guess - 1
        else:
            mi = guess + 1

    return None


def main():
    a = [i**2 for i in range(1, 10)]
    result = b_search(a, int(input('in {} Look for: '.format(a))))
    if result is None:
        print('NotFound!')
    else:
        print('POS:', result['position'] + 1)
        print('STEPS:', result['steps'])


if __name__ == '__main__':
    main()
