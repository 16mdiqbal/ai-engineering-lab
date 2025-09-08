
"""
Assignment 05 — Sales Data Summary

Computes total, average (1 decimal), highest, and lowest for a sales list.
"""


def sales_summary(sales: list) -> None:
    """Print total, average, highest and lowest values for the given sales list."""
    
    # Calculate and print total sales
    total_sales = sum(sales)
    print(f"Total Sales: {total_sales}")

    # Calculate and print average sales
    average_sales = total_sales / len(sales)
    print(f"Average Sales: {average_sales:.1f}")

    # highest sales
    highest_sales = max(sales)
    print(f"Highest Sales: {highest_sales}")

    # lowest sales
    lowest_sales = min(sales)
    print(f"Lowest Sales: {lowest_sales}")


if __name__ == "__main__":
    sales = [1200, 3400, 560, 4500, 2100]
    sales_summary(sales)
    
