# numpy_wrapper
#
# A wrapper around the NumPy library that makes it easier to use for simple
# array mathematics.

import numpy

def new(num_rows, num_cols):
    return numpy.zeros((num_rows, num_cols), dtype=numpy.int32)

def average(arrays_to_average):
    return numpy.mean(numpy.array(arrays_to_average), axis=0)

def get_indices(array):
    return numpy.transpose(array.nonzero())

