import unittest

from utils.utils import small_synopsis


class TestUtils(unittest.TestCase):
    def test_small_synopsis(self):
        text = "Dr. Kenzou Tenma is a renowned brain surgeon of Japanese descent " \
               "working in Europe. Highly lauded by his peers as one of the great " \
               "young minds that will revolutionize the field, he is blessed with a " \
               "beautiful fiancée and is on the cusp of a big promotion in the " \
               "hospital he works at. But all of that is about to change with a grave " \
               "dilemma that Kenzou faces one night—whether to save the life of a small " \
               "boy or that of the town's mayor. Despite being pressured by his superiors " \
               "to perform surgery on the mayor, his morals force him to perform the " \
               "surgery on the other critical patient, saving his life and forfeiting " \
               "the mayor's. A doctor is taught to believe that all life is equal; however, " \
               "when a series of murders occur in the surgeon's vicinity, all of the " \
               "evidence pointing to the boy he saved, Kenzou's beliefs are shaken. Along " \
               "his journey to unravel the true identity of his little patient, Kenzou " \
               "discovers that the fate of the world may be intertwined with the mysterious " \
               "child.\n[Written by MAL Rewrite]"

        want = "Dr. Kenzou Tenma is a renowned brain surgeon of Japanese descent working in " \
               "Europe. Highly lauded by his peers as one of the great young minds that will " \
               "revolutionize the field, he is blessed with a beautiful fiancée and is on the " \
               "cusp of a big promotion in the hospital he works at." \

        got = small_synopsis(text)

        self.assertEqual(want, got)


if __name__ == '__main__':
    unittest.main()
