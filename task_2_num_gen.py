import re
from typing import Callable

def generator_numbers(text: str) -> iter:
    """
    Input: string
    Output: generator of numbers(separetaed by spaces) from string
    """
    pattern = r'-?\d+\.\d{2}' # pattern for positive and negative numbers with two decimal places
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number
        

def sum_profit(text: str, func: Callable[[str], float]) -> float:
    """
    Input: string
    Output: sum of numbers from string
    """
    summury = sum(float(number) for number in func(text))
    
    return summury


if __name__ == '__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")