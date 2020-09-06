from mcc_api import Pegasus


#
# Demonstrate to create a layout
#
def cycle_length(i_and_j):
    print(i_and_j)
    return '1'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the two numbers via Pegasus.
    i_and_j = p.attempt('cycle_length')

    ########################################
    # Figure out the maximum cycle length and submit to Astria
    max_length = cycle_length(i_and_j)
    result = p.submit('cycle_length', i_and_j, max_length)

    ########################################
    # See what's the answer from Astria
    print('cycle_length', result)
