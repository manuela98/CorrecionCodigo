import module
import unittest

class Test(unittest.TestCase):

    def initialize(self):
        self.s=module.Series(3,[1,1/2,1/6])

    def test_function(self):
        try:
            f=module.Series(0,[])
        except:
            print("No class")
        return True
        
    def test_get_value(self):
        self.initialize()
        y=self.s.get_value(1.0)
        self.assertAlmostEqual(y,1.67,places=2)

    def test_get_derivative(self):
        self.initialize()
        y=self.s.get_derivative(1.0)
        self.assertAlmostEqual(y,0.83,places=2)
        
    def test_error_ranges(self):
        self.initialize()
        try:
            e=self.s.Error(10)
        except:
            print("n larger than N passed")
        try:
            e=self.s.Error(-1)
        except:
            print("n negative")

    def test_error(self):
        self.initialize()
        e=self.s.getError(1,1)
        self.assertEqual(e,1)

    def test_clean(self):
        self.initialize()
