"""
Assignment 03 — Employee Names

Print employee names with serial numbers from a list.

Usage
- Python: `python ai-engineer-assignment/week1-assignment/python/03_employee_name.py`
- Makefile: `make run W=week1-assignment S=python/03_employee_name.py`
"""
def get_employee_name() -> None:
    employees = ["Alice", "Bob", "Charlie", "David", "Eve"]

    for index, name in enumerate(employees, start=1):
        print(f"{index}. {name}")



if __name__ == "__main__":
    get_employee_name()       
