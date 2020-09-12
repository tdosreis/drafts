import numpy as np
import itertools
from scipy import stats


class EvalMetrics():
    """Alternative class for model performance evaluation. The
    current implementation allows the computation of the KS test
    as well as accuracy and confusion matrix computation.

    Author: Tiago Rosa dos Reis

    Note: code is still under development
    """

    def __init__(self, y_true, y_pred):
        self.y_true = np.array(y_true)
        self.y_pred = np.array(y_pred)

    def kolmogorov_smirnov(self):
        '''
        Computes the Kolmogorov-Smirnov test between y_true and y_pred
        '''
        ks_ = stats.ks_2samp(
                self.y_pred[self.y_true == 1.0],
                self.y_pred[self.y_true == 0.0]
                )[0]
        return ks_

    def accuracy(self):
        '''
        Computes the accuracy between y_true and y_pred
        '''
        x = zip(self.y_true, self.y_pred)
        trues = list(map(
            lambda x: 1 if x[0] == x[1] else 0, x))
        return sum(trues)/len(trues)

    def confusion_matrix(self):
        '''
        Generalized form of the confusion matrix between y_true and y_pred
        '''
        map_to_map = self._convert_maps()

        M = self._zero_matrix()

        for i in map_to_map:
            M[i] = map_to_map.get(i)

        return M

    def _convert_maps(self):
        coordinates = self._transform()
        sum_maps = self._sum_maps()
        return {coordinates.get(i): sum_maps.get(i) for i in sum_maps}

    def _zero_matrix(self):

        dim = len(np.unique(self.y_true))

        return np.zeros((1, dim, dim))[0]

    def _combinations(self, n_combinations=2):

        list_of_values = np.unique(self.y_true)

        # identity combinations
        a = list(map(lambda x: (x, x), list_of_values))

        # ordered combinations
        b = list(itertools.combinations(list_of_values, n_combinations))

        # reverse order combinations
        c = list(map(lambda x: tuple(sorted(x, reverse=True)), b))

        return sorted(sum([a, b, c], []))

    def _map_indices(self):

        return {j: i for (i, j) in enumerate(np.unique(self.y_true))}

    def _get_indices(self, x):

        ix = self._map_indices()
        return tuple([ix.get(x[i]) for i in range(len(x))])

    def _transform(self, n_combinations=2):

        return {i: self._get_indices(i)
                for i in self._combinations(n_combinations=2)}

    def _sum_maps(self):

        maps = {
                i: sum(
                    list(
                        map(
                            lambda x: x == i,
                            list(zip(self.y_true, self.y_pred))
                            )
                        )
                    )
                for i in self._combinations()}

        return maps
