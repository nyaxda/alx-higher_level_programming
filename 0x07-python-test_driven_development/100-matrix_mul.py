#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices."""
    message1 = "each row of m_a must be of the same size"
    message2 = "each row of m_b must be of the same size"
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    elif not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    elif len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    else:
        for row in m_a:
            if not isinstance(row, list):
                raise TypeError("m_a must be a list of lists")
            elif len(row) == 0:
                raise ValueError("m_a can't be empty")
            elif len(row) != len(m_a[0]):
                raise TypeError(message1)
            else:
                for num in row:
                    if isinstance(num, bool) or not isinstance(num, (int, float)):
                        raise TypeError("m_a should contain only integers or floats")
        for row in m_b:
                if not isinstance(row, list):
                    raise TypeError("m_b must be a list of lists")
                elif len(row) == 0:
                    raise ValueError("m_b can't be empty")
                elif len(row) != len(m_b[0]):
                    raise TypeError(message2)
                else:
                    for num in row:
                        if isinstance(num, bool) or not isinstance(num, (int, float)):
                            raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_a[0])):
                sum += m_a[i][k] * m_b[k][j]
            result_row.append(sum)
        result.append(result_row)

    return result
