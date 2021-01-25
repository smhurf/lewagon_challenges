from nbresult import ChallengeResultTestCase


class TestColorcount(ChallengeResultTestCase):
    def test_colorcount(self):
        self.assertEqual(self.result.color_count, 113382)
