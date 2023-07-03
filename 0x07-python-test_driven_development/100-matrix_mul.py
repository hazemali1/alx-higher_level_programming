#!/usr/bin/python3
"""

taking two matrix

"""


def matrix_mul(m_a, m_b):
    """
    multipli two matrix and handle error
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [num for r in m_a for num in r]):
        raise TypeError("m_a should contain only integers or floats")

    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [num for r in m_b for num in r]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m = []
    for i in range(len(m_a)):
        d = []
        for w in range(len(m_b[0])):
            q = 0
            for j in range(len(m_a[0])):
                q += m_a[i][j] * m_b[j][w]
            d.append(q)
        m.append(d)
    return m
