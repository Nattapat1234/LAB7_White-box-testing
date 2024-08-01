import unittest
import os, sys
CURRENTDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENTDIR))
from source.CountClump import CountClump




class TestCountClump(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('This method is called once before all tests in the class.')

    @classmethod
    def tearDownClass(cls):
        print('\nThis method is called once after all tests in the class.')

    def setUp(self):
        self.test_obj = CountClump()
        print('\nSetting up test case.')

    def tearDown(self):
        print('End of test case.')

    def test_none_input(self):
        """TestcaseNo. 1: Test with None as input"""
        result = self.test_obj.count_clumps(None)
        self.assertEqual(result, 0)

    def test_empty_list(self):
        """TestcaseNo. 2: Test with an empty list"""
        result = self.test_obj.count_clumps([])
        self.assertEqual(result, 0)

    def test_single_element(self):
        """TestcaseNo. 3: Test with a list containing one element"""
        result = self.test_obj.count_clumps([1])
        self.assertEqual(result, 0)

    def test_two_elements_no_clump(self):
        """TestcaseNo. 9: Test with a list of two different elements"""
        result = self.test_obj.count_clumps([1, 2])
        self.assertEqual(result, 0)

    def test_two_elements_with_clump(self):
        """TestcaseNo. 4: Test with a list of two same elements"""
        result = self.test_obj.count_clumps([1, 1, 2, 3])
        self.assertEqual(result, 1)

    def test_multiple_clumps(self):
        """TestcaseNo. 6: Test with multiple clumps"""
        result = self.test_obj.count_clumps([1, 2, 2, 3, 3, 4])
        self.assertEqual(result, 2)

    def test_single_clump(self):
        """TestcaseNo. 5: Test with a single clump in the list"""
        result = self.test_obj.count_clumps([1, 1, 1])
        self.assertEqual(result, 1)

    def test_no_clumps(self):
        """TestcaseNo. 7: Test with a list where clump is not continuous"""
        result = self.test_obj.count_clumps([1, 2, 2, 2, 3])
        self.assertEqual(result, 1)

    def test_multiple_clumps_with_overlap(self):
        """TestcaseNo. 8: Test with overlapping clumps"""
        result = self.test_obj.count_clumps([1, 1, 2, 2, 2, 3, 3])
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()