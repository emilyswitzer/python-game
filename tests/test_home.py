import unittest

## some

class BasicTest(unittest.TestCase):


    def test_home_valid(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
   


