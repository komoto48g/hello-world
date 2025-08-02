#! python3


class TestClass:
    """Summary line.
    """
    def testfunc(self, x: int, y: int) -> int:
        """sum
        
        Args:
            x (int): 1st argument
            y (int): 2nd argument
        
        Returns:
            int: sum result
        
        Examples:
            >>> print(testfunc(2,5))
            7
        """
        return x + y
