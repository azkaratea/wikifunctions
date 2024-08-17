import unittest
from kardinalak import Z18733 


# Testbench class for the function
class TestZ18733(unittest.TestCase):
    
    def test_case_1(self):
        # Description: Test Case 1 (hamaika if 11)
        input_data = 11
        expected_output = "hamaika"
        self.assertEqual(Z18733(input_data), expected_output)

    def test_case_2(self):
        # Description: Test Case 2 (Another scenario)
        input_data = -11
        expected_output = "minus hamaika"
        self.assertEqual(Z18733(input_data), expected_output)

    def test_case_3(self):
        # Description: Test Case 1 (hamaika if 11)
        input_data = 37
        expected_output = "hogeita hamazazpi"
        self.assertEqual(Z18733(input_data), expected_output)

    def test_case_4(self):
        # Description: Test Case 2 (Another scenario)
        input_data = 100
        expected_output = "ehun"
        self.assertEqual(Z18733(input_data), expected_output)

    def test_case_5(self):
        # Description: Test Case 1 (hamaika if 11)
        input_data = 101
        expected_output = "ehun eta bat"
        self.assertEqual(Z18733(input_data), expected_output)


# Entry point for running tests
if __name__ == '__main__':
    unittest.main()
