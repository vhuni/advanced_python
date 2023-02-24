import unittest

def addition(a,b):
    return a+b

class test_sum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(addition(1,2),3, "sum of 1 and 2 is 3") 
        self.assertEqual(addition(100,1),101, "sum of 100 and 1 is 101")
        self.assertEqual(addition(1000,1),1001, "sum of 1000 and 1 is 1001")
    
    def test_sum_float(self):
        self.assertEqual(addition(2.5,3.5),6, "sum of 2.5 and 3.5 is 6")

    def test_sum_string(self):
        self.assertEqual(addition('a','b'),'ab', "sum of a and b is ab")

if __name__ == '__main__':
    unittest.main()