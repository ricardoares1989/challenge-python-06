def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    # You have to code here!
    def numerator(d):
        assert type(d) == int or type(d) == float or d != 0, 'El denominador ingresado debe ser un numero y diferente a 0 '
        return d / n
    return numerator


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):
        def setUp(self):
            self.n = [[5,2],[8,4],[6,3],[15,2]]
            
        def test_closure_make_division_by(self):
            # Make the closure test here
            for i in self.n:
                division = make_division_by(i[1])
                self.assertEqual(i[0]/i[1] , division(i[0]) )
        
        def tearDown(self):
            del self.n


    # unittest.main()
    run()
