from mcc_api import Pegasus


#
# Demonstrate to find if the number is a carmichael number
#
def carmichael_numbers(number):
    print(number)
    return '-1'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the number via Pegasus
    number = p.attempt('carmichael_numbers')

    ########################################
    # Figure out what the number and submit to Astria
    is_carmichael_number = carmichael_numbers(number)
    result = p.submit('carmichael_numbers', number, is_carmichael_number)

    ########################################
    # See what's the answer from Astria
    print('carmichael_numbers', result)
