from mcc_api import Pegasus


#
# Demonstrate to find the number of carry operations and the sum
#
def where_waldorf(word_m_n_grid):
    splits = word_and_m_n_grid.lower().split('\n')
    word, grid = splits[0], [[e for e in row] for row in splits[2:]]
    word_len = len(word)
    m, n = [int(e) for e in splits[1].split()]
    for m_pos in range(0, m-1):
        for n_pos in range(0, n-1):
            count = 1
            for direction in [[0, 1], [1, 1], [1, 0]]:
                for k in range(1, len(word)):
                    i, j = m_pos + k*direction[0], n_pos + k*direction[1]
                    if i >= m or j >= n or grid[i][j] != word[k]:
                        break
                    count += 1
                if count == word_len:
                    return '%s %s' % (m_pos, n_pos)
    return ''


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive word, dimensions, and the grid via Pegasus
    word_and_m_n_grid = p.attempt('where_waldorf')
    print(word_and_m_n_grid)

    ########################################
    # Figure out where the word is and submit to Astria
    coordinates = where_waldorf(word_and_m_n_grid)
    print(coordinates)
    result = p.submit('where_waldorf', word_and_m_n_grid, coordinates)

    ########################################
    # See what's the answer from Astria
    print('where_waldorf', result)
