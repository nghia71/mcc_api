from mcc_api import Pegasus


#
# Demonstrate to find all the mines
#
def mine_sweeper(field):
    print(field)
    return '1*102210*1001100'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the field via Pegasus
    field = p.attempt('mine_sweeper')

    ########################################
    # Figure out the values of other squares of the field and submit to Astria
    detected = mine_sweeper(field)
    result = p.submit('mine_sweeper', field, detected)

    ########################################
    # See what's the answer from Astria
    print('mine_sweeper', result)
