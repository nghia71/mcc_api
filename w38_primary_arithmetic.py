from mcc_api import Pegasus


#
# Demonstrate to find the number of carry operation and the sum
#
def primary_arithmetic(i_j):
    print(i_j)
    return '3 1010'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the two numbers via Pegasus.
    i_and_j = p.attempt('primary_arithmetic')

    ########################################
    # Figure out the number of carry operations and the sum and submit to Astria
    carry_sum = primary_arithmetic(i_and_j)
    result = p.submit('primary_arithmetic', i_and_j, carry_sum)

    ########################################
    # See what's the answer from Astria
    print('primary_arithmetic', result)
