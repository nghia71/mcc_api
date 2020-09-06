from mcc_api import Pegasus


#
# Demonstrate to create a layout
#
def lcd_display(sequence):
    print(sequence)
    return '1'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the size and sequence via Pegasus
    size_and_sequence = p.attempt('lcd_display')

    ########################################
    # Figure out how to draw it and submit to Astria
    layout = lcd_display(size_and_sequence)
    result = p.submit('lcd_display', size_and_sequence, layout)

    ########################################
    # See what's the answer from Astria
    print('lcd_display', result)
