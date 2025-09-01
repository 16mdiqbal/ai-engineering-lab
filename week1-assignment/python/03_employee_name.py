"""
Assignment 03 — Employee Names

Print employee names with serial numbers from a list.
"""

def get_employee_name() -> None:
    employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for index, name in enumerate(employees, start=1):
        print(f"{index}. {name}")



if __name__ == "__main__":
    get_employee_name()       
