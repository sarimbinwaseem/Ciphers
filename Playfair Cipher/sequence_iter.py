"""To iterate over the data i.e. alphabets for inserting into matrix
using next()
"""


class SequenceIterator:
    """Iterator class for data to get iterated by next()"""

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
        else:
            raise StopIteration

        return item
