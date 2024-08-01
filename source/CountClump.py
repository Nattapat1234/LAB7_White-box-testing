# Lab#7 - Whitebox testing
# SC353201 Software Quality Assurance
# Semester 1/2567
# Instructor: Chitsutha Soomlek

class CountClump:
  """
  This class provides a method to count the number of "clumps" in a list of integers.
  A clump is a run of 2 or more of the same adjacent numbers.
  """

  @staticmethod
  def count_clumps(nums):
    """
    Counts the number of "clumps" in a list of integers.
    A clump is a run of 2 or more of the same adjacent numbers.

    Args:
      nums: A list of integers.

    Returns:
      The number of clumps in the list.
    """
    if nums is None or len(nums) == 0:
      return 0
    
    count = 0
    prev = nums[0]
    in_clump = False
    for i in range(1, len(nums)):
      if nums[i] == prev and not in_clump:
        in_clump = True
        count += 1

      elif nums[i] != prev:
        prev = nums[i]
        in_clump = False      

    return count  

# #Example usage
# nums = [1, 2, 2, 3, 3, 4, 4, 4, 1]
# clump_count = CountClump.count_clumps(nums)
# print(f"Number of clumps: {clump_count}")  # Output: Number of clumps: 3
test_cases = [
    {"TestcaseNo": 1, "input": None, "ExpectedResult": 0}, 
    {"TestcaseNo": 2, "input": [], "ExpectedResult": 0}, 
    {"TestcaseNo": 3, "input": [1], "ExpectedResult": 0}, 
    {"TestcaseNo": 4, "input": [1, 1, 2, 3], "ExpectedResult": 1}, 
    {"TestcaseNo": 5, "input": [1, 1, 1], "ExpectedResult": 1}, 
    {"TestcaseNo": 6, "input": [1, 2, 2, 3, 3, 4], "ExpectedResult": 2}, 
    {"TestcaseNo": 7, "input": [1, 2, 2, 2, 3], "ExpectedResult": 1}, 
    {"TestcaseNo": 8, "input": [1, 1, 2, 2, 2, 3, 3], "ExpectedResult": 3},
    {"TestcaseNo": 9, "input": [1, 2], "ExpectedResult": 0},
]

# Test Runner
def run_tests():
    for test in test_cases:
        result = CountClump.count_clumps(test["input"])
        assert result == test["ExpectedResult"], f"Test case {test['TestcaseNo']} failed: got {result}, expected {test['ExpectedResult']}"

# Run the tests
run_tests()
print("All test cases passed.")
