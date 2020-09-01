from mcc_api import Pegasus


#
# Demonstrate to find the missing difference
#
def missing_difference(sequence):
    print(sequence)
    return '1'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the sequence via Pegasus
    sequence = p.attempt('jolly_jumpers')

    ########################################
    # Figure out what is the missing numbers and submit to Astria
    missing_number = missing_difference(sequence)
    result = p.submit('jolly_jumpers', sequence, missing_number)

    ########################################
    # See what's the answer from Astria
    print('jolly_jumpers', result)
