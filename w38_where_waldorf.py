from mcc_api import Pegasus


#
# Demonstrate to find the number of carry operations and the sum
#
def where_waldorf(word_m_n_grid):
    print(word_m_n_grid)
    return '1 6'


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive word, dimensions, and the grid via Pegasus
    word_and_m_n_grid = p.attempt('where_waldorf')

    ########################################
    # Figure out where the word is and submit to Astria
    coordinates = where_waldorf(word_and_m_n_grid)
    result = p.submit('where_waldorf', word_and_m_n_grid, coordinates)

    ########################################
    # See what's the answer from Astria
    print('where_waldorf', result)
