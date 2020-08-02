import random
import time
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
# This is a fake implementation, it always return '4'. The test run will fail.
#
def my_fake_coin(coins):
    return '4'


#
# This is a fake implementation, it always return '4'. The test run will fail.
#
def my_move_sequence(position):
    return '12345678'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('anthony_ly.conf')

    # Solve the first problem and submit
    result = p.submit('next_prime', 10, 11)
    print(result)

    my_number = 100
    result = p.submit('next_prime', my_number, my_next_prime(my_number))
    print(result)

    my_coins = '10111111'
    result = p.submit('fake_coin', my_coins, my_fake_coin(my_coins))
    print(result)

    my_position ='7'
    result = p.submit('move_sequence', my_position, my_move_sequence(my_position))
    print(result)
