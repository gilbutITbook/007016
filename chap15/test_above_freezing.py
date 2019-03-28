import unittest 
import temperature 

class TestAboveFreezing(unittest.TestCase): 
    """temperature.above_freezing을 테스트한다.""" 

    def test_above_freezing_above(self):
        """어떤 온도가 어는점보다 높은지 테스트한다.""" 

        expected = True
        actual = temperature.above_freezing(5.2)
        self.assertEqual(expected, actual, 
            "The temperature is above freezing.")

    def test_above_freezing_below(self): 
        """어떤 온도가 어는점보다 낮은지 테스트한다."""

        expected = False
        actual = temperature.above_freezing(-2)
        self.assertEqual(expected, actual,
            "The temperature is below freezing.")

    def test_above_freezing_at_zero(self): 
        """어떤 온도가 어는점과 같은지 테스트한다."""

        expected = False
        actual = temperature.above_freezing(0)
        self.assertEqual(expected, actual, 
            "The temperature is at the freezing mark.") 

unittest.main()