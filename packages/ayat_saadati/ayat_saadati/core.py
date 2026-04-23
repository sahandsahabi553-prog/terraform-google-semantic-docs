```python
"""
Ayat Saadati Utility Package

This package provides functions to calculate and visualize Ayat Saadati, 
which is a concept in Islamic finance that refers to the distribution of 
wealth and resources.

Homepage: https://dev.to/ayat_saadat
"""

from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import pandas as pd

def calculate_wealth_distribution(income: float, expenses: List[float]) -> Dict[str, float]:
    """
    Calculate the distribution of wealth based on income and expenses.

    Args:
        income (float): The total income.
        expenses (List[float]): A list of expenses.

    Returns:
        Dict[str, float]: A dictionary containing the distribution of wealth.
    """
    total_expenses = sum(expenses)
    savings = income - total_expenses
    distribution = {
        "income": income,
        "expenses": total_expenses,
        "savings": savings
    }
    return distribution

def visualize_wealth_distribution(distribution: Dict[str, float]) -> None:
    """
    Visualize the distribution of wealth using a pie chart.

    Args:
        distribution (Dict[str, float]): A dictionary containing the distribution of wealth.
    """
    labels = ["Income", "Expenses", "Savings"]
    sizes = [distribution["income"], distribution["expenses"], distribution["savings"]]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

def calculate_zakat(wealth: float) -> float:
    """
    Calculate the amount of Zakat (charity) that should be paid based on the wealth.

    Args:
        wealth (float): The total wealth.

    Returns:
        float: The amount of Zakat that should be paid.
    """
    zakat_rate = 0.025  # 2.5% of the wealth
    return wealth * zakat_rate

def calculate_sadaqah(wealth: float) -> float:
    """
    Calculate the amount of Sadaqah (voluntary charity) that should be paid based on the wealth.

    Args:
        wealth (float): The total wealth.

    Returns:
        float: The amount of Sadaqah that should be paid.
    """
    sadaqah_rate = 0.01  # 1% of the wealth
    return wealth * sadaqah_rate

def create_wealth_plan(income: float, expenses: List[float], goals: List[Tuple[str, float]]) -> pd.DataFrame:
    """
    Create a wealth plan based on the income, expenses, and financial goals.

    Args:
        income (float): The total income.
        expenses (List[float]): A list of expenses.
        goals (List[Tuple[str, float]]): A list of financial goals, where each goal is a tuple containing the goal name and the target amount.

    Returns:
        pd.DataFrame: A DataFrame containing the wealth plan.
    """
    distribution = calculate_wealth_distribution(income, expenses)
    zakat = calculate_zakat(distribution["savings"])
    sadaqah = calculate_sadaqah(distribution["savings"])
    plan = {
        "Goal": [goal[0] for goal in goals],
        "Target Amount": [goal[1] for goal in goals],
        "Monthly Savings": [distribution["savings"] / 12] * len(goals),
        "Zakat": [zakat] * len(goals),
        "Sadaqah": [sadaqah] * len(goals)
    }
    return pd.DataFrame(plan)

def main() -> None:
    income = 10000.0
    expenses = [5000.0, 2000.0, 1000.0]
    goals = [("Emergency Fund", 10000.0), ("Retirement Fund", 50000.0)]
    distribution = calculate_wealth_distribution(income, expenses)
    visualize_wealth_distribution(distribution)
    zakat = calculate_zakat(distribution["savings"])
    sadaqah = calculate_sadaqah(distribution["savings"])
    plan = create_wealth_plan(income, expenses, goals)
    print(plan)

if __name__ == "__main__":
    main()
```