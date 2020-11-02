from mcc_api import Pegasus


#
# Demonstrate to find the number of carry operation and the sum
#
def primary_arithmetic(i_j):
    i, j = [''.join(reversed(e)) for e in i_j.split()]
    c, cc, s = 0, 0, []
    for k in range(0, max([len(i), len(j)])):
        ik = int(i[k]) if k < len(i) else 0
        jk = int(j[k]) if k < len(j) else 0
        sk = ik + jk + c
        c = 0
        if sk > 9:
            sk = sk - 10
            c = 1
            cc += 1
        s.append(str(sk))
    if c == 1:
        s.append('1')
    return '%s %s' % (''.join(reversed(s)), cc)


if __name__ == '__main__':
    # Setup your credentials
    p = Pegasus('mcc.conf')

    ########################################
    # Receive the two numbers via Pegasus.
    i_and_j = p.attempt('primary_arithmetic')
    print('i_and_j', i_and_j)

    ########################################
    # Figure out the number of carry operations and the sum and submit to Astria
    carry_sum = primary_arithmetic(i_and_j)
    print('carry_sum', carry_sum)
    result = p.submit('primary_arithmetic', i_and_j, carry_sum)

    ########################################
    # See what's the answer from Astria
    print('primary_arithmetic', result)
