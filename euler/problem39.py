# -*- encoding: utf-8 -*-

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import math


def problem39():
    p = 0
    max_candidates = 0
    max_p = 0
    for p in xrange(3, 1001):
        print 'testing %d' % p
        candidates = 0
        for hypo in range(p/3 + 1, p-1):
            hypo_sq = hypo ** 2
            for side_a in range(1, int(math.sqrt(hypo_sq/2.0))):
                side_b = p - hypo - side_a
                if side_b ** 2 + side_a ** 2 == hypo_sq:
                    candidates += 1
                    print '(%d, %d, %d)' % (side_a, side_b, hypo)
        print 'found %d candidates' % candidates
        if candidates > max_candidates:
            max_p = p
            max_candidates = candidates
    return max_p


if __name__ == '__main__':
    print problem39()
