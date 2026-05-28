class Calculator:
    @staticmethod
    def multiply(a: int,b: int) -> int:
        """Multiply two integers.
        Args:
            a (int): The first integer.
            b (int): The second integer.
        Returns:
            int: The product of a and b."""
        return a * b
    
    @staticmethod
    def calculate_total(*x: float) -> float:
        """Calculate sum of the given list of numbers
        Args:
            *x (list): List of floating numbers.
            
        Returns:
            float: The sum of numbers in list x."""
        return sum(x)
    
    @staticmethod
    def calculate_daily_budget(total: float, days: int) -> float:
        """
        Calculate daily budget
        
        Args:
            total (float): Total budget for the trip.
            days (int): Number of days of the trip.
        
        Returns:
            float: Daily budget for the trip.
        """
        return total/days if days>0 else 0