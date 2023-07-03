#!/usr/bin/python3
"""

Numpy

"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    multipli two matrix using numpy
    """
    return np.dot(np.array(m_a), np.array(m_b))
