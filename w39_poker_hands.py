from mcc_api import Pegasus


#
# Demonstrate to compare the list hands
#
def poker_hands(hands):
    print(hands)
    return '0 1 2'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the hands via Pegasus
    hands = p.attempt('poker_hands')

    ########################################
    # Figure out what is the order of the hands and submit to Astria
    order = poker_hands(hands)
    result = p.submit('poker_hands', hands, order)

    ########################################
    # See what's the answer from Astria
    print('poker_hands', result)
