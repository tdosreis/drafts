import numpy as np


class SubStrings():
    """This class is under development...

    Author: Tiago Rosa dos Reis
    """

    def __init__(self, key_words, variables):
        self.key_words = key_words
        self.variables = variables

    def catch_sub_variables(self):
        """Quick utility that displays all the variables
        belonging to a certain general group.

        Parameters
        ----------
        key_words : dictionary
            Dictionary containing a general word and its derivatives.

        list_of_variables : list
            List of all features present in a dataset.

        Returns
        -------
        data_dictionary : dictionary
            Dictionary containing all the groups matching a
            certain condition.
        """
        list_of_substrings = self._list_of_values()

        strs = self._get_sub_strings(list_of_substrings, self.variables)

        groups = {
            str(i): [v for k in j for v in strs if k in v]
            for i, j in self.key_words.items()
        }

        return groups

    def _list_of_values(self):

        return list(
                np.array(
                    list(self.key_words.values()), dtype=object
                ).ravel()
            )

    def _get_sub_strings(self, list_of_substrings, list_of_variables):

        return list(
            np.unique(
                [i for j in list_of_substrings
                 for i in list_of_variables if j in i]
            )
        )
