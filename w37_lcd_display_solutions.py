from mcc_api import Pegasus


PATTERNS = {
    '1': ['   ', '  |', '   ', '  |', '   '],
    '2': [' - ', '  |', ' - ', '|  ', ' - '],
    '3': [' - ', '  |', ' - ', '  |', ' - '],
    '4': ['   ', '| |', ' - ', '  |', '   '],
    '5': [' - ', '|  ', ' - ', '  |', ' - '],
    '6': [' - ', '|  ', ' - ', '| |', ' - '],
    '7': [' - ', '  |', '   ', '  |', '   '],
    '8': [' - ', '| |', ' - ', '| |', ' - '],
    '9': [' - ', '| |', ' - ', '  |', ' - '],
    '0': [' - ', '| |', '   ', '| |', ' - '],
}

#
# The key idea is to construct `mini` patterns - digits with size s=1
# and then extend the pattern when s>1
#
def lcd_display(size_and_sequence):
    # get the size an sequence, note that size is an integer
    size, sequence = size_and_sequence.split()
    size = int(size)
    digit_sequence = []

    # For each digit in the sequence
    for d in sequence:
        pattern = PATTERNS[d]   # Take the pattern of that digit
        digit = []
        for l in range(0, 2*size+3):    # For each of the 2s + 3 lines

            # Determine which line k in the patter is used for line l
            if l == 0 or l == (size+1) or l==(2*size+2):
                k = 0 if l == 0 else 2 if l == (size+1) else 4
            else:  # 0 < l and l < (size+1), (size+1) < l and l < (2*size+2):
                k = 1 if 0 < l and l < (size+1) else 3

            # Then take the line in the pattern,
            # extend the middle - keep the first and last characters
            # and assemble it into a new line
            first, middle, last = pattern[k]
            extended_middle = ''.join([middle for i in range(0, size)])
            line = '%s%s%s' % (first, extended_middle, last)
            digit.append(line)

        digit_sequence.append(digit)

    layout_lines = []
    for l in range(0, 2*size+3):
        layout_line = ' '.join([digit[l] for digit in digit_sequence])
        layout_lines.append(layout_line)

    print_layout = '\n'.join([line for line in layout_lines])
    return ''.join(layout_lines), print_layout

if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the size and sequence via Pegasus
    size_and_sequence = p.attempt('lcd_display')
    print(size_and_sequence)

    ########################################
    # Figure out how to draw it and submit to Astria
    layout, print_layout = lcd_display(size_and_sequence)
    result = p.submit('lcd_display', size_and_sequence, layout)

    ########################################
    # See what's the answer from Astria
    print(print_layout)
    print('lcd_display', result)
