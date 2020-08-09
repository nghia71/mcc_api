from random import choice, shuffle
from mcc_api import Pegasus


#
# This is a simple implementation, it works but not a good one
#
def is_prime(number):
    for i in range(2, number-1):
        if number % i == 0:
            return False
    return True


#
# This implementation is only to demonstrate how to write such a function
#
def my_next_prime(number):
    next_prime = number
    found_prime = False

    while not found_prime:
        found_prime = is_prime(next_prime)
        if found_prime:
            return next_prime
        next_prime += 1


#
# This is an incomplete implementation. The test run fails in most of the cases.
#
def my_fake_coin(coins):
    if int(coins[0]) < int(coins[1]):
        return 0
    return 1


#
# This is a fake implementation, it returns '16789234' or '18789234'.
# The test run will fail.
#
def my_move_sequence(position):
    if my_position = '1':
        next_position = choice(['6', '8'])
    return next_position + '789234' + my_position


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # First sample test for the next_prime problem
    #
    result = p.submit('next_prime', 10, 11)
    print(result)

    ########################################
    # Second sample test for the next_prime problem
    #
    my_number = 100
    result = p.submit('next_prime', my_number, my_next_prime(my_number))
    print(result)

    ########################################
    # Sample test for the fake_coin problem
    #
    my_coins = '11101111'
    result = p.submit('fake_coin', my_coins, my_fake_coin(my_coins))
    print(result)

    ########################################
    # Sample test for the move_sequence problem
    #
    my_position = '7'
    result = p.submit('move_sequence', my_position, my_move_sequence(my_position))
    print(result)

    ########################################
    # Task for the next_prime problem: uncomment and make them work
    #
    # my_number = 1000000000
    # result = p.submit('next_prime', my_number, my_next_prime(my_number))

    ########################################
    # Task for the fake_coin problem: uncomment and make them work
    #
    # coins = ['0', '1', '1', '1', '1', '1', '1', '1']
    # shuffle(coins)
    # my_coins = ''.join(coins)
    # result = p.submit('fake_coin', my_coins, my_fake_coin(my_coins))
    # print(result)

    ########################################
    # Task for the move_sequence problem: uncomment and make them work
    #
    # my_position = choice(['1', '2', '3', '4', '6', '7', '8', '9'])
    # result = p.submit('move_sequence', my_position, my_move_sequence(my_position))
    # print(result)
