"""
Helper functions for Playfair Cipher
"""


from pprint import pprint
from sequence_iter import SequenceIterator


class PlayfairUtils:
    """docstring for PlayfairUtils"""

    def __init__(self):
        super().__init__()
        self.first_index = 0
        self.second_index = 0
        self.matrix = [["" for _ in range(5)] for _ in range(5)]

    def clean_keyword(self, keyword: str) -> str:
        """Remove repeating letters from the keyword
        datetype "set" doesn't work as it randomizes the letters.
        """

        key_set = "".join(dict.fromkeys(keyword))

        return key_set

    def check_for_IJ(self) -> bool:
        """Checks if I or J in the row"""

        for row in self.matrix:
            if "I" in row or "J" in row:
                return True

        return False

    def insert_into_matrix(self, data) -> None:
        """Inserting keyword into matrix"""

        data = SequenceIterator(data)

        flag = True
        while self.first_index < 5:
            while self.second_index < 5 and flag:
                try:
                    alpha = next(data)
                except StopIteration:
                    flag = False
                else:
                    # creating error.
                    if (alpha in ('I', 'J')) and self.check_for_IJ():
                        continue
                        # self.matrix[self.first_index][self.second_index] = 'I'


                    self.matrix[self.first_index][self.second_index] = alpha
                    # print(f"First_index: {self.first_index} and Second_index: {self.second_index}")
                    # print(f"Alphabet: {alpha}")
                    # pprint(self.matrix)
                    # print()
                    self.second_index += 1
            if flag:
                self.second_index = 0
                self.first_index += 1
            if flag is False:
                break

    def get_letter_row(self, letter) -> int:
        """Returns the row number of the letter"""

        for index_row, row in enumerate(self.matrix):
            if letter in row:
                idx_row = index_row

        return idx_row

    def get_letter_index(self, row_index, letter) -> int:
        """Returns the index of the letter in the row"""

        idx_letter = self.matrix[row_index].index(letter)

        return idx_letter


def main():
    pu = PlayfairUtils()
    e = pu.clean_keyword("NEWCOMBINATION")
    print(e)
    pu.insert_into_matrix(e)
    pprint(pu.matrix)


if __name__ == "__main__":
    main()
