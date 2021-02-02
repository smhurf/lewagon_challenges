from nbresult import ChallengeResultTestCase
import numpy as np


class TestTwoMeans(ChallengeResultTestCase):
    def test_two_clusters(self):
        self.assertEqual(len(np.unique(self.result.clusters)), 2)

    def test_imbalanced_clusters(self):
        unique, counts = np.unique(self.result.clusters, return_counts=True)
        data = dict(zip(unique, counts))
        self.assertEqual(data[1] / data[0], 3)
