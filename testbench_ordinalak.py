import unittest
from ordinalak import Z18742 


# Testbench class for the function
class TestZ18742(unittest.TestCase):
    
    def test_case_1(self):
        # Description: Test Case 1 (hamaika if 11)
        input_data = "bat"
        expected_output = "lehenengo"
        self.assertEqual(Z18742(input_data), expected_output)

    def test_case_2(self):
        # Description: Test Case 2 (Another scenario)
        input_data = "bost"
        expected_output = "bosgarren"
        self.assertEqual(Z18742(input_data), expected_output)

    def test_case_3(self):
        # Description: Test Case 1 (hamaika if 11)
        input_data = "milioi bat"
        expected_output = "milioigarren"
        self.assertEqual(Z18742(input_data), expected_output)

# Entry point for running tests
if __name__ == '__main__':
    unittest.main()
