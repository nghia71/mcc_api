from math import sqrt
from mcc_api import Pegasus

MINE = '*'

def mine_sweeper(field):
    # Calculate the size length of the field
    f_size = int(sqrt(len(field)))

    # Create a 2-dimension 0-filled field, basically the below:
    # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # This is the result after filled with mines and numbers around the mines
    swept_field = [[0 for i in range(0, f_size)] for j in range(0, f_size)]

    # Iterate through all squares on the field as if it is a 1-diemension array
    for pos in range(0, len(field)):

        # take some action only if there's a mine
        if field[pos] == MINE:

            # find which row and column by determine the quotient and remainder
            m_row, m_col = pos // f_size, pos % f_size
            swept_field[m_row][m_col] = MINE    # duplicate the mine

            # Now look at the squares in the above, current, and below row
            # as well as the left, current, and right column
            for r_diff in [-1, 0, 1]:   # row above, this, below
                for c_diff in [-1, 0, 1]:   # left, this, right column
                    if r_diff == 0 and c_diff == 0:   # skip the mine
                        continue
                    row = m_row + r_diff    # row of the square
                    col = m_col + c_diff    # column of the square
                    if 0 <= row <= f_size-1 and 0 <= col <= f_size-1:
                        if swept_field[row][col] == MINE:    # don't fill mines
                            continue
                        swept_field[row][col] += 1  # increase one

    return ''.join(str(i) for row in swept_field for i in row)


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the field via Pegasus
    field = p.attempt('mine_sweeper')
    print('\n'.join([field[0+i:4+i] for i in range(0, 16, 4)]), '\n')

    ########################################
    # Figure out the values of other squares of the field and submit to Astria
    detected = mine_sweeper(field)
    result = p.submit('mine_sweeper', field, detected)

    ########################################
    # See what's the answer from Astria
    print('\n'.join([detected[0+i:4+i] for i in range(0, 16, 4)]), '\n')
    print('mine_sweeper', result)
